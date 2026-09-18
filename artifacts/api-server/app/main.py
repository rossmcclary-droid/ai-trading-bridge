"""Application entrypoint for AI Trading Bridge."""

from fastapi import FastAPI

from app.routes.accounts import router as accounts_router
from app.routes.health import router as health_router
from app.routes.strategy import router as strategy_router
from app.routes.scanner import router as scanner_router

from app.routes.approvals import router as approvals_router
from app.routes.exports import router as exports_router
from app.routes.bootstrap import router as bootstrap_router
from app.routes.monitor import router as monitor_router, recover_monitor_on_startup
from app.routes.alerts import router as alerts_router
from app.routes.practice import router as practice_router
app = FastAPI(
    title="AI Trading Bridge",
    description=(
        "A read-only trading data bridge. Trade execution is intentionally "
        "not supported."
    ),
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(accounts_router)
app.include_router(strategy_router)
app.include_router(scanner_router)
app.include_router(approvals_router)
app.include_router(bootstrap_router)
app.include_router(monitor_router)
app.include_router(alerts_router)
app.include_router(practice_router)
app.include_router(exports_router)
# Artifact routing keeps the /api service prefix in the request path. Keep
# the application route available at /health as well for direct ASGI usage.
app.include_router(health_router, prefix="/api")
app.include_router(accounts_router, prefix="/api")
app.include_router(strategy_router, prefix="/api")
app.include_router(scanner_router, prefix="/api")
app.include_router(approvals_router, prefix="/api")
app.include_router(bootstrap_router, prefix="/api")
app.include_router(monitor_router, prefix="/api")
app.include_router(alerts_router, prefix="/api")
app.include_router(practice_router, prefix="/api")
app.include_router(exports_router, prefix="/api")


@app.on_event("startup")
async def atlas_monitor_recovery_startup() -> None:
    await recover_monitor_on_startup()
