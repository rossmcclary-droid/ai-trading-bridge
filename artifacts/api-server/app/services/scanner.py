"""Read-only live market scanner service."""

import time
from typing import Any

from app.connectors.tradelocker import (
    TradeLockerConfig,
    TradeLockerConnector,
)


TIMEFRAMES = ("4H", "1H", "15M", "5M")


async def _history_with_retry(
    connector,
    *,
    attempts: int = 3,
    timing: dict[str, Any] | None = None,
    request_timing: dict[str, Any] | None = None,
    **kwargs,
):
    import asyncio

    last_error = None

    for attempt in range(attempts):
        if request_timing is not None:
            request_timing["attempts"] = request_timing.get("attempts", 0) + 1
            request_timing["retry_count"] = attempt
        try:
            _t=time.perf_counter()
            try:
                result=await connector.get_historical_candles(**kwargs)
            finally:
                if timing is not None: timing["history_network_ms"]=timing.get("history_network_ms",0.0)+(time.perf_counter()-_t)*1000.0
            return result
        except Exception as error:
            last_error = error

            if attempt == attempts - 1:
                raise

            _t=time.perf_counter()
        await asyncio.sleep(3 * (attempt + 1))
        if timing is not None: timing["history_delay_sleep_ms"]=timing.get("history_delay_sleep_ms",0.0)+(time.perf_counter()-_t)*1000.0

    raise last_error


