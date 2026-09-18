"""TradeLocker order-request preparation.

Builds a request that follows the documented TradeLocker order schema.
This module NEVER submits a broker request.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.services.execution import ExecutionPreview


class TradeLockerExecutionError(ValueError):
    """Raised when a safe TradeLocker request cannot be prepared."""


@dataclass(frozen=True)
class TradeLockerPreparedRequest:
    method: str
    path: str
    headers: dict[str, str]
    body: dict[str, Any]
    account: str
    execution_enabled: bool = False
    execution_status: str = "PREPARED_NOT_SENT"


def prepare_tradelocker_request(
    preview: ExecutionPreview,
    *,
    account_id: int,
    acc_num: str,
    qty: float,
    route_id: int,
    tradable_instrument_id: int,
) -> TradeLockerPreparedRequest:
    """Translate a validated preview into a documented dry-run request."""

    if preview.execution_enabled:
        raise TradeLockerExecutionError(
            "Expected a dry-run preview, but execution_enabled was True."
        )

    if preview.side not in {"LONG", "SHORT"}:
        raise TradeLockerExecutionError(
            f"Unsupported preview side: {preview.side}"
        )

    if account_id <= 0:
        raise TradeLockerExecutionError("account_id must be positive.")

    if not str(acc_num).strip():
        raise TradeLockerExecutionError("acc_num is required.")

    if qty <= 0:
        raise TradeLockerExecutionError("qty must be greater than zero.")

    if route_id <= 0:
        raise TradeLockerExecutionError("TRADE route_id must be positive.")

    if tradable_instrument_id <= 0:
        raise TradeLockerExecutionError(
            "tradable_instrument_id must be positive."
        )

    side = "buy" if preview.side == "LONG" else "sell"

    body = {
        "price": 0,
        "qty": qty,
        "routeId": route_id,
        "side": side,
        "stopLoss": preview.safe_loss,
        "stopLossType": "absolute",
        "takeProfit": preview.take_profit_1,
        "takeProfitType": "absolute",
        "tradableInstrumentId": tradable_instrument_id,
        "type": "market",
        "validity": "IOC",
        "strategyId": "AI-TRADING-BRIDGE",
    }

    return TradeLockerPreparedRequest(
        method="POST",
        path=f"/trade/accounts/{account_id}/orders",
        headers={
            "accNum": str(acc_num),
            "content-type": "application/json",
        },
        body=body,
        account=preview.account,
    )
