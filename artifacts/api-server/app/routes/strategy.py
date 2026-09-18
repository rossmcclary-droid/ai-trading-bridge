"""Read-only Trading Brain configuration endpoint."""

from fastapi import APIRouter

from app.models.strategy import active_strategy

router = APIRouter(tags=["strategy"])


@router.get("/strategy", response_model=active_strategy.__class__)
async def get_strategy() -> active_strategy.__class__:
    """Return active bootstrap metadata without exposing strategy rules."""

    return active_strategy