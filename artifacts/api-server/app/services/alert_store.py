"""Persistent read-only alert storage for Atlas AI Bridge."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4


STORE_PATH = Path("data/atlas_alerts.json")
MAX_ACTIVE_ALERTS = 6

VALID_CONDITIONS = {
    "PRICE_ABOVE",
    "PRICE_BELOW",
    "PRICE_CROSSES_ABOVE",
    "PRICE_CROSSES_BELOW",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_store() -> None:
    STORE_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not STORE_PATH.exists():
        STORE_PATH.write_text(
            json.dumps(
                {
                    "alerts": [],
                    "updated_at": _utc_now(),
                },
                indent=2,
            )
            + "\n"
        )


def _load() -> dict[str, Any]:
    _ensure_store()

    try:
        data = json.loads(STORE_PATH.read_text())
    except Exception:
        data = {
            "alerts": [],
            "updated_at": _utc_now(),
        }

    if not isinstance(data, dict):
        data = {}

    if not isinstance(data.get("alerts"), list):
        data["alerts"] = []

    return data


def _save(data: dict[str, Any]) -> None:
    data["updated_at"] = _utc_now()

    tmp = STORE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, default=str) + "\n")
    tmp.replace(STORE_PATH)


def list_alerts() -> list[dict[str, Any]]:
    return list(_load()["alerts"])


def active_alerts() -> list[dict[str, Any]]:
    return [
        alert
        for alert in list_alerts()
        if alert.get("status") == "ACTIVE"
    ]


def create_alert(
    *,
    instrument: str,
    condition: str,
    trigger_price: float,
    timeframe: str | None = None,
    reason: str | None = None,
    expires_at: str | None = None,
) -> dict[str, Any]:
    condition = condition.strip().upper()
    instrument = instrument.strip().upper()

    if condition not in VALID_CONDITIONS:
        raise ValueError(
            "condition must be one of: "
            + ", ".join(sorted(VALID_CONDITIONS))
        )

    if not instrument:
        raise ValueError("instrument is required.")

    data = _load()

    active = [
        alert
        for alert in data["alerts"]
        if alert.get("status") == "ACTIVE"
    ]

    if len(active) >= MAX_ACTIVE_ALERTS:
        raise ValueError(
            f"No more than {MAX_ACTIVE_ALERTS} active alerts are allowed."
        )

    alert = {
        "id": uuid4().hex,
        "instrument": instrument,
        "condition": condition,
        "trigger_price": float(trigger_price),
        "timeframe": timeframe,
        "reason": reason,
        "expires_at": expires_at,
        "status": "ACTIVE",
        "created_at": _utc_now(),
        "updated_at": _utc_now(),
        "triggered_at": None,
        "triggered_price": None,
        "previous_price": None,
        "last_checked_at": None,
        "last_price": None,
        "review_required": False,
        "read_only": True,
        "broker_order_submitted": False,
    }

    data["alerts"].append(alert)
    _save(data)

    return alert


def cancel_alert(alert_id: str) -> dict[str, Any] | None:
    data = _load()

    for alert in data["alerts"]:
        if alert.get("id") == alert_id:
            alert["status"] = "CANCELLED"
            alert["updated_at"] = _utc_now()
            _save(data)
            return alert

    return None


def clear_alerts() -> int:
    data = _load()
    count = 0

    for alert in data["alerts"]:
        if alert.get("status") == "ACTIVE":
            alert["status"] = "CANCELLED"
            alert["updated_at"] = _utc_now()
            count += 1

    _save(data)
    return count


def evaluate_alert(
    alert_id: str,
    *,
    current_price: float,
) -> dict[str, Any] | None:
    """
    Evaluate one alert against a supplied normalized market price.

    This function cannot place or modify an order.
    """
    data = _load()

    for alert in data["alerts"]:
        if alert.get("id") != alert_id:
            continue

        if alert.get("status") != "ACTIVE":
            return alert

        price = float(current_price)
        previous = alert.get("last_price")
        condition = alert.get("condition")
        level = float(alert.get("trigger_price"))

        triggered = False

        if condition == "PRICE_ABOVE":
            triggered = price >= level

        elif condition == "PRICE_BELOW":
            triggered = price <= level

        elif condition == "PRICE_CROSSES_ABOVE":
            triggered = (
                previous is not None
                and float(previous) < level
                and price >= level
            )

        elif condition == "PRICE_CROSSES_BELOW":
            triggered = (
                previous is not None
                and float(previous) > level
                and price <= level
            )

        alert["previous_price"] = previous
        alert["last_price"] = price
        alert["last_checked_at"] = _utc_now()
        alert["updated_at"] = _utc_now()

        if triggered:
            alert["status"] = "TRIGGERED"
            alert["triggered_at"] = _utc_now()
            alert["triggered_price"] = price
            alert["review_required"] = True

        _save(data)
        return alert

    return None
