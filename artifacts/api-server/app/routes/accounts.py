"""Read-only account endpoints."""

from fastapi import APIRouter, HTTPException, status

from app.account_manager import account_manager
from app.connectors.tradelocker import TradeLockerConnector
from app.models.account import Account

router = APIRouter(prefix="/accounts", tags=["accounts"])
tradelocker = TradeLockerConnector()


@router.get("", response_model=list[Account])
async def list_accounts() -> list[Account]:
    """List configured account metadata."""

    return account_manager.list_accounts()


@router.get("/{nickname}", response_model=Account)
async def get_account(nickname: str) -> Account:
    """Retrieve one account by nickname."""

    account = account_manager.get_account(nickname)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account '{nickname}' was not found",
        )
    return account


@router.get("/{nickname}/connection-status")
async def get_connection_status(nickname: str) -> dict[str, object]:
    """Report safe TradeLocker configuration status without secret values."""

    account = account_manager.get_account(nickname)
    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account '{nickname}' was not found",
        )
    if account.platform.value == "TradeLocker":
        return {
            "nickname": account.nickname,
            "platform": account.platform,
            "environment": account.environment,
            "provider": tradelocker.provider,
            **tradelocker.configuration_status(),
        }
    return {
        "nickname": account.nickname,
        "platform": account.platform,
        "environment": account.environment,
        "provider": account.platform.value,
        "configured": False,
        "missing_configuration": [],
        "authentication_method": "not_configured",
        "google_sign_in_supported": False,
        "message": "No connector is configured for this account.",
    }