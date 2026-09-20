import ast
import asyncio
from email.message import Message
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from app.services.failure_telemetry import sanitize_failure


ROOT = Path(__file__).parents[3]
HARNESS_PATH = ROOT / "scripts" / "bridge_challenge_benchmark.py"


def load_harness():
    spec = importlib.util.spec_from_file_location("bridge_challenge_benchmark", HARNESS_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SanitizedFailureTelemetryTests(unittest.TestCase):
    def test_adversarial_exception_never_preserves_secret_material(self):
        secret_values = [
            "person@example.com", "p@ssword-123", "demo-server-secret",
            "api-key-secret", "https://provider.invalid/account/123", "Bearer token-secret",
        ]
        EvilSecretClass = type("Password_person_example_com", (RuntimeError,), {})
        error = EvilSecretClass(" ".join(secret_values))
        error.response = type("Response", (), {
            "status_code": 503,
            "body": "p@ssword-123",
            "headers": {"Authorization": "Bearer token-secret"},
            "url": "https://provider.invalid/account/123",
        })()
        error.provider_operation = "accounts"
        error.failure_stage = "account_discovery"

        result = sanitize_failure(error)
        serialized = json.dumps(result, sort_keys=True)

        self.assertEqual(result["error_type"], "UnknownError")
        self.assertEqual(result["provider_http_status"], 503)
        self.assertEqual(result["provider_operation"], "accounts")
        self.assertEqual(result["failure_stage"], "account_discovery")
        for secret in secret_values:
            self.assertNotIn(secret, serialized)
        self.assertEqual(
            set(result),
            {
                "error_type", "failure_stage", "provider_http_status",
                "provider_operation", "rate_limited", "retry_after_present",
                "retry_after_seconds",
            },
        )

    def test_429_and_safe_numeric_retry_after_are_reported(self):
        error = RuntimeError("message deliberately ignored")
        error.status_code = 429
        error.retry_after = "12.5"
        error.provider_operation = "history"
        error.failure_stage = "deep_analysis"

        result = sanitize_failure(error)

        self.assertTrue(result["rate_limited"])
        self.assertEqual(result["provider_http_status"], 429)
        self.assertTrue(result["retry_after_present"])
        self.assertEqual(result["retry_after_seconds"], 12.5)

    def test_real_http_error_reads_only_numeric_retry_after_header(self):
        headers = Message()
        headers["Retry-After"] = "17"
        headers["Authorization"] = "Bearer super-secret-token"
        headers["X-Account"] = "account-secret"
        error = HTTPError(
            "https://provider.invalid/path?email=person@example.com",
            429,
            "password-secret",
            headers,
            None,
        )

        result = sanitize_failure(
            error,
            failure_stage="deep_analysis",
            provider_operation="history",
        )
        serialized = json.dumps(result, sort_keys=True)

        self.assertEqual(result["error_type"], "HTTPError")
        self.assertEqual(result["provider_http_status"], 429)
        self.assertTrue(result["rate_limited"])
        self.assertTrue(result["retry_after_present"])
        self.assertEqual(result["retry_after_seconds"], 17.0)
        for secret in (
            "super-secret-token", "account-secret", "person@example.com",
            "password-secret", "Authorization", "X-Account",
        ):
            self.assertNotIn(secret, serialized)

    def test_unsafe_retry_after_is_only_reported_as_present(self):
        error = RuntimeError("opaque")
        error.retry_after = "Saturday, 20 Sep 2026 12:00:00 GMT; token=secret"
        result = sanitize_failure(error)
        self.assertTrue(result["retry_after_present"])
        self.assertIsNone(result["retry_after_seconds"])
        self.assertNotIn("Saturday", json.dumps(result))

    def test_unknown_failure_uses_closed_taxonomy(self):
        Unknown = type("Token_super_secret", (Exception,), {})
        result = sanitize_failure(Unknown("email@example.com password"))
        self.assertEqual(result["error_type"], "UnknownError")
        self.assertEqual(result["failure_stage"], "export")
        self.assertEqual(result["provider_operation"], "application")
        self.assertIsNone(result["provider_http_status"])
        self.assertFalse(result["rate_limited"])

    def test_harness_copies_only_allowlisted_failure_taxonomy_and_posts_once(self):
        harness = load_harness()
        calls = []
        terminal = {
            "job_id": "a" * 32,
            "status": "FAILED",
            "error": "person@example.com p@ssword token-secret",
            "error_type": "RuntimeError",
            "failure_stage": "deep_analysis",
            "provider_http_status": 429,
            "provider_operation": "history",
            "rate_limited": True,
            "retry_after_present": True,
            "retry_after_seconds": 9.0,
            "response_body": "secret-body",
            "headers": {"Authorization": "secret"},
        }

        def fake_read(url, *, method="GET"):
            calls.append((method, url))
            if url.endswith("/api/health"):
                return {"ok": True}
            if method == "POST":
                return {"job_id": "a" * 32}
            return terminal

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "evidence.json"
            with patch.object(harness, "_read_json", side_effect=fake_read), patch.dict(
                os.environ, {"BRIDGE_EVIDENCE_PATH": str(output)}, clear=False
            ):
                result = harness.main()
            evidence = json.loads(output.read_text())

        self.assertEqual(result, 1)
        self.assertEqual([call for call in calls if call[0] == "POST"], [
            ("POST", "http://127.0.0.1:8765/api/scan/Challenge/export-ai/start")
        ])
        self.assertEqual(evidence["start_post_count"], 1)
        self.assertFalse(evidence["automatic_retry"])
        self.assertEqual(evidence["provider_operation"], "history")
        serialized = json.dumps(evidence)
        self.assertNotIn("person@example.com", serialized)
        self.assertNotIn("secret-body", serialized)
        self.assertNotIn("Authorization", serialized)

    def test_post_response_timing_and_null_payload_guards_are_present(self):
        source = ROOT / "artifacts" / "api-server" / "app" / "routes" / "exports.py"
        tree = ast.parse(source.read_text())
        function = next(
            node for node in tree.body
            if isinstance(node, ast.AsyncFunctionDef) and node.name == "_run_ai_scan_export_job"
        )
        assignments = [
            node for node in ast.walk(function)
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "_payload_assembly_started" for target in node.targets)
        ]
        self.assertEqual(len(assignments), 1)
        guarded_payload_checks = [
            node for node in ast.walk(function)
            if isinstance(node, ast.If)
            and "_job_payload is not None" in ast.unparse(node.test)
        ]
        self.assertGreaterEqual(len(guarded_payload_checks), 2)

    def test_get_job_omits_failure_taxonomy_for_building_and_ready(self):
        source = ROOT / "artifacts" / "api-server" / "app" / "routes" / "exports.py"
        tree = ast.parse(source.read_text())
        function = next(
            node for node in tree.body
            if isinstance(node, ast.AsyncFunctionDef) and node.name == "get_ai_scan_export_job"
        )
        function.decorator_list = []
        namespace = {"Any": object}
        exec(
            compile(ast.Module(body=[function], type_ignores=[]), str(source), "exec"),
            namespace,
        )
        get_job = namespace["get_ai_scan_export_job"]
        base_job = {
            "job_id": "a" * 32,
            "nickname": "Challenge",
            "created_at": "2026-09-20T00:00:00+00:00",
            "completed_at": None,
            "filename": None,
            "error": None,
            "error_type": "RuntimeError",
            "failure_stage": "export",
            "provider_http_status": 500,
            "provider_operation": "application",
            "rate_limited": False,
            "retry_after_present": False,
            "retry_after_seconds": None,
        }

        async def exercise(status):
            namespace["_load_export_job"] = lambda _job_id: {
                **base_job,
                "status": status,
            }
            return await get_job("a" * 32)

        for status in ("BUILDING", "READY"):
            result = asyncio.run(exercise(status))
            for key in (
                "error_type", "failure_stage", "provider_http_status",
                "provider_operation", "rate_limited", "retry_after_present",
                "retry_after_seconds",
            ):
                self.assertNotIn(key, result)

        failed = asyncio.run(exercise("FAILED"))
        self.assertEqual(failed["failure_stage"], "export")
        self.assertEqual(failed["provider_operation"], "application")


if __name__ == "__main__":
    unittest.main()
