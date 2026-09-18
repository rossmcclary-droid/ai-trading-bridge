"""Application configuration and safety policy."""

from enum import StrEnum


class TradingMode(StrEnum):
    """Supported operating modes."""

    READ_ONLY = "read-only"


SERVICE_NAME = "AI Trading Bridge"
MODE = TradingMode.READ_ONLY

# Keep this allowlist explicit. Future connector methods must be added here
# only when they are read operations; execution operations have no interface.
READ_OPERATIONS = frozenset(
    {
        "get_account",
        "get_balances",
        "get_positions",
        "get_orders",
        "get_market_data",
    }
)