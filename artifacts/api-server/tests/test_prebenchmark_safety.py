import ast
import asyncio
from pathlib import Path
import unittest
from unittest.mock import AsyncMock, patch

from app.services.rate_limit import RateLimitError, gather_rate_limit_aware, is_rate_limited
from app.services.scanner import ScannerService, TIMEFRAMES, _history_with_retry
from app.services.export_timings import build_patch002d


class FakeConnector:
    def __init__(self, symbols):
        self.symbols = symbols
        self.active = 0
        self.maximum_active = 0
        self.calls = []

    async def authenticate(self):
        return None

    async def get_available_instruments(self, **kwargs):
        return {
            "d": {
                "instruments": [
                    {
                        "name": symbol,
                        "tradableInstrumentId": index,
                        "routes": [{"type": "INFO", "id": index + 100}],
                    }
                    for index, symbol in enumerate(self.symbols)
                ]
            }
        }

    async def get_historical_candles(self, **kwargs):
        self.active += 1
        self.maximum_active = max(self.maximum_active, self.active)
        self.calls.append((kwargs["tradable_instrument_id"], kwargs["resolution"]))
        try:
            await asyncio.sleep(0.005)
            return {"d": {"barDetails": []}}
        finally:
            self.active -= 1


def load_export_retry():
    source_path = Path(__file__).parents[1] / "app" / "routes" / "exports.py"
    module = ast.parse(source_path.read_text())
    function = next(
        node
        for node in module.body
        if isinstance(node, ast.AsyncFunctionDef) and node.name == "_export_retry"
    )
    namespace = {
        "asyncio": asyncio,
        "RateLimitError": RateLimitError,
        "is_rate_limited": is_rate_limited,
    }
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(source_path), "exec"), namespace)
    return namespace["_export_retry"]


def load_exports_ast():
    source_path = Path(__file__).parents[1] / "app" / "routes" / "exports.py"
    return ast.parse(source_path.read_text())


