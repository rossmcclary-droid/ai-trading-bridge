#!/usr/bin/env python3
"""Run one, and only one, local Challenge export and emit sanitized evidence."""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


JOB_ID = re.compile(r"^[0-9a-f]{32}$")
POLL_SECONDS = 3.0
MAX_WALL_SECONDS = 480.0


def _read_json(url: str, *, method: str = "GET") -> dict[str, Any]:
    request = Request(url, method=method)
    with urlopen(request, timeout=20) as response:
        body = response.read()
    value = json.loads(body)
    if not isinstance(value, dict):
        raise RuntimeError("Bridge returned a non-object JSON response")
    return value


def _looks_rate_limited(value: Any) -> bool:
    text = str(value).lower()
    return bool(re.search(r"(?:http\s*)?429(?!\d)|too many requests|rate.?limit", text))


_FAILURE_FIELDS = {
    "error_type", "failure_stage", "provider_http_status", "provider_operation",
    "rate_limited", "retry_after_present", "retry_after_seconds",
}


def _copy_failure_telemetry(source: dict[str, Any], evidence: dict[str, Any]) -> None:
    """Copy only the backend's fixed non-secret failure taxonomy."""
    for key in _FAILURE_FIELDS:
        if key in source:
            evidence[key] = source[key]


def _number(value: Any) -> float | None:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return round(float(value), 3)
    return None


def _summary(payload: dict[str, Any], evidence: dict[str, Any]) -> None:
    discovery = payload.get("market_discovery")
    scan = payload.get("scan_status")
    workflow = payload.get("workflow_snapshot")
    diagnostics = payload.get("diagnostics")
    discovery = discovery if isinstance(discovery, dict) else {}
    scan = scan if isinstance(scan, dict) else {}
    workflow = workflow if isinstance(workflow, dict) else {}
    diagnostics = diagnostics if isinstance(diagnostics, dict) else {}

    patch_b = diagnostics.get("patch002b_timings")
    patch_j = diagnostics.get("patch002dj_timings")
    patch_b = patch_b if isinstance(patch_b, dict) else {}
    patch_j = patch_j if isinstance(patch_j, dict) else {}
    top = patch_j.get("top_level")
    top = top if isinstance(top, dict) else {}
    discovery_timing = top.get("discovery")
    discovery_timing = discovery_timing if isinstance(discovery_timing, dict) else {}

    evidence["metrics"] = {
        "wall_ms": evidence.get("wall_ms"),
        "discovery_ms": _number(
            discovery_timing.get("ms")
            if discovery_timing.get("ms") is not None
            else discovery.get("timing_parent_total_ms")
        ),
        "export_function_ms": _number(patch_b.get("export_ai_scan_total_ms")),
        "selected_count": discovery.get("selected_count"),
        "selected_symbols": discovery.get("selected_symbols", []),
        "deep_analysis_requested": scan.get("deep_analysis_requested"),
        "deep_analysis_successful": scan.get("deep_analysis_successful"),
        "deep_analysis_missing": scan.get("deep_analysis_missing"),
        "deep_analysis_missing_symbols": scan.get(
            "deep_analysis_missing_symbols", []
        ),
        "workflow_ready": workflow.get("workflow_ready"),
        "overall_scan_complete": scan.get("overall_scan_complete"),
    }


def main() -> int:
    base_url = os.environ.get("BRIDGE_BASE_URL", "http://127.0.0.1:8765").rstrip("/")
    output_path = Path(
        os.environ.get("BRIDGE_EVIDENCE_PATH", "bridge-benchmark-evidence.json")
    )
    evidence: dict[str, Any] = {
        "schema": "bridge.challenge-benchmark.summary.v1",
        "nickname": "Challenge",
        "source_revision": os.environ.get("BRIDGE_EXPECTED_SHA"),
        "start_post_count": 0,
        "poll_uses_exact_job_id": True,
        "automatic_retry": False,
        "raw_payload_preserved": False,
        "status": "PREPARING",
        "rate_limited": False,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)

    def save() -> None:
        output_path.write_text(
            json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

    save()
    readiness_started = time.monotonic()
    benchmark_started: float | None = None

    def benchmark_elapsed_ms() -> float | None:
        if benchmark_started is None:
            return None
        return round((time.monotonic() - benchmark_started) * 1000, 3)

    try:
        readiness_deadline = readiness_started + 30.0
        while True:
            try:
                _read_json(f"{base_url}/api/health")
                break
            except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
                if time.monotonic() >= readiness_deadline:
                    raise RuntimeError("local_api_not_ready")
                time.sleep(1.0)
        evidence["api_readiness_wait_ms"] = round(
            (time.monotonic() - readiness_started) * 1000, 3
        )

        # This is the sole POST in this program. It is deliberately outside
        # any retry loop and the exact response ID is retained for all polls.
        evidence["start_post_count"] = 1
        benchmark_started = time.monotonic()
        started_job = _read_json(
            f"{base_url}/api/scan/Challenge/export-ai/start", method="POST"
        )
        job_id = started_job.get("job_id")
        if not isinstance(job_id, str) or JOB_ID.fullmatch(job_id) is None:
            raise RuntimeError("invalid_job_id")
        evidence["job_id"] = job_id
        evidence["status"] = "BUILDING"
        save()

        terminal: dict[str, Any] | None = None
        benchmark_deadline = benchmark_started + MAX_WALL_SECONDS
        while time.monotonic() < benchmark_deadline:
            polled = _read_json(f"{base_url}/api/scan/export-ai/jobs/{job_id}")
            if polled.get("job_id") != job_id:
                raise RuntimeError("poll_job_id_mismatch")
            status = polled.get("status")
            if status in {"READY", "FAILED"}:
                terminal = polled
                break
            if status != "BUILDING":
                raise RuntimeError("unexpected_job_status")
            time.sleep(POLL_SECONDS)

        evidence["wall_ms"] = benchmark_elapsed_ms()
        if terminal is None:
            evidence["status"] = "TIMEOUT"
            evidence["failure_category"] = "benchmark_timeout"
            save()
            return 1

        evidence["status"] = str(terminal.get("status"))
        if terminal.get("status") == "FAILED":
            _copy_failure_telemetry(terminal, evidence)
            evidence["failure_category"] = (
                "provider_rate_limited"
                if evidence.get("rate_limited") is True
                else "export_failed"
            )
            save()
            return 1

        payload = _read_json(
            f"{base_url}/api/scan/export-ai/jobs/{job_id}/download"
        )
        _summary(payload, evidence)
        evidence["status"] = "READY"
        save()
        return 0

    except HTTPError as error:
        evidence["wall_ms"] = benchmark_elapsed_ms()
        evidence["rate_limited"] = error.code == 429
        evidence["status"] = "FAILED"
        evidence["failure_category"] = (
            "provider_rate_limited" if error.code == 429 else "http_failure"
        )
        save()
        return 1
    except Exception as error:
        evidence["wall_ms"] = benchmark_elapsed_ms()
        evidence["rate_limited"] = _looks_rate_limited(error)
        evidence["status"] = "FAILED"
        category = str(error)
        evidence["failure_category"] = (
            category
            if category
            in {
                "local_api_not_ready",
                "invalid_job_id",
                "poll_job_id_mismatch",
                "unexpected_job_status",
            }
            else "harness_failure"
        )
        save()
        return 1


if __name__ == "__main__":
    sys.exit(main())
