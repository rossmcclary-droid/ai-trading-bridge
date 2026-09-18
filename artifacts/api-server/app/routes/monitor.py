"""Server-side market monitoring for Atlas AI Bridge.

The monitor performs read-only scans on a timer. It never approves
or submits an order.
"""

from __future__ import annotations

import json
import asyncio
from datetime import datetime, timezone
from typing import Any
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.routes.scanner import scan_trading_summary
from app.services.tradability_interlock import assert_pending_instrument_tradable
from app.services.practice_session import (
    record_review,
    record_trigger,
)


MONITOR_RECOVERY_PATH = Path("data/atlas_monitor_recovery.json")


def _save_monitor_recovery(
    *,
    enabled: bool,
    nickname: str | None = None,
    symbols: list[str] | None = None,
    interval_seconds: int = 60,
) -> None:
    """Persist desired monitor recovery state."""
    MONITOR_RECOVERY_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    payload = {
        "enabled": bool(enabled),
        "nickname": nickname,
        "symbols": symbols,
        "interval_seconds": int(interval_seconds),
        "updated_at": _utc_now(),
    }

    tmp = MONITOR_RECOVERY_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(payload, indent=2) + "\n")
    tmp.replace(MONITOR_RECOVERY_PATH)


def _load_monitor_recovery() -> dict[str, Any]:
    if not MONITOR_RECOVERY_PATH.exists():
        return {"enabled": False}

    try:
        data = json.loads(MONITOR_RECOVERY_PATH.read_text())
    except Exception:
        return {"enabled": False}

    if not isinstance(data, dict):
        return {"enabled": False}

    return data


router = APIRouter(
    prefix="/monitor",
    tags=["monitor"],
)


class MonitorStartRequest(BaseModel):
    nickname: str = "Challenge"
    symbols: list[str] | None = None
    interval_seconds: int = 60


class ReviewDecisionRequest(BaseModel):
    decision: str
    reason: str | None = None


_monitor_task: asyncio.Task | None = None

_state: dict[str, Any] = {
    "running": False,
    "nickname": None,
    "symbols": None,
    "interval_seconds": 60,
    "started_at": None,
    "last_scan_at": None,
    "scan_count": 0,
    "last_error": None,
    "actionable_trade_found": False,
    "actionable_instrument": None,
    "stop_reason": None,
    "latest_result": None,
    "frozen_trade_plan": None,
    "candidate_ready_for_review": False,
    "workflow_state": "IDLE",
    "external_ai_review_status": None,
    "external_ai_review_reason": None,
    "external_ai_reviewed_at": None,
    "user_action_required": False,
}


def mark_alert_review_required(
    *,
    instrument: str,
    alert: dict[str, Any],
) -> None:
    """Mark a triggered read-only alert for external Atlas reassessment."""
    _state["workflow_state"] = "ALERT_TRIGGERED_REASSESSMENT_REQUIRED"
    _state["external_ai_review_status"] = "PENDING"
    _state["external_ai_review_reason"] = (
        f"Alert triggered for {instrument}: "
        f"{alert.get('condition')} @ {alert.get('trigger_price')}"
    )
    _state["external_ai_reviewed_at"] = None
    _state["user_action_required"] = False
    _state["stop_reason"] = "ALERT_TRIGGERED"
    _state["running"] = False

    _save_monitor_recovery(
        enabled=False,
        nickname=_state.get("nickname"),
        symbols=_state.get("symbols"),
        interval_seconds=int(_state.get("interval_seconds") or 60),
    )

    record_trigger(
        source="alert",
        instrument=instrument,
        details={
            "alert_id": alert.get("id"),
            "condition": alert.get("condition"),
            "trigger_price": alert.get("trigger_price"),
            "triggered_price": alert.get("triggered_price"),
            "timeframe": alert.get("timeframe"),
            "reason": alert.get("reason"),
        },
    )


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _find_actionable(result: dict[str, Any]) -> str | None:
    executable = result.get("executable_orders") or []

    if executable:
        return executable[0].get("instrument") or "Trade"

    pending = result.get("pending_setup")

    if (
        isinstance(pending, dict)
        and pending.get("status") == "READY FOR REASSESSMENT"
    ):
        return pending.get("instrument") or "Trade"

    return None


