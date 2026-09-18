"""Service health endpoint."""

from fastapi import APIRouter
from pydantic import BaseModel

from app.config import MODE, SERVICE_NAME

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Stable health-check response contract."""

    status: str
    service: str
    mode: str


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Confirm that the bridge is running in read-only mode."""

    return HealthResponse(status="ok", service=SERVICE_NAME, mode=MODE.value)