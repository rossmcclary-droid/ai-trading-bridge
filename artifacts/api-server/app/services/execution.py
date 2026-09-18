"""Dry-run trade execution service.

Builds and validates broker order payloads without submitting them.
Live broker execution remains disabled.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class ExecutionValidationError(ValueError):
    """Raised when an approved trade is not safe to prepare."""


@dataclass(frozen=True)
class ExecutionPreview:
    instrument: str
    side: str
    entry: float
    safe_loss: float
    take_profit_1: float
    take_profit_2: float
    take_profit_3: float
    account: str
    scope: str
    broker_payload: dict[str, Any]
    execution_enabled: bool = False
    execution_status: str = "DRY_RUN_ONLY"


def build_execution_preview(
    *,
    instrument: str,
    direction: str,
    entry: float,
    safe_loss: float,
    take_profit_1: float,
    take_profit_2: float,
    take_profit_3: float | None = None,
    account: str,
    approved: bool,
    all_accounts: bool = False,
) -> ExecutionPreview:
    """Validate an approved trade and build a non-executable payload."""

    if not approved:
        raise ExecutionValidationError(
            "Trade has not received explicit approval."
        )

    normalized_direction = direction.upper()

    if take_profit_3 is None:
        take_profit_3 = (take_profit_1 + take_profit_2) / 2

    if normalized_direction not in {"LONG", "SHORT"}:
        raise ExecutionValidationError(
            f"Unsupported direction: {direction}"
        )

    if (
        entry <= 0
        or safe_loss <= 0
        or take_profit_1 <= 0
        or take_profit_2 <= 0
        or take_profit_3 <= 0
    ):
        raise ExecutionValidationError(
            "Entry, stop, and targets must all be positive."
        )

    if normalized_direction == "LONG":
        if not safe_loss < entry:
            raise ExecutionValidationError(
                "LONG safe loss must be below entry."
            )
        if not (
            take_profit_1 > entry
            and take_profit_3 >= take_profit_1
            and take_profit_2 >= take_profit_3
        ):
            raise ExecutionValidationError(
                "LONG targets must be above entry and ordered TP1 <= TP3 <= TP2."
            )

    if normalized_direction == "SHORT":
        if not safe_loss > entry:
            raise ExecutionValidationError(
                "SHORT safe loss must be above entry."
            )
        if not (
            take_profit_1 < entry
            and take_profit_3 <= take_profit_1
            and take_profit_2 <= take_profit_3
        ):
            raise ExecutionValidationError(
                "SHORT targets must be below entry and ordered TP1 >= TP3 >= TP2."
            )

    broker_payload = {
        "instrument": instrument,
        "side": "buy" if normalized_direction == "LONG" else "sell",
        "orderType": "market",
        "entryReference": entry,
        "stopLoss": safe_loss,
        "takeProfit1": take_profit_1,
        "takeProfit2": take_profit_2,
        "takeProfit3Bridge": take_profit_3,
        "account": account,
        "scope": "all_connected_accounts" if all_accounts else "single_account",
    }

    return ExecutionPreview(
        instrument=instrument,
        side=normalized_direction,
        entry=entry,
        safe_loss=safe_loss,
        take_profit_1=take_profit_1,
        take_profit_2=take_profit_2,
        take_profit_3=take_profit_3,
        account=account,
        scope=broker_payload["scope"],
        broker_payload=broker_payload,
    )