async def _monitor_loop(
    *,
    nickname: str,
    symbols: list[str] | None,
    interval_seconds: int,
) -> None:
    global _monitor_task

    try:
        while _state["running"]:
            try:
                result = await scan_trading_summary(
                    nickname=nickname,
                    symbols=symbols,
                )

                _state["latest_result"] = result
                _state["last_scan_at"] = _utc_now()
                _state["scan_count"] += 1
                _state["last_error"] = None

                instrument = _find_actionable(result)

                if instrument is not None:
                    executable = result.get("executable_orders") or []
                    pending = result.get("pending_setup")

                    frozen = None

                    if executable:
                        order = executable[0]

                        frozen = {
                            "instrument": order.get("instrument"),
                            "order_type": order.get("order_type"),
                            "entry": order.get("entry"),
                            "safe_loss": order.get("safe_loss"),
                            "take_profit_1": order.get("take_profit_1"),
                            "take_profit_2": order.get("take_profit_2"),
                            "take_profit_3": order.get("take_profit_3"),
                            "grade": order.get("grade"),
                            "reason": order.get("reason"),
                            "captured_at": _utc_now(),
                            "source": "executable_order",
                        }

                    elif isinstance(pending, dict):
                        tradability_ok, tradability_reason, tradability_details = await assert_pending_instrument_tradable(pending, scan_result=result)
                        if not tradability_ok:
                            _state["actionable_trade_found"] = False
                            _state["actionable_instrument"] = None
                            _state["candidate_ready_for_review"] = False
                            _state["frozen_trade_plan"] = None
                            _state["last_error"] = tradability_reason
                            _state["stop_reason"] = tradability_details.get("error") or tradability_reason
                            continue
                        frozen = {
                            "instrument": pending.get("instrument"),
                            "order_type": "Pending",
                            "entry": pending.get("entry_reference"),
                            "safe_loss": pending.get("safe_loss"),
                            "take_profit_1": pending.get("tp1"),
                            "take_profit_2": pending.get("tp2"),
                            "take_profit_3": pending.get("tp3"),
                            "grade": pending.get("grade"),
                            "reason": pending.get("reason"),
                            "captured_at": _utc_now(),
                            "source": "pending_setup",
                        }

                    _state["frozen_trade_plan"] = frozen
                    _state["actionable_trade_found"] = True
                    _state["actionable_instrument"] = instrument
                    _state["candidate_ready_for_review"] = True
                    _state["workflow_state"] = "AWAITING_EXTERNAL_AI_REVIEW"
                    _state["external_ai_review_status"] = "PENDING"
                    _state["external_ai_review_reason"] = None
                    _state["external_ai_reviewed_at"] = None
                    _state["user_action_required"] = False
                    _state["stop_reason"] = "CANDIDATE_READY_FOR_REVIEW"

                    _save_monitor_recovery(
                        enabled=False,
                        nickname=_state.get("nickname"),
                        symbols=_state.get("symbols"),
                        interval_seconds=int(_state.get("interval_seconds") or 60),
                    )

                    record_trigger(
                        source="scan_candidate",
                        instrument=instrument,
                        details={
                            "frozen_trade_plan": frozen,
                            "scan_count": _state.get("scan_count"),
                            "stop_reason": "CANDIDATE_READY_FOR_REVIEW",
                        },
                    )
                    _state["running"] = False
                    break

            except asyncio.CancelledError:
                raise
            except Exception as error:
                _state["last_error"] = (
                    f"{type(error).__name__}: {error}"
                )
                _state["last_scan_at"] = _utc_now()

            if _state["running"]:
                await asyncio.sleep(interval_seconds)

    except asyncio.CancelledError:
        _state["running"] = False

        if _state["stop_reason"] is None:
            _state["stop_reason"] = "MANUAL_STOP"

        raise

    finally:
        _monitor_task = None


@router.post("/start")
async def start_monitor(
    request: MonitorStartRequest,
) -> dict[str, Any]:
    global _monitor_task

    if _state["running"]:
        raise HTTPException(
            status_code=409,
            detail="Monitor is already running.",
        )

    if not 10 <= request.interval_seconds <= 3600:
        raise HTTPException(
            status_code=400,
            detail=(
                "interval_seconds must be between "
                "10 and 3600."
            ),
        )

    if request.symbols is not None and len(request.symbols) > 10:
        raise HTTPException(
            status_code=400,
            detail="Monitor may contain no more than 10 symbols.",
        )

    _state.update(
        {
            "running": True,
            "nickname": request.nickname,
            "symbols": request.symbols,
            "interval_seconds": request.interval_seconds,
            "started_at": _utc_now(),
            "last_scan_at": None,
            "scan_count": 0,
            "last_error": None,
            "actionable_trade_found": False,
            "actionable_instrument": None,
            "stop_reason": None,
            "latest_result": None,
            "frozen_trade_plan": None,
            "candidate_ready_for_review": False,
            "workflow_state": "SCANNING",
            "external_ai_review_status": None,
            "external_ai_review_reason": None,
            "external_ai_reviewed_at": None,
            "user_action_required": False,
        }
    )

    _save_monitor_recovery(
        enabled=True,
        nickname=request.nickname,
        symbols=request.symbols,
        interval_seconds=request.interval_seconds,
    )

    _monitor_task = asyncio.create_task(
        _monitor_loop(
            nickname=request.nickname,
            symbols=request.symbols,
            interval_seconds=request.interval_seconds,
        )
    )

    return {
        "started": True,
        **_state,
    }


