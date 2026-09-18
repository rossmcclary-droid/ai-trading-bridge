"""Small durable store for background AI Scan export job metadata."""

from __future__ import annotations

import copy
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

try:
    import fcntl
except ImportError:  # pragma: no cover
    fcntl = None

_ROOT = Path(__file__).resolve().parents[2] / "data" / "export_jobs"
_INDEX = _ROOT / "jobs.json"
_LOCK = _ROOT / "jobs.lock"
_RESULTS = _ROOT / "results"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _lock(exclusive: bool):
    class _FileLock:
        def __enter__(self):
            _ROOT.mkdir(parents=True, exist_ok=True)
            self.handle = _LOCK.open("a+")
            if fcntl is not None:
                fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
            return self

        def __exit__(self, exc_type, exc, tb):
            if fcntl is not None:
                fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
            self.handle.close()

    return _FileLock()


def _read_index() -> dict[str, dict[str, Any]]:
    if not _INDEX.exists():
        return {}
    try:
        value = json.loads(_INDEX.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return {}
    return value if isinstance(value, dict) else {}

def _write_index(jobs: dict[str, dict[str, Any]]) -> None:
    _ROOT.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=_ROOT, prefix=".jobs-", suffix=".tmp", delete=False) as handle:
        json.dump(jobs, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
        temp_name = handle.name
    os.replace(temp_name, _INDEX)


def _write_result(job_id: str, content: bytes) -> str:
    _RESULTS.mkdir(parents=True, exist_ok=True)
    result_path = _RESULTS / f"{job_id}.json"
    with tempfile.NamedTemporaryFile(mode="wb", dir=_RESULTS, prefix=f".{job_id}-", suffix=".tmp", delete=False) as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
        temp_name = handle.name
    os.replace(temp_name, result_path)
    return str(result_path)


def _serializable_job(job: dict[str, Any]) -> dict[str, Any]:
    stored = copy.deepcopy(job)
    content = stored.pop("content", None)
    if content is not None and stored.get("status") == "READY":
        stored["result_path"] = _write_result(stored["job_id"], bytes(content))
        stored["content_size"] = len(content)
    stored.pop("content", None)
    return stored


def save_job(job: dict[str, Any]) -> dict[str, Any]:
    """Atomically persist one job and return its in-memory representation."""
    job["updated_at"] = _now()
    with _lock(True):
        jobs = _read_index()
        stored = _serializable_job(job)
        jobs[str(stored["job_id"])] = stored
        _write_index(jobs)
    if stored.get("result_path"):
        job["result_path"] = stored["result_path"]
        if "content_size" in stored:
            job["content_size"] = stored["content_size"]
    return job

def get_job(job_id: str, *, include_content: bool = False) -> dict[str, Any] | None:
    with _lock(False):
        stored = _read_index().get(job_id)
    if not isinstance(stored, dict):
        return None
    job = copy.deepcopy(stored)
    if include_content and job.get("result_path"):
        try:
            job["content"] = Path(job["result_path"]).read_bytes()
        except OSError:
            job["content"] = None
    return job


def reconcile_orphans(live_job_ids: Iterable[str] = ()) -> list[str]:
    """Fail persisted BUILDING jobs that have no task in this process."""
    live = {str(value) for value in live_job_ids}
    interrupted: list[str] = []
    with _lock(True):
        jobs = _read_index()
        changed = False
        now = _now()
        for job_id, job in jobs.items():
            if job.get("status") == "BUILDING" and job_id not in live:
                job["status"] = "FAILED"
                job["error"] = "WORKER_RESTARTED_BEFORE_COMPLETION"
                job["completed_at"] = now
                job["updated_at"] = now
                interrupted.append(job_id)
                changed = True
        if changed:
            _write_index(jobs)
    return interrupted