class ScannerService:
    """Collect live market data without modifying broker state."""

    def __init__(self) -> None:
        self.connector = TradeLockerConnector(
            TradeLockerConfig.from_environment()
        )

    async def scan_symbol(
        self,
        *,
        symbol: str,
        account_id: int,
        acc_num: str,
    ) -> dict[str, Any]:

        await self.connector.authenticate()

        instruments_response = (
            await self.connector.get_available_instruments(
                account_id=account_id,
                acc_num=acc_num,
            )
        )

        instruments = (
            instruments_response.get("d", {}).get("instruments", [])
        )

        instrument = next(
            (
                item
                for item in instruments
                if str(item.get("name", "")).upper()
                == symbol.upper()
            ),
            None,
        )

        if instrument is None:
            raise ValueError(
                f"Instrument {symbol!r} was not found."
            )

        tradable_id = instrument.get("tradableInstrumentId")

        info_route = next(
            (
                route
                for route in instrument.get("routes", [])
                if route.get("type") == "INFO"
            ),
            None,
        )

        if info_route is None:
            raise ValueError(
                f"No INFO route found for {symbol}."
            )

        route_id = info_route["id"]

        now = int(time.time() * 1000)

        lookbacks = {
            "4H": 14 * 24 * 60 * 60 * 1000,
            "1H": 7 * 24 * 60 * 60 * 1000,
            "15M": 2 * 24 * 60 * 60 * 1000,
            "5M": 12 * 60 * 60 * 1000,
        }

        candles: dict[str, Any] = {}

        for timeframe in TIMEFRAMES:
            _processing_started=time.perf_counter()
            candles[timeframe] = (
                await self.connector.get_historical_candles(
                    account_id=account_id,
                    acc_num=acc_num,
                    tradable_instrument_id=tradable_id,
                    route_id=route_id,
                    resolution=timeframe,
                    from_timestamp=now - lookbacks[timeframe],
                    to_timestamp=now,
                )
            )

        return {
            "symbol": symbol.upper(),
            "account_id": account_id,
            "acc_num": acc_num,
            "tradable_instrument_id": tradable_id,
            "route_id": route_id,
            "timeframes": candles,
            "_patch002c_timing": _symbol_timing,
        }


    async def scan_symbols(
        self,
        *,
        symbols: list[str],
        account_id: int,
        acc_num: str,
        broker_crypto_only: bool = False,
        history_request_delay_seconds: float | None = None,
    timing: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Collect multi-timeframe data while respecting broker rate limits."""

        import asyncio

        if len(symbols) > 10:
            raise ValueError(
                "A scan may contain no more than 10 symbols."
            )

        await self.connector.authenticate()

        instruments_response = (
            await self.connector.get_available_instruments(
                account_id=account_id,
                acc_num=acc_num,
            )
        )

        instruments = (
            instruments_response.get("d", {}).get("instruments", [])
        )

        instrument_map = {
            str(item.get("name", "")).upper(): item
            for item in instruments
        }

        if broker_crypto_only:
            crypto_symbols = [
                str(item.get("name", "")).strip().upper()
                for item in instruments
                if isinstance(item, dict)
                and str(item.get("type", "")).upper() == "CRYPTO"
                and str(item.get("name", "")).strip()
            ]

            # Preserve broker order while removing duplicates.
            symbols = list(dict.fromkeys(crypto_symbols))[:10]

            if not symbols:
                raise ValueError(
                    "TradeLocker reported no CRYPTO instruments "
                    "for this account."
                )

        now = int(time.time() * 1000)

        lookbacks = {
            "4H": 14 * 24 * 60 * 60 * 1000,
            "1H": 7 * 24 * 60 * 60 * 1000,
            "15M": 2 * 24 * 60 * 60 * 1000,
            "5M": 12 * 60 * 60 * 1000,
        }

        results: dict[str, Any] = {}
        errors: dict[str, str] = {}

        history_semaphore = asyncio.Semaphore(3)

    async def _scan_symbol(symbol: str) -> None:
        async with history_semaphore:
                normalized = symbol.upper()

                try:
                    instrument = instrument_map.get(normalized)

                    if instrument is None:
                        raise ValueError(
                            f"Instrument {normalized!r} was not found."
                        )

                    tradable_id = instrument.get("tradableInstrumentId")

                    info_route = next(
                        (
                            route
                            for route in instrument.get("routes", [])
                            if route.get("type") == "INFO"
                        ),
                        None,
                    )

                    if info_route is None:
                        raise ValueError(
                            f"No INFO route found for {normalized}."
                        )

                    route_id = info_route["id"]
                    candles: dict[str, Any] = {}

                    for timeframe in TIMEFRAMES:
                        request_timing = {"timeframe": timeframe, "attempts": 0, "retry_count": 0, "history_network_ms": 0.0, "history_delay_sleep_ms": 0.0}
                        _request_started = time.perf_counter()
                        candles[timeframe] = (
                            await _history_with_retry(
                                self.connector,
                                account_id=account_id,
                                acc_num=acc_num,
                                tradable_instrument_id=tradable_id,
                                route_id=route_id,
                                resolution=timeframe,
                                from_timestamp=now - lookbacks[timeframe],
                                to_timestamp=now,
                                timing=timing,
                                request_timing=request_timing,
                            )
                        )
                        _request_ended = time.perf_counter()
                        request_timing.update(started_at_ms=round(_request_started * 1000.0, 3), ended_at_ms=round(_request_ended * 1000.0, 3), elapsed_ms=round((_request_ended - _request_started) * 1000.0, 3))
                        if timing is not None:
                            timing.setdefault("history_request_trace", []).append(request_timing)

            # Avoid bursting TradeLocker's history endpoint.
                        delay_seconds = (
                            history_request_delay_seconds
                            if history_request_delay_seconds is not None
                            else (2.0 if broker_crypto_only else 1.0)
                        )
                        delay_elapsed_ms = 0.0
                        if delay_seconds > 0:
                            delay_started = time.perf_counter()
                            await asyncio.sleep(delay_seconds)
                            delay_elapsed_ms = (time.perf_counter() - delay_started) * 1000.0
                    results[normalized] = {
                        "symbol": normalized,
                        "account_id": account_id,
                        "acc_num": acc_num,
                        "tradable_instrument_id": tradable_id,
                        "route_id": route_id,
                        "timeframes": candles,
                    }

                    symbol_timing = results[normalized].get("patch002c_timing")
                    if isinstance(symbol_timing, dict) and delay_elapsed_ms > 0:
                        symbol_timing["history_delay_sleep_ms"] = round(
                            float(symbol_timing.get("history_delay_sleep_ms", 0.0))
                            + delay_elapsed_ms,
                            3,
                        )
                        symbol_timing["history_success_delay_sleep_ms"] = round(
                            float(symbol_timing.get("history_success_delay_sleep_ms", 0.0))
                            + delay_elapsed_ms,
                            3,
                        )
            
                except Exception as error:
                    errors[normalized] = str(error)

                    # Give the broker extra recovery time after a failure.
                    await asyncio.sleep(1.0)

        await asyncio.gather(*(_scan_symbol(symbol) for symbol in symbols))

        return {
                "results": results,
                "errors": errors,
                "requested": len(symbols),
                "successful": len(results),
                "failed": len(errors),
            }
