"""Cache for read-only TradeLocker enrichment data.

Quotes and other fast-changing data remain process-local.

Instrument specifications are also persisted to disk because:
- they change infrequently,
- TradeLocker's instrument-detail endpoint is highly rate-limited,
- Uvicorn --reload otherwise destroys the warmed in-memory cache.

No trade authorization or execution data is stored here.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any


_CACHE: dict[str, dict[str, Any]] = {}

_CACHE_FILE = (
    Path(__file__).resolve().parents[2]
    / ".cache"
    / "atlas_broker_cache.json"
)

_PERSISTENT_NAMESPACES = {
    "instrument_specs",
}


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _key(namespace: str, identity: str) -> str:
    return f"{namespace}:{identity}"


def _load_persistent_cache() -> None:
    if not _CACHE_FILE.exists():
        return

    try:
        payload = json.loads(_CACHE_FILE.read_text())
    except Exception:
        return

    if not isinstance(payload, dict):
        return

    for key, entry in payload.items():
        if not isinstance(entry, dict):
            continue

        captured_raw = entry.get("captured_at")

        try:
            captured_at = datetime.fromisoformat(
                str(captured_raw)
            )
        except Exception:
            continue

        if captured_at.tzinfo is None:
            captured_at = captured_at.replace(
                tzinfo=timezone.utc
            )

        _CACHE[key] = {
            "value": entry.get("value"),
            "captured_at": captured_at,
        }


def _save_persistent_cache() -> None:
    payload: dict[str, Any] = {}

    for key, entry in _CACHE.items():
        namespace = key.split(":", 1)[0]

        if namespace not in _PERSISTENT_NAMESPACES:
            continue

        captured_at = entry.get("captured_at")

        if not isinstance(captured_at, datetime):
            continue

        payload[key] = {
            "value": entry.get("value"),
            "captured_at": captured_at.isoformat(),
        }

    _CACHE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp = _CACHE_FILE.with_suffix(".tmp")

    temp.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
            default=str,
        )
    )

    temp.replace(_CACHE_FILE)


def set_cached(
    namespace: str,
    identity: str,
    value: Any,
) -> None:
    _CACHE[_key(namespace, identity)] = {
        "value": value,
        "captured_at": _utc_now(),
    }

    if namespace in _PERSISTENT_NAMESPACES:
        _save_persistent_cache()


def get_cached(
    namespace: str,
    identity: str,
    *,
    ttl_seconds: float,
) -> dict[str, Any] | None:
    entry = _CACHE.get(
        _key(namespace, identity)
    )

    if not isinstance(entry, dict):
        return None

    captured_at = entry.get("captured_at")

    if not isinstance(captured_at, datetime):
        return None

    age_seconds = (
        _utc_now() - captured_at
    ).total_seconds()

    if age_seconds > ttl_seconds:
        return None

    return {
        "value": entry.get("value"),
        "captured_at": captured_at.isoformat(),
        "age_seconds": round(age_seconds, 3),
    }


def get_cached_even_if_stale(
    namespace: str,
    identity: str,
) -> dict[str, Any] | None:
    entry = _CACHE.get(
        _key(namespace, identity)
    )

    if not isinstance(entry, dict):
        return None

    captured_at = entry.get("captured_at")

    if not isinstance(captured_at, datetime):
        return None

    age_seconds = (
        _utc_now() - captured_at
    ).total_seconds()

    return {
        "value": entry.get("value"),
        "captured_at": captured_at.isoformat(),
        "age_seconds": round(age_seconds, 3),
    }


def cache_status() -> dict[str, Any]:
    now = _utc_now()
    items = {}

    for key, entry in _CACHE.items():
        captured_at = entry.get("captured_at")
        age_seconds = None

        if isinstance(captured_at, datetime):
            age_seconds = round(
                (now - captured_at).total_seconds(),
                3,
            )

        items[key] = {
            "captured_at": (
                captured_at.isoformat()
                if isinstance(captured_at, datetime)
                else None
            ),
            "age_seconds": age_seconds,
        }

    return {
        "entry_count": len(_CACHE),
        "persistent_file": str(_CACHE_FILE),
        "entries": items,
    }


_load_persistent_cache()