@router.post("/stop")
async def stop_monitor() -> dict[str, Any]:
    global _monitor_task

    if not _state["running"]:
        _save_monitor_recovery(
            enabled=False,
            nickname=_state.get("nickname"),
            symbols=_state.get("symbols"),
            interval_seconds=int(_state.get("interval_seconds") or 60),
        )

        return {
            "stopped": False,
            "message": "Monitor is not running.",
            **_state,
        }

    _state["running"] = False
    _state["stop_reason"] = "MANUAL_STOP"

    task = _monitor_task

    if task is not None and not task.done():
        task.cancel()

    return {
        "stopped": True,
        **_state,
    }


@router.post("/review-decision")
async def review_decision(
    request: ReviewDecisionRequest,
) -> dict[str, Any]:
    """Record an advisory decision from external Atlas."""

    if not _state.get("candidate_ready_for_review"):
        raise HTTPException(
            status_code=409,
            detail="No frozen candidate is awaiting review.",
        )

    decision = request.decision.strip().upper()

    allowed = {"APPROVE", "REJECT", "WATCH"}

    if decision not in allowed:
        raise HTTPException(
            status_code=400,
            detail="decision must be APPROVE, REJECT, or WATCH.",
        )

    _state["external_ai_review_status"] = decision
    _state["external_ai_review_reason"] = request.reason
    _state["external_ai_reviewed_at"] = _utc_now()

    if decision == "APPROVE":
        _state["workflow_state"] = "AWAITING_USER_ACTION"
        _state["stop_reason"] = "AWAITING_USER_ACTION"
        _state["user_action_required"] = True
        _state["candidate_ready_for_review"] = False

    elif decision == "REJECT":
        _state["workflow_state"] = "REJECTED_BY_EXTERNAL_AI"
        _state["stop_reason"] = "REJECTED_BY_EXTERNAL_AI"
        _state["user_action_required"] = False
        _state["candidate_ready_for_review"] = False

    else:
        _state["workflow_state"] = "WATCH"
        _state["stop_reason"] = "WATCH"
        _state["user_action_required"] = False

    record_review(
        decision=decision,
        reason=request.reason,
        workflow_state=str(_state.get("workflow_state")),
        user_action_required=bool(
            _state.get("user_action_required")
        ),
    )

    return {
        "recorded": True,
        "broker_order_submitted": False,
        "manual_execution_only": True,
        **_state,
    }


async def recover_monitor_on_startup() -> dict[str, Any]:
    """Resume a monitor that was actively scanning before restart."""
    global _monitor_task

    recovery = _load_monitor_recovery()

    if not recovery.get("enabled"):
        return {
            "recovered": False,
            "reason": "RECOVERY_DISABLED",
        }

    nickname = recovery.get("nickname")
    symbols = recovery.get("symbols")
    interval_seconds = int(recovery.get("interval_seconds") or 60)

    if not nickname:
        return {
            "recovered": False,
            "reason": "MISSING_NICKNAME",
        }

    _state.update(
        {
            "running": True,
            "nickname": nickname,
            "symbols": symbols,
            "interval_seconds": interval_seconds,
            "started_at": _utc_now(),
            "last_scan_at": None,
            "scan_count": 0,
            "last_error": None,
            "actionable_trade_found": False,
            "actionable_instrument": None,
            "stop_reason": None,
            "latest_result": None,
            "frozen_trade_plan": None,
            "candidate_ready_for_review": False,
            "workflow_state": "SCANNING",
            "external_ai_review_status": None,
            "external_ai_review_reason": None,
            "external_ai_reviewed_at": None,
            "user_action_required": False,
        }
    )

    _monitor_task = asyncio.create_task(
        _monitor_loop(
            nickname=str(nickname),
            symbols=symbols,
            interval_seconds=interval_seconds,
        )
    )

    return {
        "recovered": True,
        "nickname": nickname,
        "symbols": symbols,
        "interval_seconds": interval_seconds,
    }


@router.get("/status")
async def monitor_status() -> dict[str, Any]:
    return dict(_state)
