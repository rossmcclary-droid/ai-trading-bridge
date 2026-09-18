"""TradeLocker account-state field mapping.

Maps TradeLocker's positional account-state response using /trade/config.
Read-only utility.
"""

from __future__ import annotations

from typing import Any


class TradeLockerAccountStateError(ValueError):
    """Raised when account-state values cannot be mapped safely."""


def _find_field_order(config: Any) -> list[str]:
    matches: list[list[str]] = []

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for child in value.values():
                if (
                    isinstance(child, list)
                    and child
                    and all(
                        isinstance(item, dict) and "id" in item
                        for item in child
                    )
                ):
                    ids = [str(item.get("id")) for item in child]

                    if (
                        "balance" in ids
                        and "availableFunds" in ids
                    ):
                        matches.append(ids)

                walk(child)

        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(config)

    if not matches:
        raise TradeLockerAccountStateError(
            "Could not locate TradeLocker account-state field ordering."
        )

    return matches[0]


def _find_state_rows(
    state: Any,
    expected_length: int,
) -> list[list[Any]]:
    rows: list[list[Any]] = []

    def walk(value: Any) -> None:
        if isinstance(value, list):
            if (
                len(value) == expected_length
                and not any(
                    isinstance(item, (dict, list))
                    for item in value
                )
            ):
                rows.append(value)

            for child in value:
                walk(child)

        elif isinstance(value, dict):
            for child in value.values():
                walk(child)

    walk(state)
    return rows


def map_tradelocker_account_state(
    config: Any,
    state: Any,
) -> dict[str, Any]:
    """Map positional state values to TradeLocker field IDs."""

    fields = _find_field_order(config)
    rows = _find_state_rows(state, len(fields))

    if not rows:
        raise TradeLockerAccountStateError(
            f"No account-state row matched {len(fields)} configured fields."
        )

    # For current single-account requests we expect one matching state row.
    # Multiple rows are treated as ambiguous rather than guessed.
    if len(rows) > 1:
        unique_rows = []

        for row in rows:
            if row not in unique_rows:
                unique_rows.append(row)

        rows = unique_rows

    if len(rows) != 1:
        raise TradeLockerAccountStateError(
            f"Expected one account-state row, found {len(rows)}."
        )

    return dict(zip(fields, rows[0]))
