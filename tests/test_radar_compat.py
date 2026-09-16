import importlib
import os
import sys
from pathlib import Path

os.environ["TRADING_BRIDGE_DB"] = "/tmp/radar-compat-test.db"
Path(os.environ["TRADING_BRIDGE_DB"]).unlink(missing_ok=True)
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
server = importlib.import_module("server")


def test_simulated_account_is_explicitly_unavailable():
    result = server.radar_observation("XAUUSD", "sim-tl-784215")
    assert result["quality"]["status"] == "UNAVAILABLE"
    assert all(value is None for value in result["raw"].values())
    assert result["session"]["dayBoundary"] is None


def test_history_projection_never_synthesizes_quotes(monkeypatch):
    account = {"id": "real", "platform": "TradeLocker", "connection_id": "c"}
    instrument = {"symbol": "XAUUSD"}
    class FakeBroker:
        def candles(self, account, instrument, tf, count):
            now = int(server.time.time())
            return [{"time": now - 7200 + i * 3600, "o": 10+i, "h": 11+i, "l": 9+i, "c": 10.5+i, "v": 1} for i in range(2)]
    monkeypatch.setattr(server, "broker_for", lambda _: FakeBroker())
    monkeypatch.setattr(server, "all_accounts", lambda: [account])
    monkeypatch.setattr(server, "instruments_for", lambda _: [instrument])
    result = server.radar_observation("XAUUSD", "real")
    assert result["raw"]["bid"] is None
    assert result["raw"]["ask"] is None
    assert result["raw"]["currentDayHigh"] is None
    assert result["raw"]["previousDayClose"] is None
    assert result["quality"]["status"] == "QUESTIONABLE"


def test_completed_history_lookbacks_are_deterministic(monkeypatch):
    account = {"id": "real", "platform": "TradeLocker", "connection_id": "c"}
    instrument = {"symbol": "XAUUSD"}
    now = 2_000_000_000
    rows = [{"time": now - (6-i)*3600, "o": 100+i, "h": 101+i, "l": 99+i, "c": 100.5+i, "v": 1} for i in range(6)]
    class FakeBroker:
        def candles(self, *args, **kwargs): return rows
    monkeypatch.setattr(server, "broker_for", lambda _: FakeBroker())
    monkeypatch.setattr(server.time, "time", lambda: now)
    out = server._radar_history_observation(account, instrument)
    assert out["price1HourAgo"] == 105.5
    assert out["price4HoursAgo"] == 102.5


def test_radar_routes_are_get_only():
    routes = {(r.path, tuple(sorted(r.methods))) for r in server.app.routes if getattr(r, "methods", None)}
    assert ("/api/radar/v0/instruments", ("GET",)) in routes
    assert ("/api/radar/v0/observations", ("GET",)) in routes
    assert not any(path.startswith("/api/radar/") and methods != ("GET",) for path, methods in routes)


def test_radar_payload_contains_no_credential_fields():
    result = server.radar_observation("XAUUSD", "sim-tl-784215")
    text = str(result).lower()
    for forbidden in ("password", "access_token", "authorization", "developer_api_key", "secret_blob"):
        assert forbidden not in text
