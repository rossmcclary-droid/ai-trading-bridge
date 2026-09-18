"""Human trade-approval endpoints.

Records explicit user authorization and can construct a validated
DRY-RUN execution preview.

Broker submission remains disabled.
"""

from enum import StrEnum

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.execution import (
    ExecutionValidationError,
    build_execution_preview,
)


router = APIRouter(prefix="/approvals", tags=["approvals"])


class ApprovalAction(StrEnum):
    APP = "App"
    APP_AND_EXPLAIN = "App + Exp"
    EXPLAIN = "Exp"
    REJECT = "Rej"
    APP_ALL = "App All"


class ApprovalRequest(BaseModel):
    action: ApprovalAction
    instrument: str
    account: str | None = None

    direction: str | None = None
    entry: float | None = None
    safe_loss: float | None = None
    take_profit_1: float | None = None
    take_profit_2: float | None = None
    take_profit_3: float | None = None


@router.post("")
async def submit_approval(request: ApprovalRequest) -> dict[str, object]:
    approved = request.action in {
        ApprovalAction.APP,
        ApprovalAction.APP_AND_EXPLAIN,
        ApprovalAction.APP_ALL,
    }

    explanation_requested = request.action in {
        ApprovalAction.APP_AND_EXPLAIN,
        ApprovalAction.EXPLAIN,
    }

    rejected = request.action == ApprovalAction.REJECT

    result: dict[str, object] = {
        "accepted": True,
        "action": request.action,
        "instrument": request.instrument,
        "account": request.account,
        "approved": approved,
        "rejected": rejected,
        "explanation_requested": explanation_requested,
        "all_accounts": request.action == ApprovalAction.APP_ALL,
        "execution_status": "BLOCKED",
        "execution_enabled": False,
        "execution_preview": None,
    }

    if approved:
        geometry = (
            request.direction,
            request.entry,
            request.safe_loss,
            request.take_profit_1,
            request.take_profit_2,
        )

        if all(value is not None for value in geometry):
            try:
                preview = build_execution_preview(
                    instrument=request.instrument,
                    direction=request.direction,
                    entry=request.entry,
                    safe_loss=request.safe_loss,
                    take_profit_1=request.take_profit_1,
                    take_profit_2=request.take_profit_2,
                    take_profit_3=request.take_profit_3,
                    account=request.account or "unknown",
                    approved=True,
                    all_accounts=request.action == ApprovalAction.APP_ALL,
                )

                result["execution_preview"] = {
                    "instrument": preview.instrument,
                    "side": preview.side,
                    "entry": preview.entry,
                    "safe_loss": preview.safe_loss,
                    "take_profit_1": preview.take_profit_1,
                    "take_profit_2": preview.take_profit_2,
                    "take_profit_3": preview.take_profit_3,
                    "account": preview.account,
                    "scope": preview.scope,
                    "broker_payload": preview.broker_payload,
                }

                result["execution_status"] = preview.execution_status

            except ExecutionValidationError as error:
                result["execution_status"] = "VALIDATION_BLOCKED"
                result["validation_error"] = str(error)

    if rejected:
        result["message"] = "Trade rejected. No execution permitted."
    elif approved and result["execution_preview"] is not None:
        result["message"] = (
            "Approval recorded. Dry-run execution preview prepared. "
            "Broker submission remains disabled."
        )
    elif approved:
        result["message"] = (
            "Approval recorded. No execution preview was prepared because "
            "complete trade geometry was not supplied."
        )
    else:
        result["message"] = (
            "Decision recorded. Broker execution remains disabled."
        )

    return result
