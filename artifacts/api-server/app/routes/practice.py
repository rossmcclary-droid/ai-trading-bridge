"""Practice-session inspection API for Atlas AI Bridge."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from app.services.practice_session import (
    get_session,
    reset_session,
)


router = APIRouter(
    prefix="/practice",
    tags=["practice"],
)


@router.get("/status")
async def practice_status() -> dict[str, Any]:
    return get_session()


@router.post("/reset")
async def practice_reset() -> dict[str, Any]:
    session = reset_session()

    return {
        "reset": True,
        "practice_mode": True,
        "broker_order_submitted": False,
        "session": session,
    }
