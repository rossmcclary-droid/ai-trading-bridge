import importlib
import os
import sys
from pathlib import Path

os.environ["TRADING_BRIDGE_DB"] = "/tmp/radar-compat-test.db"
Path(os.environ["TRADING_BRIDGE_DB"]).unlink(missing_ok=True)
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
server = importlib.import_module("server")


def clear_radar_cache():
    server._RADAR_OBSERVATION_CACHE.clear()


def test_simulated_account_is_explicitly_unavailable():
    clear_radar_cache()
    result = server.radar_observation("XAUUSD", "sim-tl-784215")
    assert result["quality"]["status"] == "UNAVAILABLE"
    assert all(value is None for value in result["raw"].values())
    assert result["session"]["dayBoundary"] is None


def test_history_projection_never_synthesizes_quotes(monkeypatch):
    clear_radar_cache()
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
    assert result["quality"]["status"] == "MISSING"


def test_completed_history_lookbacks_are_deterministic(monkeypatch):
    account = {"id": "real", "platform": "TradeLocker", "connection_id": "c"}
    instrument = {"symbol": "XAUUSD"}
    now = 2_000_000_000
    rows = [{"time": now - (300-i)*60, "o": 100+i, "h": 101+i, "l": 99+i, "c": 100.5+i, "v": 1} for i in range(300)]
    class FakeBroker:
        def candles(self, *args, **kwargs): return rows
    monkeypatch.setattr(server, "broker_for", lambda _: FakeBroker())
    monkeypatch.setattr(server.time, "time", lambda: now)
    out = server._radar_history_observation(account, instrument)
    assert out["price1HourAgo"] == 339.5
    assert out["price4HoursAgo"] == 159.5


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


def test_tradelocker_quote_uses_info_route_and_preserves_raw_response():
    class Response:
        status_code = 200
        def raise_for_status(self): pass
        def json(self): return {"d": {"opaque": [1, 2, 3]}}
    class Client:
        def __init__(self): self.call = None
        def get(self, url, params=None, headers=None):
            self.call = (url, params, headers)
            return Response()
    broker = object.__new__(server.TradeLockerBroker)
    broker.base = "https://example.invalid/backend-api"
    broker.client = Client()
    broker.token = "test-token"
    broker.creds = {}
    account = {"acc_num": "123"}
    instrument = {"infoRouteId": 44, "tradableInstrumentId": 55, "tradeRouteId": 99}
    out = broker.quote_raw(account, instrument)
    assert out == {"d": {"opaque": [1, 2, 3]}}
    _, params, headers = broker.client.call
    assert params == {"routeId": 44, "tradableInstrumentId": 55}
    assert params["routeId"] != instrument["tradeRouteId"]
    assert headers["accNum"] == "123"


def test_quote_projection_preserves_evidence_without_guessing_bid_ask(monkeypatch):
    clear_radar_cache()
    account = {"id": "real", "platform": "TradeLocker", "connection_id": "c"}
    instrument = {"symbol": "XAUUSD"}
    class FakeBroker:
        def quote_raw(self, *args): return {"mysteryBidLike": 2400, "mysteryAskLike": 2401}
        def candles(self, *args, **kwargs): return []
    monkeypatch.setattr(server, "broker_for", lambda _: FakeBroker())
    monkeypatch.setattr(server, "all_accounts", lambda: [account])
    monkeypatch.setattr(server, "instruments_for", lambda _: [instrument])
    result = server.radar_observation("XAUUSD", "real")
    assert result["quoteEvidence"]["rawResponse"] == {"mysteryBidLike": 2400, "mysteryAskLike": 2401}
    assert result["quoteEvidence"]["status"] == "QUESTIONABLE"
    assert result["raw"]["bid"] is None
    assert result["raw"]["ask"] is None


def test_bridge_ui_defers_app_script_until_connection_form_exists():
    html = Path("index.html").read_text()
    assert '<script src="app.js" defer></script>' in html
    assert 'id="tlConnectForm"' in html


def test_validation_ui_cache_version_bumped_for_form_fix():
    sw = Path("service-worker.js").read_text()
    assert "ai-trading-bridge-v13-radar-validation-1" in sw


def test_connection_form_has_no_native_get_fallback():
    html = Path("index.html").read_text()
    start = html.index('<form id="tlConnectForm"')
    end = html.index('</form>', start)
    form = html[start:end]
    assert 'method="get"' not in form.lower()
    assert 'action=' not in form.lower()


def test_connection_javascript_posts_credentials_in_json_body_only():
    js = Path("app.js").read_text()
    marker = "fetch('/api/connect/tradelocker'"
    start = js.index(marker)
    snippet = js[start:start + 350]
    assert "method:'POST'" in snippet
    assert "body:JSON.stringify(f)" in snippet
    assert "?" not in snippet.split("fetch(", 1)[1].split(",", 1)[0]