class ScannerSafetyTests(unittest.IsolatedAsyncioTestCase):
    def test_rate_limit_detection_accepts_structured_provider_signals(self):
        class ProviderError(RuntimeError):
            pass

        class Response:
            status_code = "429"

        direct = ProviderError("opaque provider failure")
        direct.status_code = 429
        nested = ProviderError("opaque provider failure")
        nested.response = Response()
        coded = ProviderError("opaque provider failure")
        coded.error_category = "rate_limited"

        self.assertTrue(is_rate_limited(direct))
        self.assertTrue(is_rate_limited(nested))
        self.assertTrue(is_rate_limited(coded))

    def test_rate_limit_detection_rejects_incidental_text_and_4290(self):
        self.assertFalse(is_rate_limited(RuntimeError("HTTP 4290 upstream")))
        self.assertFalse(
            is_rate_limited(RuntimeError("rate_limited must be false"))
        )
        self.assertFalse(is_rate_limited(RuntimeError("result code=1429")))
        self.assertTrue(is_rate_limited(RuntimeError("provider returned HTTP 429.")))

    def test_rate_limit_detection_accepts_sdk_exception_class_name(self):
        ProviderRateLimitError = type("RateLimitError", (RuntimeError,), {})
        self.assertTrue(is_rate_limited(ProviderRateLimitError("opaque")))

    def test_quote_discovery_uses_fail_fast_batch_at_concurrency_six(self):
        module = load_exports_ast()
        calls = [
            node
            for node in ast.walk(module)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "gather_rate_limit_aware"
        ]
        quote_call = next(
            call
            for call in calls
            if any(
                keyword.arg == "concurrency"
                and isinstance(keyword.value, ast.Constant)
                and keyword.value.value == 6
                for keyword in call.keywords
            )
        )
        self.assertIsNotNone(quote_call)

    async def test_rate_limit_batch_stops_queued_work_and_settles_peers(self):
        started = []
        cancelled = []
        peers_started = asyncio.Event()

        async def worker(item):
            started.append(item)
            if item == 0:
                await peers_started.wait()
                raise RuntimeError("HTTP 429")
            if item in (1, 2):
                if len(started) >= 3:
                    peers_started.set()
                try:
                    await asyncio.Event().wait()
                finally:
                    cancelled.append(item)
            return item

        with self.assertRaises(RateLimitError):
            await gather_rate_limit_aware(range(7), worker, concurrency=3)

        self.assertEqual(set(started), {0, 1, 2})
        self.assertEqual(set(cancelled), {1, 2})

    async def test_scan_symbols_returns_batch_and_caps_symbol_concurrency_at_three(self):
        symbols = [f"SYM{index}" for index in range(6)]
        connector = FakeConnector(symbols)
        scanner = ScannerService.__new__(ScannerService)
        scanner.connector = connector

        batch = await scanner.scan_symbols(
            symbols=symbols,
            account_id=1,
            acc_num="A",
            history_request_delay_seconds=0,
        )

        self.assertEqual(batch["successful"], 6)
        self.assertEqual(batch["failed"], 0)
        self.assertEqual(set(batch["results"]), set(symbols))
        self.assertEqual(connector.maximum_active, 3)
        for index in range(6):
            per_symbol = [tf for instrument, tf in connector.calls if instrument == index]
            self.assertEqual(per_symbol, list(TIMEFRAMES))

    async def test_scan_symbol_has_no_undefined_timing_name(self):
        connector = FakeConnector(["BTCUSD"])
        scanner = ScannerService.__new__(ScannerService)
        scanner.connector = connector

        result = await scanner.scan_symbol(symbol="BTCUSD", account_id=1, acc_num="A")

        self.assertEqual(result["symbol"], "BTCUSD")
        self.assertEqual(list(result["timeframes"]), list(TIMEFRAMES))

    async def test_history_429_is_not_retried(self):
        connector = unittest.mock.Mock()
        connector.get_historical_candles = AsyncMock(side_effect=RuntimeError("HTTP 429 rate_limited"))
        with patch("asyncio.sleep", new=AsyncMock()) as sleep:
            with self.assertRaises(RuntimeError):
                await _history_with_retry(connector, attempts=3)
        self.assertEqual(connector.get_historical_candles.await_count, 1)
        sleep.assert_not_awaited()

    async def test_history_non_429_retry_remains_bounded(self):
        connector = unittest.mock.Mock()
        connector.get_historical_candles = AsyncMock(side_effect=RuntimeError("temporary"))
        with patch("asyncio.sleep", new=AsyncMock()) as sleep:
            with self.assertRaises(RuntimeError):
                await _history_with_retry(connector, attempts=3)
        self.assertEqual(connector.get_historical_candles.await_count, 3)
        self.assertEqual(sleep.await_count, 2)

    async def test_scanner_429_fails_batch_and_does_not_return_partial_errors(self):
        symbols = [f"SYM{index}" for index in range(6)]
        connector = FakeConnector(symbols)
        connector.get_historical_candles = AsyncMock(
            side_effect=RuntimeError("HTTP 429 rate_limited")
        )
        scanner = ScannerService.__new__(ScannerService)
        scanner.connector = connector

        with self.assertRaises(RateLimitError):
            await scanner.scan_symbols(
                symbols=symbols,
                account_id=1,
                acc_num="A",
                history_request_delay_seconds=0,
            )
        self.assertEqual(connector.get_historical_candles.await_count, 1)

    async def test_scanner_reports_nonzero_network_and_success_delay_timings(self):
        connector = FakeConnector(["BTCUSD"])
        scanner = ScannerService.__new__(ScannerService)
        scanner.connector = connector
        timing = {}

        batch = await scanner.scan_symbols(
            symbols=["BTCUSD"],
            account_id=1,
            acc_num="A",
            history_request_delay_seconds=0.001,
            timing=timing,
        )

        per_symbol = batch["results"]["BTCUSD"]["_patch002c_timing"]
        self.assertGreater(per_symbol["history_network_ms"], 0)
        self.assertGreater(per_symbol["history_success_delay_sleep_ms"], 0)
        self.assertGreater(timing["history_network_ms"], 0)
        self.assertGreater(timing["history_success_delay_sleep_ms"], 0)

        diagnostics = build_patch002d(
            wall_created_to_ready_ms=100,
            history={
                **timing,
                "history_processing_ms": None,
            },
        )
        self.assertGreater(diagnostics["history"]["history_network_ms"], 0)
        self.assertGreater(
            diagnostics["history"]["history_success_delay_sleep_ms"], 0
        )
        self.assertIsNone(diagnostics["history"]["history_processing_ms"])
        self.assertTrue(diagnostics["history"]["history_processing_unmeasured"])

    async def test_failed_symbol_timing_and_terminal_trace_are_preserved_once(self):
        class FailingConnector(FakeConnector):
            async def get_historical_candles(self, **kwargs):
                self.calls.append(
                    (kwargs["tradable_instrument_id"], kwargs["resolution"])
                )
                await original_sleep(0.002)
                raise RuntimeError("temporary provider failure")

        async def short_sleep(_seconds):
            await original_sleep(0.001)

        original_sleep = asyncio.sleep
        connector = FailingConnector(["BTCUSD"])
        scanner = ScannerService.__new__(ScannerService)
        scanner.connector = connector
        timing = {}

        with patch("asyncio.sleep", new=short_sleep):
            batch = await scanner.scan_symbols(
                symbols=["BTCUSD"],
                account_id=1,
                acc_num="A",
                history_request_delay_seconds=0,
                timing=timing,
            )

        self.assertEqual(batch["successful"], 0)
        self.assertEqual(batch["failed"], 1)
        self.assertIn("BTCUSD", batch["errors"])
        self.assertGreater(timing["history_network_ms"], 0)
        self.assertGreater(timing["history_delay_sleep_ms"], 0)
        self.assertEqual(timing["history_success_delay_sleep_ms"], 0)
        self.assertEqual(len(timing["history_request_trace"]), 1)
        terminal = timing["history_request_trace"][0]
        self.assertEqual(terminal["outcome"], "failure")
        self.assertEqual(terminal["attempts"], 3)
        self.assertEqual(terminal["retry_count"], 2)
        self.assertAlmostEqual(
            terminal["history_network_ms"],
            timing["history_network_ms"],
            places=6,
        )
        self.assertAlmostEqual(
            terminal["history_delay_sleep_ms"],
            timing["history_delay_sleep_ms"],
            places=6,
        )

    async def test_export_429_is_not_retried(self):
        export_retry = load_export_retry()
        call = AsyncMock(side_effect=RuntimeError("rate_limited"))
        with patch("asyncio.sleep", new=AsyncMock()):
            with self.assertRaises(RuntimeError):
                await export_retry(call)
        self.assertEqual(call.await_count, 1)

    async def test_export_non_429_retry_remains_bounded(self):
        export_retry = load_export_retry()
        call = AsyncMock(side_effect=RuntimeError("temporary"))
        with patch("asyncio.sleep", new=AsyncMock()):
            with self.assertRaises(RuntimeError):
                await export_retry(call)
        self.assertEqual(call.await_count, 3)


if __name__ == "__main__":
    unittest.main()
