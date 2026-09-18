"""Account-aware position sizing.

Calculates broker-valid quantity from:
- account balance
- requested risk percentage
- entry/stop distance
- instrument lot size
- broker lot step/minimum

Sizing always rounds DOWN. No broker requests occur here.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_FLOOR


MAX_RISK_PERCENT = 1.0


class RiskSizingError(ValueError):
    """Raised when a position cannot be sized safely."""


@dataclass(frozen=True)
class PositionSizeResult:
    balance: float
    risk_percent: float
    risk_budget: float
    stop_distance: float
    lot_size: float
    raw_quantity: float
    quantity: float
    lot_step: float
    min_lot: float
    estimated_stop_risk: float


def _round_down_to_step(
    value: float,
    step: float,
) -> float:
    if step <= 0:
        raise RiskSizingError("lot_step must be greater than zero.")

    d_value = Decimal(str(value))
    d_step = Decimal(str(step))

    units = (d_value / d_step).to_integral_value(
        rounding=ROUND_FLOOR
    )

    return float(units * d_step)


def calculate_position_size(
    *,
    balance: float,
    risk_percent: float,
    entry: float,
    safe_loss: float,
    lot_size: float,
    lot_step: float,
    min_lot: float,
    available_funds: float | None = None,
) -> PositionSizeResult:
    """Return a broker-valid quantity without exceeding risk budget."""

    if balance <= 0:
        raise RiskSizingError("Account balance must be positive.")

    if not (0 < risk_percent <= MAX_RISK_PERCENT):
        raise RiskSizingError(
            f"risk_percent must be greater than 0 and no more than "
            f"{MAX_RISK_PERCENT}%."
        )

    if entry <= 0 or safe_loss <= 0:
        raise RiskSizingError(
            "Entry and safe loss must be positive."
        )

    if lot_size <= 0:
        raise RiskSizingError("lot_size must be positive.")

    if min_lot <= 0:
        raise RiskSizingError("min_lot must be positive.")

    if available_funds is not None and available_funds <= 0:
        raise RiskSizingError(
            "No available funds are currently available for trading."
        )

    stop_distance = abs(entry - safe_loss)

    if stop_distance <= 0:
        raise RiskSizingError(
            "Entry and safe loss cannot be identical."
        )

    risk_budget = balance * (risk_percent / 100.0)

    # For an instrument quoted in account currency:
    #
    # stop risk = price distance × units represented by one lot × lots
    #
    # XAUUSD example:
    # lotSize=100, so a $1 move = $100 per 1.00 lot.
    risk_per_full_lot = stop_distance * lot_size

    if risk_per_full_lot <= 0:
        raise RiskSizingError(
            "Calculated risk per full lot is invalid."
        )

    raw_quantity = risk_budget / risk_per_full_lot

    quantity = _round_down_to_step(
        raw_quantity,
        lot_step,
    )

    if quantity < min_lot:
        raise RiskSizingError(
            "Calculated quantity is below the broker minimum lot size."
        )

    estimated_stop_risk = (
        stop_distance
        * lot_size
        * quantity
    )

    # Rounding must never cause risk to exceed the requested budget.
    if estimated_stop_risk > risk_budget + 1e-9:
        raise RiskSizingError(
            "Rounded quantity exceeds the requested risk budget."
        )

    return PositionSizeResult(
        balance=balance,
        risk_percent=risk_percent,
        risk_budget=round(risk_budget, 2),
        stop_distance=stop_distance,
        lot_size=lot_size,
        raw_quantity=raw_quantity,
        quantity=quantity,
        lot_step=lot_step,
        min_lot=min_lot,
        estimated_stop_risk=round(estimated_stop_risk, 2),
    )