def test_verified_quote_fields_map_ap_to_ask_and_bp_to_bid(monkeypatch):
    clear_radar_cache()
    account = {"id":"real","platform":"TradeLocker","connection_id":"c"}
    instrument = {"symbol":"XAUUSD"}
    class FakeBroker:
        def quote_raw(self,*args): return {"s":"ok","d":{"ap":4368.23,"bp":4368.02,"as":100,"bs":100}}
        def candles(self,*args,**kwargs): return []
    monkeypatch.setattr(server,"broker_for",lambda _:FakeBroker())
    monkeypatch.setattr(server,"all_accounts",lambda:[account])
    monkeypatch.setattr(server,"instruments_for",lambda _:[instrument])
    out=server.radar_observation("XAUUSD","real")
    assert out["raw"]["ask"] == 4368.23
    assert out["raw"]["bid"] == 4368.02
    assert out["quoteEvidence"]["status"] == "CURRENT"

def test_authenticated_history_bar_details_normalizes_milliseconds():
    class Response:
        status_code = 200
        def raise_for_status(self): pass
        def json(self): return {"s":"ok","d":{"barDetails":[{"t":1789614000000,"o":1,"h":2,"l":0.5,"c":1.5,"v":3}]}}
    class Client:
        def get(self,*args,**kwargs): return Response()
    b=object.__new__(server.TradeLockerBroker); b.base="https://example.invalid"; b.client=Client(); b.token="test"; b.creds={}
    rows=b.candles({"acc_num":"1"},{"infoRouteId":2,"tradableInstrumentId":3},"1H",8)
    assert rows[0]["time"] == 1789614000
    assert rows[0]["c"] == 1.5

def test_instrument_cache_avoids_repeated_broker_discovery(monkeypatch):
    account={"id":"cache-test","connection_id":"cache-conn"}
    calls=[]
    class B:
        def instruments(self,a): calls.append(1); return [{"symbol":"XAUUSD"}]
    server._INSTRUMENT_CACHE.pop(account["id"],None)
    monkeypatch.setattr(server,"broker_for",lambda _:B())
    assert server.instruments_for(account)==[{"symbol":"XAUUSD"}]
    assert server.instruments_for(account)==[{"symbol":"XAUUSD"}]
    assert len(calls)==1
    server._INSTRUMENT_CACHE.pop(account["id"],None)

def test_radar_observation_cache_avoids_repeat_broker_reads(monkeypatch):
    account={"id":"real","platform":"TradeLocker","connection_id":"c"}; instrument={"symbol":"XAUUSD"}
    class B:
        quotes=0; histories=0
        def quote_raw(self,*args): self.quotes+=1; return {"d":{"ap":2.0,"bp":1.0}}
        def candles(self,*args,**kwargs):
            self.histories+=1; now=int(server.time.time())
            return [{"time":now-(300-i)*60,"o":1,"h":2,"l":0.5,"c":1.5,"v":1} for i in range(300)]
    b=B(); server._RADAR_OBSERVATION_CACHE.clear()
    monkeypatch.setattr(server,"all_accounts",lambda:[account]); monkeypatch.setattr(server,"instruments_for",lambda _:[instrument]); monkeypatch.setattr(server,"broker_for",lambda _:b)
    first=server.radar_observation("XAUUSD","real"); second=server.radar_observation("XAUUSD","real")
    assert first == second
    assert b.quotes == 1 and b.histories == 1
    assert server.RADAR_OBSERVATION_CACHE_SECONDS == 300.0

def test_info_get_rate_limit_retry_is_bounded(monkeypatch):
    class R: status_code=429
    class C:
        calls=0
        def get(self,*args,**kwargs): self.calls+=1; return R()
    sleeps=[]; monkeypatch.setattr(server.time,'sleep',lambda n:sleeps.append(n))
    b=object.__new__(server.TradeLockerBroker); b.client=C()
    out=b._info_get('https://example.invalid')
    assert out.status_code == 429 and b.client.calls == 3
    assert sleeps == [0.25,0.5]

def test_tradelocker_http_timeout_is_bounded(monkeypatch):
    seen={}
    class C:
        def __init__(self,timeout): seen['timeout']=timeout
        def post(self,*args,**kwargs): raise RuntimeError('stop before credentials')
    monkeypatch.setattr(server.httpx,'Client',C)
    try: server.TradeLockerBroker({'environment':'DEMO','email':'x','password':'y','server':'z'})
    except RuntimeError: pass
    assert seen['timeout'] == 8.0
