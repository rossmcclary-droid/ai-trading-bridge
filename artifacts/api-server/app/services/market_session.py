"""Tradable-universe rules for Atlas scans."""

from datetime import datetime
from zoneinfo import ZoneInfo


NEW_YORK = ZoneInfo("America/New_York")

CRYPTO_SYMBOLS = [
    "BTCUSD",
]


def weekend_crypto_only(now: datetime | None = None) -> bool:
    """Return True during the normal non-crypto weekend closure.

    Window:
    Friday 4:30 PM New York time through Sunday 7:00 PM New York time.

    This is a scheduling fallback, not a broker market-status guarantee.
    """

    current = now or datetime.now(NEW_YORK)

    if current.tzinfo is None:
        current = current.replace(tzinfo=NEW_YORK)
    else:
        current = current.astimezone(NEW_YORK)

    weekday = current.weekday()
    minutes = current.hour * 60 + current.minute

    friday_cutoff = 16 * 60 + 30
    sunday_reopen = 19 * 60

    if weekday == 4:
        return minutes >= friday_cutoff

    if weekday == 5:
        return True

    if weekday == 6:
        return minutes < sunday_reopen

    return False


def default_tradable_symbols(
    normal_symbols: list[str],
    now: datetime | None = None,
) -> list[str]:
    """Return the default universe appropriate for the current session."""

    if weekend_crypto_only(now):
        allowed = set(CRYPTO_SYMBOLS)
        return [
            symbol
            for symbol in normal_symbols
            if symbol in allowed
        ]

    return list(normal_symbols)
