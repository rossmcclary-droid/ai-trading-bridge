"""Account models exposed by the read-only account manager."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class Platform(StrEnum):
    """Supported trading platforms."""

    TRADELOCKER = "TradeLocker"
    MATCH_TRADER = "Match-Trader"


class Environment(StrEnum):
    """Trading account environments."""

    DEMO = "Demo"
    LIVE = "Live"


class ConnectionStatus(StrEnum):
    """Connection state for a broker account."""

    NOT_CONNECTED = "not_connected"
    CONNECTED = "connected"


class Account(BaseModel):
    """Read-only account metadata.

    Credential fields are intentionally absent. Connection details will be
    added only through a dedicated secure integration flow in a later phase.
    """

    model_config = ConfigDict(frozen=True)

    internal_id: str
    nickname: str
    platform: Platform
    environment: Environment
    broker: str
    external_account_id: str | None = None
    external_account_number: str | None = None
    connection_status: ConnectionStatus