"""Practice-run audit trail for Atlas AI Bridge."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


STORE_PATH = Path("data/atlas_practice_session.json")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _default() -> dict[str, Any]:
    return {
        "practice_mode": True,
        "session_started_at": None,
        "session_updated_at": None,
        "trigger_source": None,
        "instrument": None,
        "trigger_details": None,
        "review_status": None,
        "review_reason": None,
        "reviewed_at": None,
        "user_action_required": False,
        "workflow_state": "IDLE",
        "broker_execution_allowed": False,
        "broker_order_submitted": False,
        "events": [],
    }


def _load() -> dict[str, Any]:
    if not STORE_PATH.exists():
        return _default()

    try:
        data = json.loads(STORE_PATH.read_text())
    except Exception:
        return _default()

    if not isinstance(data, dict):
        return _default()

    if not isinstance(data.get("events"), list):
        data["events"] = []

    return data


def _save(data: dict[str, Any]) -> None:
    STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
    data["session_updated_at"] = _utc_now()

    tmp = STORE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, default=str) + "\n")
    tmp.replace(STORE_PATH)


def reset_session() -> dict[str, Any]:
    data = _default()
    data["session_started_at"] = _utc_now()
    _save(data)
    return data


def record_event(
    event_type: str,
    *,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    data = _load()

    if data.get("session_started_at") is None:
        data["session_started_at"] = _utc_now()

    event = {
        "type": event_type,
        "at": _utc_now(),
        "details": details or {},
    }

    data["events"].append(event)
    _save(data)
    return data


def record_trigger(
    *,
    source: str,
    instrument: str | None,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    data = _load()

    if data.get("session_started_at") is None:
        data["session_started_at"] = _utc_now()

    data["trigger_source"] = source
    data["instrument"] = instrument
    data["trigger_details"] = details
    data["workflow_state"] = "AWAITING_EXTERNAL_AI_REVIEW"
    data["review_status"] = "PENDING"
    data["user_action_required"] = False

    data["events"].append(
        {
            "type": "TRIGGER",
            "at": _utc_now(),
            "details": {
                "source": source,
                "instrument": instrument,
                "trigger_details": details,
            },
        }
    )

    _save(data)
    return data


def record_review(
    *,
    decision: str,
    reason: str | None,
    workflow_state: str,
    user_action_required: bool,
) -> dict[str, Any]:
    data = _load()

    data["review_status"] = decision
    data["review_reason"] = reason
    data["reviewed_at"] = _utc_now()
    data["workflow_state"] = workflow_state
    data["user_action_required"] = user_action_required
    data["broker_execution_allowed"] = False
    data["broker_order_submitted"] = False

    data["events"].append(
        {
            "type": "EXTERNAL_AI_REVIEW",
            "at": _utc_now(),
            "details": {
                "decision": decision,
                "reason": reason,
                "workflow_state": workflow_state,
                "user_action_required": user_action_required,
            },
        }
    )

    _save(data)
    return data


def get_session() -> dict[str, Any]:
    return _load()
