"""Read-only broker connector contracts."""

from abc import ABC, abstractmethod
from typing import Any

class ReadOnlyConnector(ABC):
    """Common contract for broker integrations.

    This interface intentionally contains observation-only operations. There
    are no create, update, cancel, close, or execute methods by design.
    """

    provider: str

    @abstractmethod
    async def authenticate(self) -> dict[str, Any]:
        """Authenticate using the broker's documented read-only API flow."""

    @abstractmethod
    async def get_accounts(self) -> list[dict[str, Any]]:
        """Return broker accounts without changing broker state."""

    @abstractmethod
    async def get_available_instruments(
        self, account_id: int, acc_num: str
    ) -> dict[str, Any]:
        """Return instruments available to an account."""

    @abstractmethod
    async def get_account_state(
        self, account_id: int, acc_num: str
    ) -> dict[str, Any]:
        """Return current account state."""

    @abstractmethod
    async def get_open_positions(
        self, account_id: int, acc_num: str
    ) -> dict[str, Any]:
        """Return currently open positions."""

    @abstractmethod
    async def get_pending_orders(
        self, account_id: int, acc_num: str
    ) -> dict[str, Any]:
        """Return non-final orders."""

    @abstractmethod
    async def get_historical_candles(
        self,
        account_id: int,
        acc_num: str,
        tradable_instrument_id: int,
        route_id: int,
        resolution: str,
        from_timestamp: int,
        to_timestamp: int,
    ) -> dict[str, Any]:
        """Return historical candles for an instrument."""
