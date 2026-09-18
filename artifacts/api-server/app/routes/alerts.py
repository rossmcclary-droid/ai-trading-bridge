"""Read-only persistent alert API for Atlas AI Bridge."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.alert_store import (
    active_alerts,
    cancel_alert,
    clear_alerts,
    create_alert,
    evaluate_alert,
    list_alerts,
)


router = APIRouter(
    prefix="/alerts",
    tags=["alerts"],
)


class AlertCreateRequest(BaseModel):
    instrument: str
    condition: str
    trigger_price: float
    timeframe: str | None = None
    reason: str | None = None
    expires_at: str | None = None


class AlertEvaluateRequest(BaseModel):
    current_price: float


@router.post("")
async def add_alert(
    request: AlertCreateRequest,
) -> dict[str, Any]:
    try:
        alert = create_alert(
            instrument=request.instrument,
            condition=request.condition,
            trigger_price=request.trigger_price,
            timeframe=request.timeframe,
            reason=request.reason,
            expires_at=request.expires_at,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error

    return {
        "created": True,
        "alert": alert,
        "read_only": True,
        "broker_order_submitted": False,
    }


@router.get("")
async def get_alerts() -> dict[str, Any]:
    alerts = list_alerts()

    return {
        "alerts": alerts,
        "count": len(alerts),
        "active_count": len(
            [
                alert
                for alert in alerts
                if alert.get("status") == "ACTIVE"
            ]
        ),
        "read_only": True,
    }


@router.get("/active")
async def get_active_alerts() -> dict[str, Any]:
    alerts = active_alerts()

    return {
        "alerts": alerts,
        "count": len(alerts),
        "read_only": True,
    }


@router.post("/{alert_id}/evaluate")
async def evaluate(
    alert_id: str,
    request: AlertEvaluateRequest,
) -> dict[str, Any]:
    alert = evaluate_alert(
        alert_id,
        current_price=request.current_price,
    )

    if alert is None:
        raise HTTPException(
            status_code=404,
            detail="Alert not found.",
        )

    return {
        "evaluated": True,
        "alert": alert,
        "review_required": bool(
            alert.get("review_required")
        ),
        "broker_order_submitted": False,
    }


@router.delete("/{alert_id}")
async def remove_alert(
    alert_id: str,
) -> dict[str, Any]:
    alert = cancel_alert(alert_id)

    if alert is None:
        raise HTTPException(
            status_code=404,
            detail="Alert not found.",
        )

    return {
        "cancelled": True,
        "alert": alert,
        "broker_order_submitted": False,
    }


@router.delete("")
async def remove_all_active_alerts() -> dict[str, Any]:
    count = clear_alerts()

    return {
        "cancelled": count,
        "broker_order_submitted": False,
    }
