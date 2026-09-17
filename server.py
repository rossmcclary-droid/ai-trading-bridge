from __future__ import annotations

import base64
import io
import json
import math
import os
import random
import sqlite3
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol

import httpx
from cryptography.fernet import Fernet, InvalidToken
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
DB_PATH = Path(os.getenv("TRADING_BRIDGE_DB", ROOT / "trading_bridge.db"))
APP_SECRET = os.getenv("TRADING_BRIDGE_SECRET")
EXECUTION_ENABLED = os.getenv("TRADING_EXECUTION_ENABLED", "false").lower() == "true"
LIVE_EXECUTION_ENABLED = os.getenv("TRADING_LIVE_EXECUTION_ENABLED", "false").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-terra").strip() or "gpt-5.6-terra"
STRATEGY_FILE = ROOT / "strategy_bootstrap.json"
TRUSTED_STRATEGY_SOURCES = {"CHATGPT_STRATEGY", "BOOTSTRAPPED_CHATGPT_STRATEGY"}


def _fernet() -> Fernet:
    # Accept either a valid Fernet key or any high-entropy hosting secret.
    # Arbitrary secrets are deterministically converted into a Fernet-compatible key.
    if APP_SECRET:
        try:
            return Fernet(APP_SECRET.encode())
        except Exception:
            derived = base64.urlsafe_b64encode(__import__("hashlib").sha256(APP_SECRET.encode()).digest())
            return Fernet(derived)
    seed = base64.urlsafe_b64encode(__import__("hashlib").sha256(b"local-trading-bridge-change-me").digest())
    return Fernet(seed)

FERNET = _fernet()
app = FastAPI(title="AI Trading Bridge", version="1.3.0")



def load_strategy_bootstrap() -> dict[str, Any]:
    try:
        return json.loads(STRATEGY_FILE.read_text())
    except Exception as e:
        raise RuntimeError(f"Could not load strategy bootstrap: {e}") from e

STRATEGY_BOOTSTRAP = load_strategy_bootstrap()

def response_output_text(data: dict[str, Any]) -> str:
    chunks=[]
    for item in data.get("output", []) or []:
        if item.get("type") != "message":
            continue
        for c in item.get("content", []) or []:
            if c.get("type") in ("output_text", "text") and c.get("text"):
                chunks.append(c["text"])
    return "\n".join(chunks).strip()

def parse_json_object(text: str) -> dict[str, Any]:
    text=text.strip()
    if text.startswith("```"):
        text=text.strip("`")
        if text.lower().startswith("json"):
            text=text[4:].lstrip()
    try:
        return json.loads(text)
    except Exception:
        start=text.find("{"); end=text.rfind("}")
        if start>=0 and end>start:
            return json.loads(text[start:end+1])
        raise ValueError("Strategy model did not return valid JSON")

def strategy_prompt(scan_payload: dict[str, Any]) -> str:
    return f"""You are the AI Trading Bridge strategy engine bootstrapped from an existing ChatGPT trading conversation.

PERMANENT STRATEGY RULES:
{json.dumps(STRATEGY_BOOTSTRAP, separators=(',', ':'))}

CURRENT SCAN SESSION:
{json.dumps(scan_payload, separators=(',', ':'))}

Analyze every scanned instrument using the permanent rules. Do not use the technicalScreen score as the decision; it is only precomputed context. Use the actual 4H, 1H, 15M, and 5M OHLC, volume, and RSI data. Select zero to three proposals. Only A+ or A setups may be proposed. B setups must not be proposed. If there are no A/A+ setups, return an empty proposals array. Do not force three trades. Consider correlated exposure. Do not claim a safe position size because numeric risk limits have not been configured.

Return ONLY valid JSON with this exact top-level shape:
{{
  "scan_session_id": "{scan_payload.get('scanSessionId','')}",
  "summary": "short overall scan summary",
  "proposals": [
    {{
      "rank": 1,
      "symbol": "broker exact symbol",
      "direction": "BUY or SELL",
      "setup_grade": "A+ or A",
      "score": 0,
      "entry": 0,
      "safe_loss": 0,
      "take_profit_1": 0,
      "take_profit_2": 0,
      "risk_percent": null,
      "risk_reward": "text ratio or description",
      "invalidation": "specific structural invalidation",
      "missing_confirmation": "none or what is still missing",
      "explanation": "Detailed reasoning covering 4H bias, 1H structure, 15M setup, 5M trigger, RSI, volume, key level, entry logic, stop, targets, cancellation condition and why the grade is A/A+."
    }}
  ]
}}
"""

def run_bootstrapped_strategy(scan_payload: dict[str, Any]) -> dict[str, Any]:
    if not OPENAI_API_KEY:
        return {"status":"OPENAI_NOT_CONFIGURED","message":"Add OPENAI_API_KEY on the server to enable the bootstrapped strategy engine."}
    headers={"Authorization":f"Bearer {OPENAI_API_KEY}","Content-Type":"application/json"}
    body={
        "model":OPENAI_MODEL,
        "input":strategy_prompt(scan_payload),
        "max_output_tokens":7000
    }
    with httpx.Client(timeout=180.0) as client:
        r=client.post("https://api.openai.com/v1/responses",headers=headers,json=body)
        r.raise_for_status(); raw=r.json()
    text=response_output_text(raw)
    parsed=parse_json_object(text)
    proposals=parsed.get("proposals") or []
    if not isinstance(proposals,list) or len(proposals)>3:
        raise ValueError("Strategy response must contain zero to three proposals")
    return {"status":"ANALYZED","model":OPENAI_MODEL,"response_id":raw.get("id"),"summary":parsed.get("summary",""),"proposals":proposals}

def save_bootstrapped_strategy_proposals(scan_payload: dict[str, Any], analysis: dict[str, Any]) -> list[dict[str, Any]]:
    account=scan_payload["account"]; allowed={x.get("symbol") for x in scan_payload.get("results",[]) if not x.get("error")}; saved=[]
    for idx,item in enumerate(analysis.get("proposals") or []):
        symbol=item.get("symbol")
        if symbol not in allowed:
            continue
        direction=str(item.get("direction","")).upper()
        if direction not in ("BUY","SELL"):
            continue
        grade=str(item.get("setup_grade","")).upper()
        if grade not in ("A","A+"):
            continue
        try:
            entry=float(item["entry"]); sl=float(item["safe_loss"]); tp1=float(item["take_profit_1"]); tp2=float(item["take_profit_2"]); score=float(item.get("score",0))
        except Exception:
            continue
        inst=next((x.get("instrument") for x in scan_payload["results"] if x.get("symbol")==symbol),{"symbol":symbol})
        p={"proposalId":"bootstrap-"+uuid.uuid4().hex[:16],"scanSessionId":scan_payload["scanSessionId"],"accountId":account["id"],
           "platform":account["platform"],"accountNumber":account["account_number"],"symbol":symbol,"instrument":inst,
           "direction":direction,"entry":entry,"safeLoss":sl,"takeProfit1":tp1,"takeProfit2":tp2,
           "riskPercent":None,"score":max(0,min(100,score)),"rank":idx+1,"setupGrade":grade,
           "riskReward":item.get("risk_reward","") or "","invalidation":item.get("invalidation","") or "",
           "missingConfirmation":item.get("missing_confirmation","") or "",
           "explanation":item.get("explanation","") or "","source":"BOOTSTRAPPED_CHATGPT_STRATEGY",
           "conversationLabel":"AI Trading 5k funded · Bootstrap v1","conversationReference":"exported_strategy_bootstrap_v1",
           "strategyModel":analysis.get("model"),"strategyResponseId":analysis.get("response_id"),"status":"AWAITING_APPROVAL"}
        save_proposal(p); saved.append(p)
    audit("bootstrapped_openai_strategy",account["id"],scan_session_id=scan_payload["scanSessionId"],count=len(saved),model=analysis.get("model"),response_id=analysis.get("response_id"))
    return saved

TIMEFRAMES = {"4H": "4H", "1H": "1H", "15M": "15m", "5M": "5m"}
TF_SECONDS = {"4H": 14400, "1H": 3600, "15M": 900, "5M": 300}


def db_init() -> None:
    with sqlite3.connect(DB_PATH) as c:
        c.executescript("""
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS connections(
          id TEXT PRIMARY KEY, platform TEXT NOT NULL, label TEXT NOT NULL,
          environment TEXT NOT NULL, secret_blob TEXT NOT NULL, created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS accounts(
          id TEXT PRIMARY KEY, connection_id TEXT NOT NULL, platform TEXT NOT NULL,
          account_number TEXT NOT NULL, account_id TEXT, acc_num TEXT,
          environment TEXT NOT NULL, label TEXT, active INTEGER DEFAULT 0,
          meta_json TEXT DEFAULT '{}', UNIQUE(connection_id, account_number)
        );
        CREATE TABLE IF NOT EXISTS alerts(
          id TEXT PRIMARY KEY, account_id TEXT NOT NULL, symbol TEXT NOT NULL,
          condition TEXT NOT NULL, level REAL NOT NULL, enabled INTEGER DEFAULT 1,
          created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS proposals(
          id TEXT PRIMARY KEY, account_id TEXT NOT NULL, payload_json TEXT NOT NULL,
          status TEXT NOT NULL, created_at TEXT NOT NULL, decided_at TEXT
        );
        CREATE TABLE IF NOT EXISTS audit(
          id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL, action TEXT NOT NULL,
          account_id TEXT, details_json TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS scan_sessions(
          id TEXT PRIMARY KEY, account_id TEXT NOT NULL, payload_json TEXT NOT NULL, created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS strategy_state(
          key TEXT PRIMARY KEY, value_json TEXT NOT NULL, updated_at TEXT NOT NULL
        );
        """)

db_init()


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def encrypt_json(value: dict[str, Any]) -> str:
    return FERNET.encrypt(json.dumps(value).encode()).decode()


def decrypt_json(blob: str) -> dict[str, Any]:
    try:
        return json.loads(FERNET.decrypt(blob.encode()).decode())
    except (InvalidToken, ValueError, json.JSONDecodeError) as e:
        raise RuntimeError("Stored credentials cannot be decrypted. Check TRADING_BRIDGE_SECRET.") from e


def audit(action: str, account_id: str | None = None, **details: Any) -> None:
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT INTO audit(ts,action,account_id,details_json) VALUES(?,?,?,?)",
                  (utcnow(), action, account_id, json.dumps(details)))


def rowdict(cur: sqlite3.Cursor, row: tuple[Any, ...]) -> dict[str, Any]:
    return {cur.description[i][0]: row[i] for i in range(len(row))}


class Broker(Protocol):
    platform: str
    def list_accounts(self) -> list[dict[str, Any]]: ...
    def account_state(self, account: dict[str, Any]) -> dict[str, Any]: ...
    def instruments(self, account: dict[str, Any]) -> list[dict[str, Any]]: ...
    def candles(self, account: dict[str, Any], instrument: dict[str, Any], tf: str, count: int = 120) -> list[dict[str, Any]]: ...
    def positions(self, account: dict[str, Any]) -> Any: ...
    def orders(self, account: dict[str, Any]) -> Any: ...
    def place_order(self, account: dict[str, Any], instrument: dict[str, Any], order: dict[str, Any]) -> Any: ...


class TradeLockerBroker:
    platform = "TradeLocker"
    def __init__(self, creds: dict[str, Any]):
        self.creds = creds
        env = creds.get("environment", "DEMO").upper()
        self.base = "https://demo.tradelocker.com/backend-api" if env == "DEMO" else "https://live.tradelocker.com/backend-api"
        self.client = httpx.Client(timeout=25.0)
        self.token = creds.get("access_token")
        if not self.token:
            self._login()

    def _login(self) -> None:
        r = self.client.post(f"{self.base}/auth/jwt/token", json={
            "email": self.creds["email"], "password": self.creds["password"], "server": self.creds["server"]
        })
        r.raise_for_status()
        data = r.json()
        self.token = data.get("accessToken") or data.get("access_token") or (data.get("d") or {}).get("accessToken")
        if not self.token:
            raise RuntimeError("TradeLocker login succeeded but no access token was returned.")

    @property
    def headers(self) -> dict[str, str]:
        h = {"Authorization": f"Bearer {self.token}"}
        if self.creds.get("developer_api_key"):
            h["tl-developer-api-key"] = self.creds["developer_api_key"]
        return h

    def _acc_headers(self, account: dict[str, Any]) -> dict[str, str]:
        return {**self.headers, "accNum": str(account.get("acc_num") or account.get("account_number"))}

    def list_accounts(self) -> list[dict[str, Any]]:
        r = self.client.get(f"{self.base}/auth/jwt/all-accounts", headers=self.headers)
        r.raise_for_status(); data = r.json()
        raw = data.get("accounts") or data.get("d") or data
        if isinstance(raw, dict):
            raw = raw.get("accounts") or raw.get("data") or []
        out = []
        for a in raw if isinstance(raw, list) else []:
            acc_id = a.get("accountId") or a.get("id") or a.get("account_id")
            acc_num = a.get("accNum") or a.get("accountNumber") or a.get("acc_num")
            display = a.get("accountNumber") or a.get("name") or acc_id or acc_num
            out.append({"account_id": str(acc_id or display), "acc_num": str(acc_num or display), "account_number": str(display)})
        return out

    def account_state(self, account: dict[str, Any]) -> dict[str, Any]:
        r = self.client.get(f"{self.base}/trade/accounts/{account['account_id']}/state", headers=self._acc_headers(account)); r.raise_for_status()
        return r.json()

    def instruments(self, account: dict[str, Any]) -> list[dict[str, Any]]:
        r = self.client.get(f"{self.base}/trade/accounts/{account['account_id']}/instruments", headers=self._acc_headers(account)); r.raise_for_status()
        data = r.json(); raw = data.get("d") or data.get("instruments") or data
        if isinstance(raw, dict): raw = raw.get("instruments") or raw.get("data") or []
        out = []
        for x in raw if isinstance(raw, list) else []:
            routes = x.get("routes") or []
            info_route = None; trade_route = None
            for rr in routes:
                name = str(rr.get("type") or rr.get("name") or "").upper()
                rid = rr.get("id") or rr.get("routeId")
                if "INFO" in name: info_route = rid
                if "TRADE" in name: trade_route = rid
            out.append({
                "symbol": x.get("name") or x.get("symbol") or x.get("tradableInstrumentName") or str(x.get("tradableInstrumentId")),
                "tradableInstrumentId": x.get("tradableInstrumentId") or x.get("id"),
                "infoRouteId": info_route or x.get("routeId"), "tradeRouteId": trade_route or x.get("routeId"),
                "raw": x,
            })
        return out

    def quote_raw(self, account: dict[str, Any], instrument: dict[str, Any]) -> dict[str, Any]:
        """Fetch the authenticated INFO-route quote payload without interpreting its schema."""
        params = {"routeId": instrument["infoRouteId"],
                  "tradableInstrumentId": instrument["tradableInstrumentId"]}
        r = self.client.get(f"{self.base}/trade/quotes", params=params, headers=self._acc_headers(account))
        r.raise_for_status()
        return r.json()

    def candles(self, account: dict[str, Any], instrument: dict[str, Any], tf: str, count: int = 120) -> list[dict[str, Any]]:
        to_ms = int(time.time() * 1000); from_ms = to_ms - TF_SECONDS[tf] * count * 1000 * 2
        params = {"routeId": instrument["infoRouteId"], "from": from_ms, "to": to_ms,
                  "resolution": TIMEFRAMES[tf], "tradableInstrumentId": instrument["tradableInstrumentId"]}
        r = self.client.get(f"{self.base}/trade/history", params=params, headers=self._acc_headers(account)); r.raise_for_status()
        data = r.json(); d = data.get("d") or data
        # TradeLocker commonly returns column arrays. Support row objects too.
        if isinstance(d, dict) and any(k in d for k in ("t", "time", "o", "open")):
            t = d.get("t") or d.get("time") or []
            o = d.get("o") or d.get("open") or []; h = d.get("h") or d.get("high") or []
            l = d.get("l") or d.get("low") or []; c = d.get("c") or d.get("close") or []
            v = d.get("v") or d.get("volume") or [0] * len(c)
            return [{"time": t[i] if i < len(t) else i, "o": float(o[i]), "h": float(h[i]), "l": float(l[i]), "c": float(c[i]), "v": float(v[i] if i < len(v) else 0)} for i in range(min(len(o),len(h),len(l),len(c)))] [-count:]
        rows = d if isinstance(d, list) else []
        return [{"time": x.get("t") or x.get("time"), "o": float(x.get("o") or x.get("open")), "h": float(x.get("h") or x.get("high")), "l": float(x.get("l") or x.get("low")), "c": float(x.get("c") or x.get("close")), "v": float(x.get("v") or x.get("volume") or 0)} for x in rows][-count:]

    def positions(self, account: dict[str, Any]) -> Any:
        r = self.client.get(f"{self.base}/trade/accounts/{account['account_id']}/positions", headers=self._acc_headers(account)); r.raise_for_status(); return r.json()

    def orders(self, account: dict[str, Any]) -> Any:
        r = self.client.get(f"{self.base}/trade/accounts/{account['account_id']}/orders", headers=self._acc_headers(account)); r.raise_for_status(); return r.json()

    def place_order(self, account: dict[str, Any], instrument: dict[str, Any], order: dict[str, Any]) -> Any:
        typ = order.get("type", "market").lower(); side = order["side"].lower()
        payload = {"qty": float(order["qty"]), "routeId": instrument["tradeRouteId"], "side": side,
                   "validity": "IOC" if typ == "market" else "GTC", "type": typ,
                   "tradableInstrumentId": instrument["tradableInstrumentId"], "strategyId": "AITradingBridge"}
        if typ == "limit": payload["price"] = float(order["entry"])
        elif typ == "stop": payload["stopPrice"] = float(order["entry"])
        else: payload["price"] = 0
        if order.get("stop_loss") is not None:
            payload.update({"stopLoss": float(order["stop_loss"]), "stopLossType": "absolute"})
        if order.get("take_profit") is not None:
            payload.update({"takeProfit": float(order["take_profit"]), "takeProfitType": "absolute"})
        r = self.client.post(f"{self.base}/trade/accounts/{account['account_id']}/orders", json=payload, headers=self._acc_headers(account)); r.raise_for_status(); return r.json()


class MT5Broker:
    platform = "MetaTrader 5"
    def __init__(self, creds: dict[str, Any]):
        self.creds = creds
        try:
            import MetaTrader5 as mt5
        except Exception as e:
            raise RuntimeError("MetaTrader5 Python package is unavailable. Run this backend on Windows with the MT5 terminal installed.") from e
        self.mt5 = mt5
        path = creds.get("terminal_path") or None
        if not mt5.initialize(path=path) if path else not mt5.initialize():
            raise RuntimeError(f"MT5 initialize failed: {mt5.last_error()}")
        login = int(creds["login"])
        if not mt5.login(login, password=creds["password"], server=creds["server"]):
            raise RuntimeError(f"MT5 login failed: {mt5.last_error()}")

    def list_accounts(self) -> list[dict[str, Any]]:
        a = self.mt5.account_info()
        if not a: return []
        return [{"account_id": str(a.login), "acc_num": str(a.login), "account_number": str(a.login)}]

    def account_state(self, account: dict[str, Any]) -> dict[str, Any]:
        a = self.mt5.account_info(); return a._asdict() if a else {}

    def instruments(self, account: dict[str, Any]) -> list[dict[str, Any]]:
        syms = self.mt5.symbols_get() or []
        visible = [s for s in syms if getattr(s, "visible", False)] or list(syms)
        return [{"symbol": s.name, "tradableInstrumentId": s.name, "infoRouteId": 0, "tradeRouteId": 0, "raw": s._asdict()} for s in visible]

    def candles(self, account: dict[str, Any], instrument: dict[str, Any], tf: str, count: int = 120) -> list[dict[str, Any]]:
        m = {"4H": self.mt5.TIMEFRAME_H4, "1H": self.mt5.TIMEFRAME_H1, "15M": self.mt5.TIMEFRAME_M15, "5M": self.mt5.TIMEFRAME_M5}
        rates = self.mt5.copy_rates_from_pos(instrument["symbol"], m[tf], 0, count)
        if rates is None: raise RuntimeError(f"MT5 candles failed: {self.mt5.last_error()}")
        return [{"time": int(x["time"]), "o": float(x["open"]), "h": float(x["high"]), "l": float(x["low"]), "c": float(x["close"]), "v": float(x["real_volume"] or x["tick_volume"])} for x in rates]

    def positions(self, account: dict[str, Any]) -> Any:
        p = self.mt5.positions_get() or []; return [x._asdict() for x in p]

    def orders(self, account: dict[str, Any]) -> Any:
        p = self.mt5.orders_get() or []; return [x._asdict() for x in p]

    def place_order(self, account: dict[str, Any], instrument: dict[str, Any], order: dict[str, Any]) -> Any:
        symbol = instrument["symbol"]; tick = self.mt5.symbol_info_tick(symbol)
        if not tick: raise RuntimeError("No MT5 tick available")
        side_buy = order["side"].lower() == "buy"; typ = order.get("type", "market").lower()
        if typ != "market": raise RuntimeError("MT5 v1 adapter currently enables market execution only; pending orders remain available in simulation mode.")
        request = {"action": self.mt5.TRADE_ACTION_DEAL, "symbol": symbol, "volume": float(order["qty"]),
                   "type": self.mt5.ORDER_TYPE_BUY if side_buy else self.mt5.ORDER_TYPE_SELL,
                   "price": tick.ask if side_buy else tick.bid, "deviation": 20, "magic": 560001,
                   "comment": "AITradingBridge", "type_time": self.mt5.ORDER_TIME_GTC, "type_filling": self.mt5.ORDER_FILLING_IOC}
        if order.get("stop_loss") is not None: request["sl"] = float(order["stop_loss"])
        if order.get("take_profit") is not None: request["tp"] = float(order["take_profit"])
        result = self.mt5.order_send(request)
        return result._asdict() if result else {"error": self.mt5.last_error()}


SIM_ACCOUNTS = [
    {"id":"sim-tl-784215","platform":"TradeLocker","account_number":"784215","account_id":"784215","acc_num":"1","environment":"SIMULATED","connection_id":"sim","label":"TradeLocker Demo","active":1},
    {"id":"sim-mt5-51003821","platform":"MetaTrader 5","account_number":"51003821","account_id":"51003821","acc_num":"51003821","environment":"SIMULATED","connection_id":"sim","label":"MT5 Demo","active":0},
]
SIM_SYMBOLS = {
    "sim-tl-784215": ["BTCUSD","ETHUSD","EURUSD","GBPUSD","XAUUSD","NAS100"],
    "sim-mt5-51003821": ["BTCUSD.m","ETHUSD.m","EURUSD.a","GBPUSD.a","GOLD","USTEC"],
}
SIM_BASE = {"BTCUSD":64250,"BTCUSD.m":64240,"ETHUSD":2385,"ETHUSD.m":2384,"EURUSD":1.1682,"EURUSD.a":1.1681,"GBPUSD":1.3512,"GBPUSD.a":1.3511,"XAUUSD":3375,"GOLD":3374,"NAS100":23650,"USTEC":23645}


def _seed(s: str) -> random.Random:
    return random.Random(int(__import__("hashlib").sha256(s.encode()).hexdigest()[:16],16))


def calc_rsi(rows: list[dict[str, Any]], period: int = 14) -> None:
    if len(rows) < period + 1:
        for x in rows: x["rsi"] = 50.0
        return
    gains=[]; losses=[]
    for i in range(1,period+1):
        d=rows[i]["c"]-rows[i-1]["c"]; gains.append(max(d,0)); losses.append(max(-d,0))
    ag=sum(gains)/period; al=sum(losses)/period
    for i,x in enumerate(rows): x["rsi"] = 50.0
    rows[period]["rsi"] = 100.0 if al == 0 else 100 - 100/(1+ag/al)
    for i in range(period+1,len(rows)):
        d=rows[i]["c"]-rows[i-1]["c"]; ag=(ag*(period-1)+max(d,0))/period; al=(al*(period-1)+max(-d,0))/period
        rows[i]["rsi"] = 100.0 if al == 0 else 100 - 100/(1+ag/al)
    first=rows[period]["rsi"]
    for i in range(period): rows[i]["rsi"]=first


def sim_candles(account_id: str, symbol: str, tf: str, count: int=120) -> list[dict[str,Any]]:
    rng=_seed(account_id+symbol+tf+datetime.now(timezone.utc).strftime("%Y-%m-%d-%H"))
    base=SIM_BASE.get(symbol,100.0); p=base*(0.98+rng.random()*0.04); vol={"4H":.006,"1H":.003,"15M":.0015,"5M":.0008}[tf]
    rows=[]; now=int(time.time())
    for i in range(count):
        o=p; d=(rng.random()-.48)*base*vol; c=max(base*.1,o+d); span=abs(d)+base*vol*(.2+rng.random()*.6)
        rows.append({"time":now-(count-i)*TF_SECONDS[tf],"o":o,"h":max(o,c)+span*rng.random(),"l":min(o,c)-span*rng.random(),"c":c,"v":int(100+1000*rng.random())}); p=c
    calc_rsi(rows); return rows


def all_accounts() -> list[dict[str,Any]]:
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row; rows=[dict(x) for x in c.execute("SELECT * FROM accounts ORDER BY platform,account_number")]
    if not rows: return [dict(x) for x in SIM_ACCOUNTS]
    return rows


def active_account() -> dict[str,Any]:
    rows=all_accounts(); a=next((x for x in rows if int(x.get("active") or 0)==1),None); return a or rows[0]


def set_active(account_id: str) -> dict[str,Any]:
    if account_id.startswith("sim-"):
        for a in SIM_ACCOUNTS: a["active"] = 1 if a["id"] == account_id else 0
        return active_account()
    with sqlite3.connect(DB_PATH) as c:
        c.execute("UPDATE accounts SET active=0"); c.execute("UPDATE accounts SET active=1 WHERE id=?",(account_id,))
    return active_account()


def broker_for(account: dict[str,Any]) -> Broker | None:
    if account["id"].startswith("sim-"): return None
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row; row=c.execute("SELECT * FROM connections WHERE id=?",(account["connection_id"],)).fetchone()
    if not row: raise RuntimeError("Connection not found")
    creds=decrypt_json(row["secret_blob"]); creds["environment"]=row["environment"]
    return TradeLockerBroker(creds) if row["platform"]=="TradeLocker" else MT5Broker(creds)


def instruments_for(account: dict[str,Any]) -> list[dict[str,Any]]:
    broker=broker_for(account)
    if broker: return broker.instruments(account)
    return [{"symbol":s,"tradableInstrumentId":s,"infoRouteId":0,"tradeRouteId":0} for s in SIM_SYMBOLS.get(account["id"],[])]


def bundle_for(account: dict[str,Any], instrument: dict[str,Any]) -> dict[str,list[dict[str,Any]]]:
    broker=broker_for(account); out={}
    for tf in TIMEFRAMES:
        rows=broker.candles(account,instrument,tf,120) if broker else sim_candles(account["id"],instrument["symbol"],tf,120)
        calc_rsi(rows); out[tf]=rows
    return out


def score(bundle: dict[str,list[dict[str,Any]]]) -> dict[str,Any]:
    rsis={tf:bundle[tf][-1]["rsi"] for tf in TIMEFRAMES}; avg=sum(rsis.values())/4
    direction="BUY" if avg>=50 else "SELL"; alignment=sum(1 for r in rsis.values() if (r>=50)==(direction=="BUY"))
    v15=bundle["15M"][-1]["v"]; vavg=sum(x["v"] for x in bundle["15M"][-20:])/20 if bundle["15M"] else 1
    s=min(98,int(46+alignment*9+abs(avg-50)*.8+min(v15/max(vavg,1),2)*4))
    return {"direction":direction,"score":s,"rsis":rsis,"volumeRatio15m":round(v15/max(vavg,1),2)}


def scan(account: dict[str,Any], max_symbols: int=40) -> dict[str,Any]:
    """Collect broker data only. The Trading Bridge does not choose trades.
    The linked ChatGPT strategy conversation consumes this scan and submits proposals separately.
    """
    inst=instruments_for(account)[:max_symbols]; results=[]
    for x in inst:
        try:
            b=bundle_for(account,x); ev=score(b)
            results.append({
                "symbol":x["symbol"],
                "instrument":{k:v for k,v in x.items() if k!="raw"},
                "technicalScreen":ev,
                "timeframes":{tf:{
                    "lastClose":b[tf][-1]["c"],"rsi14":b[tf][-1]["rsi"],
                    "lastVolume":b[tf][-1]["v"],"candles":b[tf][-60:]
                } for tf in TIMEFRAMES}
            })
        except Exception as e:
            results.append({"symbol":x.get("symbol","?"),"error":str(e)})
    session_id="scan-"+uuid.uuid4().hex[:16]
    payload={"scanSessionId":session_id,"account":public_account(account),"symbolsScanned":len(inst),
             "timeframes":list(TIMEFRAMES),"results":results,
             "executionEnabled":EXECUTION_ENABLED,"liveExecutionEnabled":LIVE_EXECUTION_ENABLED,
             "strategyRequired":True,
             "message":"Market data collected. The linked ChatGPT strategy conversation must rank and submit the trade proposals."}
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT INTO scan_sessions(id,account_id,payload_json,created_at) VALUES(?,?,?,?)",
                  (session_id,account["id"],json.dumps(payload),utcnow()))
    audit("scan_everything",account["id"],scan_session_id=session_id,symbols=len(inst))
    return payload

def save_proposal(p: dict[str,Any]) -> None:
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT OR REPLACE INTO proposals(id,account_id,payload_json,status,created_at) VALUES(?,?,?,?,?)",
                  (p["proposalId"],p["accountId"],json.dumps(p),p["status"],utcnow()))

def latest_strategy_proposals(account_id: str | None=None) -> list[dict[str,Any]]:
    aid=account_id or active_account()["id"]
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row
        rows=c.execute("SELECT payload_json FROM proposals WHERE account_id=? ORDER BY created_at DESC LIMIT 30",(aid,)).fetchall()
    out=[]; seen=set()
    for r in rows:
        p=json.loads(r["payload_json"])
        if p.get("source") not in TRUSTED_STRATEGY_SOURCES: continue
        sid=p.get("scanSessionId")
        if not seen: first=sid
        if sid!=first: break
        if p["proposalId"] not in seen: out.append(p); seen.add(p["proposalId"])
    return sorted(out,key=lambda x:x.get("rank",99))[:3]

def public_account(a: dict[str,Any]) -> dict[str,Any]:
    return {k:a.get(k) for k in ("id","platform","account_number","account_id","acc_num","environment","label")}


class TLConnect(BaseModel):
    email: str; password: str; server: str; environment: str = "DEMO"; label: str = "TradeLocker"; developer_api_key: str | None = None
class MTConnect(BaseModel):
    login: str; password: str; server: str; terminal_path: str | None = None; environment: str = "DEMO"; label: str = "MetaTrader 5"
class SelectReq(BaseModel): account_id: str
class ScanReq(BaseModel): account_id: str | None = None; max_symbols: int = Field(default=40, ge=1, le=200)
class ApproveReq(BaseModel): proposal_id: str; qty: float = Field(gt=0); order_type: str = "market"; use_tp2: bool = False
class StrategyProposalItem(BaseModel):
    rank: int = Field(ge=1,le=3); symbol: str; direction: str; entry: float; safe_loss: float; take_profit_1: float; take_profit_2: float; risk_percent: float | None = Field(default=None, gt=0,le=5); score: float = Field(ge=0,le=100); explanation: str = ""
class StrategySubmitReq(BaseModel):
    scan_session_id: str; conversation_label: str = "Existing ChatGPT trading conversation"; conversation_reference: str | None = None; proposals: list[StrategyProposalItem]
class StrategyExplanationReq(BaseModel): proposal_id: str; explanation: str; conversation_reference: str | None = None
class AlertReq(BaseModel): symbol: str; condition: str; level: float


@app.get("/health")
def health():
    return {"ok":True,"version":"1.3.0","executionEnabled":EXECUTION_ENABLED,"liveExecutionEnabled":LIVE_EXECUTION_ENABLED,"database":str(DB_PATH.name),"strategyConfigured":bool(OPENAI_API_KEY),"strategyModel":OPENAI_MODEL,"strategyName":STRATEGY_BOOTSTRAP.get("strategy_name")}

@app.get("/api/accounts")
def api_accounts(): return {"accounts":[public_account(a) for a in all_accounts()],"active":public_account(active_account())}

@app.post("/api/select-account")
def api_select(req: SelectReq):
    a=set_active(req.account_id); audit("select_account",a["id"]); return public_account(a)

@app.post("/api/connect/tradelocker")
def connect_tl(req: TLConnect):
    creds=req.model_dump(); env=req.environment.upper(); broker=TradeLockerBroker({**creds,"environment":env}); discovered=broker.list_accounts()
    if not discovered: raise HTTPException(400,"No TradeLocker accounts were discovered.")
    cid="tlc-"+uuid.uuid4().hex[:12]
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT INTO connections VALUES(?,?,?,?,?,?)",(cid,"TradeLocker",req.label,env,encrypt_json(creds),utcnow()))
        c.execute("UPDATE accounts SET active=0")
        for i,a in enumerate(discovered):
            aid="tl-"+cid[-6:]+"-"+str(a["account_number"])
            c.execute("INSERT OR REPLACE INTO accounts(id,connection_id,platform,account_number,account_id,acc_num,environment,label,active,meta_json) VALUES(?,?,?,?,?,?,?,?,?,?)",(aid,cid,"TradeLocker",a["account_number"],a["account_id"],a["acc_num"],env,req.label,1 if i==0 else 0,"{}"))
    audit("connect_tradelocker",details={"accounts":len(discovered)})
    return api_accounts()

@app.post("/api/connect/mt5")
def connect_mt5(req: MTConnect):
    creds=req.model_dump(); broker=MT5Broker(creds); discovered=broker.list_accounts()
    if not discovered: raise HTTPException(400,"No MT5 account was discovered.")
    cid="mtc-"+uuid.uuid4().hex[:12]
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT INTO connections VALUES(?,?,?,?,?,?)",(cid,"MetaTrader 5",req.label,req.environment.upper(),encrypt_json(creds),utcnow())); c.execute("UPDATE accounts SET active=0")
        for i,a in enumerate(discovered):
            aid="mt5-"+str(a["account_number"])
            c.execute("INSERT OR REPLACE INTO accounts(id,connection_id,platform,account_number,account_id,acc_num,environment,label,active,meta_json) VALUES(?,?,?,?,?,?,?,?,?,?)",(aid,cid,"MetaTrader 5",a["account_number"],a["account_id"],a["acc_num"],req.environment.upper(),req.label,1 if i==0 else 0,"{}"))
    audit("connect_mt5",details={"accounts":len(discovered)}); return api_accounts()

@app.post("/api/scan")
def api_scan(req: ScanReq):
    a=next((x for x in all_accounts() if x["id"]==(req.account_id or active_account()["id"])),None)
    if not a: raise HTTPException(404,"Account not found")
    try:
        payload=scan(a,req.max_symbols)
        if OPENAI_API_KEY:
            analysis=run_bootstrapped_strategy(payload)
            saved=save_bootstrapped_strategy_proposals(payload,analysis)
            payload["strategy"]={"status":analysis.get("status"),"model":analysis.get("model"),"summary":analysis.get("summary",""),"proposalsSaved":len(saved),"source":"BOOTSTRAPPED_CHATGPT_STRATEGY"}
        else:
            payload["strategy"]={"status":"OPENAI_NOT_CONFIGURED","proposalsSaved":0,"source":"BOOTSTRAPPED_CHATGPT_STRATEGY"}
        return payload
    except httpx.HTTPStatusError as e:
        detail=e.response.text[:1000] if e.response is not None else str(e)
        raise HTTPException(502,f"OpenAI strategy request failed: {detail}")
    except Exception as e: raise HTTPException(502,str(e))

RADAR_REQUIRED_FIELDS = (
    "bid", "ask", "currentDayHigh", "currentDayLow", "previousDayClose",
    "previousDayHigh", "previousDayLow", "price1HourAgo", "price4HoursAgo",
)


def _radar_quote_observation(broker: Any, account: dict[str, Any], instrument: dict[str, Any]) -> dict[str, Any]:
    """Preserve authenticated raw quote evidence; Bid/Ask stay unresolved until schema validation."""
    quote_raw = getattr(broker, "quote_raw", None)
    if quote_raw is None:
        return {"status": "UNAVAILABLE", "reason": "authenticated_quote_acquisition_unavailable", "rawResponse": None}
    payload = quote_raw(account, instrument)
    return {"status": "QUESTIONABLE", "reason": "quote_schema_mapping_unverified", "rawResponse": payload}


def _radar_history_observation(account: dict[str, Any], instrument: dict[str, Any]) -> dict[str, Any]:
    """Read-only Radar compatibility projection over verified Bridge history acquisition.

    Deliberately does not synthesize quotes or assume broker session/day boundaries.
    """
    broker = broker_for(account)
    if broker is None:
        return {"status": "UNAVAILABLE", "reason": "authenticated_bridge_acquisition_unavailable"}
    rows = broker.candles(account, instrument, "1H", 8)
    completed = sorted((x for x in rows if x.get("time") is not None), key=lambda x: x["time"])
    now_s = int(time.time())
    completed = [x for x in completed if int(x["time"]) + TF_SECONDS["1H"] <= now_s]
    latest = completed[-1] if completed else None
    one = completed[-1] if completed else None
    four = completed[-4] if len(completed) >= 4 else None
    source_ts = latest.get("time") if latest else None
    freshness = (now_s - int(source_ts)) if source_ts is not None else None
    return {
        "status": "QUESTIONABLE" if latest else "MISSING",
        "reason": "live_quote_and_session_day_semantics_unverified",
        "sourceTimestamp": source_ts,
        "freshnessSeconds": freshness,
        "price1HourAgo": one.get("c") if one else None,
        "price4HoursAgo": four.get("c") if four else None,
    }


def radar_observation(symbol: str, account_id: str | None = None) -> dict[str, Any]:
    account = next((x for x in all_accounts() if x["id"] == (account_id or active_account()["id"])), None)
    if not account:
        raise HTTPException(404, "Account not found")
    instrument = next((x for x in instruments_for(account) if x["symbol"] == symbol), None)
    if not instrument:
        raise HTTPException(404, "Symbol not found")
    broker = broker_for(account)
    quote = _radar_quote_observation(broker, account, instrument) if broker is not None else {
        "status": "UNAVAILABLE", "reason": "authenticated_bridge_acquisition_unavailable", "rawResponse": None}
    hist = _radar_history_observation(account, instrument)
    raw = {key: None for key in RADAR_REQUIRED_FIELDS}
    raw["price1HourAgo"] = hist.get("price1HourAgo")
    raw["price4HoursAgo"] = hist.get("price4HoursAgo")
    return {
        "symbol": symbol,
        "raw": raw,
        "quality": {"status": hist["status"], "reason": hist["reason"],
                    "sourceTimestamp": hist.get("sourceTimestamp"), "freshnessSeconds": hist.get("freshnessSeconds")},
        "session": {"dayBoundary": None, "status": "UNRESOLVED"},
        "quoteEvidence": {"status": quote["status"], "reason": quote["reason"], "rawResponse": quote["rawResponse"]},
        "provenance": {"provider": "TradeLocker", "owner": "AI Trading Bridge",
                       "acquisition": ["authenticated_quote", "authenticated_history"], "reconnaissanceOnly": True},
    }


@app.get("/api/radar/v0/instruments")
def api_radar_instruments(account_id: str | None = None):
    account = next((x for x in all_accounts() if x["id"] == (account_id or active_account()["id"])), None)
    if not account:
        raise HTTPException(404, "Account not found")
    return {"instruments": [{"symbol": x["symbol"]} for x in instruments_for(account)]}


@app.get("/api/radar/v0/observations")
def api_radar_observations(symbol: str, account_id: str | None = None):
    return radar_observation(symbol, account_id)


@app.get("/api/strategy/status")
def api_strategy_status():
    return {"configured":bool(OPENAI_API_KEY),"model":OPENAI_MODEL,"strategy":STRATEGY_BOOTSTRAP.get("strategy_name"),"version":STRATEGY_BOOTSTRAP.get("version"),"sourceConversation":"AI Trading 5k funded","mode":"BOOTSTRAPPED_API_STRATEGY"}

@app.post("/api/strategy/run/{scan_session_id}")
def api_strategy_run(scan_session_id: str):
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row; row=c.execute("SELECT * FROM scan_sessions WHERE id=?",(scan_session_id,)).fetchone()
    if not row: raise HTTPException(404,"Scan session not found")
    payload=json.loads(row["payload_json"])
    try:
        analysis=run_bootstrapped_strategy(payload); saved=save_bootstrapped_strategy_proposals(payload,analysis)
        return {"analysis":analysis,"proposals":saved}
    except httpx.HTTPStatusError as e:
        detail=e.response.text[:1000] if e.response is not None else str(e)
        raise HTTPException(502,f"OpenAI strategy request failed: {detail}")

@app.get("/api/chart/{symbol}")
def api_chart(symbol: str, account_id: str | None=None):
    a=next((x for x in all_accounts() if x["id"]==(account_id or active_account()["id"])),None)
    if not a: raise HTTPException(404,"Account not found")
    inst=next((x for x in instruments_for(a) if x["symbol"]==symbol),None)
    if not inst: raise HTTPException(404,"Symbol not found")
    b=bundle_for(a,inst); return {"account":public_account(a),"symbol":symbol,"bundle":b}

@app.get("/api/strategy/proposals")
def api_strategy_proposals(account_id: str | None=None):
    return {"proposals":latest_strategy_proposals(account_id)}

@app.post("/api/strategy/proposals")
def api_strategy_submit(req: StrategySubmitReq):
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row; row=c.execute("SELECT * FROM scan_sessions WHERE id=?",(req.scan_session_id,)).fetchone()
    if not row: raise HTTPException(404,"Scan session not found")
    session=json.loads(row["payload_json"]); account=session["account"]
    allowed={x.get("symbol") for x in session.get("results",[]) if not x.get("error")}
    if len(req.proposals)>3: raise HTTPException(400,"Submit at most three proposals")
    saved=[]
    for item in req.proposals:
        if item.symbol not in allowed: raise HTTPException(400,f"{item.symbol} was not in scan session")
        direction=item.direction.upper();
        if direction not in ("BUY","SELL","LONG","SHORT"): raise HTTPException(400,"direction must be BUY/SELL/LONG/SHORT")
        direction="BUY" if direction in ("BUY","LONG") else "SELL"
        p={"proposalId":"ai-"+uuid.uuid4().hex[:16],"scanSessionId":req.scan_session_id,"accountId":account["id"],
           "platform":account["platform"],"accountNumber":account["account_number"],"symbol":item.symbol,
           "instrument":next((x.get("instrument") for x in session["results"] if x.get("symbol")==item.symbol),{"symbol":item.symbol}),
           "direction":direction,"entry":item.entry,"safeLoss":item.safe_loss,"takeProfit1":item.take_profit_1,"takeProfit2":item.take_profit_2,
           "riskPercent":item.risk_percent,"score":item.score,"rank":item.rank,"explanation":item.explanation,
           "source":"CHATGPT_STRATEGY","conversationLabel":req.conversation_label,"conversationReference":req.conversation_reference,
           "status":"AWAITING_APPROVAL"}
        save_proposal(p); saved.append(p)
    audit("chatgpt_strategy_proposals",account["id"],scan_session_id=req.scan_session_id,count=len(saved),conversation=req.conversation_label)
    return {"status":"RECEIVED_FROM_CHATGPT_STRATEGY","proposals":sorted(saved,key=lambda x:x["rank"])}

@app.post("/api/strategy/explanation")
def api_strategy_explanation(req: StrategyExplanationReq):
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row; row=c.execute("SELECT * FROM proposals WHERE id=?",(req.proposal_id,)).fetchone()
        if not row: raise HTTPException(404,"Proposal not found")
        p=json.loads(row["payload_json"]); p["explanation"]=req.explanation
        if req.conversation_reference: p["conversationReference"]=req.conversation_reference
        c.execute("UPDATE proposals SET payload_json=? WHERE id=?",(json.dumps(p),req.proposal_id))
    audit("chatgpt_strategy_explanation",p.get("accountId"),proposal_id=req.proposal_id)
    return {"status":"EXPLANATION_STORED","proposal":p}

@app.post("/api/proposals/approve")
def approve(req: ApproveReq):
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row; row=c.execute("SELECT * FROM proposals WHERE id=?",(req.proposal_id,)).fetchone()
    if not row: raise HTTPException(404,"Proposal not found")
    p=json.loads(row["payload_json"]);
    if p.get("source") not in TRUSTED_STRATEGY_SOURCES: raise HTTPException(403,"Only proposals produced by an approved ChatGPT strategy source can be approved.")
    a=next((x for x in all_accounts() if x["id"]==p["accountId"]),None)
    if not a: raise HTTPException(404,"Account not found")
    # Simulation accounts always simulate. Real accounts require explicit server switches.
    if a["id"].startswith("sim-") or not EXECUTION_ENABLED:
        status="SIMULATED_APPROVED"; result={"simulated":True,"reason":"Execution is disabled by server policy."}
    else:
        if a["environment"].upper()=="LIVE" and not LIVE_EXECUTION_ENABLED:
            raise HTTPException(403,"Live execution is disabled. Set TRADING_LIVE_EXECUTION_ENABLED=true only after demo testing.")
        broker=broker_for(a); inst=p["instrument"]
        result=broker.place_order(a,inst,{"qty":req.qty,"side":p["direction"].lower(),"type":req.order_type,"entry":p["entry"],"stop_loss":p["safeLoss"],"take_profit":p["takeProfit2"] if req.use_tp2 else p["takeProfit1"]})
        status="SENT_TO_BROKER"
    with sqlite3.connect(DB_PATH) as c:
        c.execute("UPDATE proposals SET status=?,decided_at=? WHERE id=?",(status,utcnow(),req.proposal_id))
    audit("approve_trade",a["id"],proposal_id=req.proposal_id,status=status,qty=req.qty)
    return {"status":status,"account":public_account(a),"proposal":p,"brokerResult":result}

@app.post("/api/proposals/reject/{proposal_id}")
def reject(proposal_id: str):
    with sqlite3.connect(DB_PATH) as c: c.execute("UPDATE proposals SET status='REJECTED',decided_at=? WHERE id=?",(utcnow(),proposal_id))
    audit("reject_trade",proposal_id=proposal_id); return {"status":"REJECTED","proposalId":proposal_id}

@app.post("/api/alerts")
def create_alert(req: AlertReq):
    a=active_account(); aid=str(uuid.uuid4())
    with sqlite3.connect(DB_PATH) as c: c.execute("INSERT INTO alerts VALUES(?,?,?,?,?,?,?)",(aid,a["id"],req.symbol,req.condition,req.level,1,utcnow()))
    audit("create_alert",a["id"],symbol=req.symbol,condition=req.condition,level=req.level); return {"id":aid,"account":public_account(a),**req.model_dump()}

@app.get("/api/audit")
def audit_log(limit: int=100):
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory=sqlite3.Row; rows=[dict(x) for x in c.execute("SELECT * FROM audit ORDER BY id DESC LIMIT ?",(min(limit,500),))]
    return {"events":rows}

TOOLS = [
 {"name":"get_active_account","description":"Return the exact active TradeLocker or MetaTrader account.","inputSchema":{"type":"object","properties":{}}},
 {"name":"list_accounts","description":"List connected trading accounts and exact account numbers.","inputSchema":{"type":"object","properties":{}}},
 {"name":"select_account","description":"Select the exact account used by future scans/actions.","inputSchema":{"type":"object","properties":{"account_id":{"type":"string"}},"required":["account_id"]}},
 {"name":"scan_everything","description":"Collect every broker-visible instrument on 4H, 1H, 15M and 5M with candles, volume and RSI. This tool does NOT choose trades. Use your conversation's saved trading rules to rank candidates, then call submit_trade_proposals.","inputSchema":{"type":"object","properties":{"max_symbols":{"type":"integer","default":40}}}},
 {"name":"submit_trade_proposals","description":"Submit up to three trade proposals chosen by this ChatGPT strategy conversation from a scan session. Include the conversation's own explanation for each proposal.","inputSchema":{"type":"object","properties":{"scan_session_id":{"type":"string"},"conversation_label":{"type":"string"},"conversation_reference":{"type":"string"},"proposals":{"type":"array","items":{"type":"object","properties":{"rank":{"type":"integer"},"symbol":{"type":"string"},"direction":{"type":"string"},"entry":{"type":"number"},"safe_loss":{"type":"number"},"take_profit_1":{"type":"number"},"take_profit_2":{"type":"number"},"risk_percent":{"type":"number"},"score":{"type":"number"},"explanation":{"type":"string"}},"required":["rank","symbol","direction","entry","safe_loss","take_profit_1","take_profit_2","risk_percent","score"]}}},"required":["scan_session_id","proposals"]}},
 {"name":"submit_trade_explanation","description":"Store or replace the explanation for a specific proposal using reasoning from this ChatGPT strategy conversation.","inputSchema":{"type":"object","properties":{"proposal_id":{"type":"string"},"explanation":{"type":"string"},"conversation_reference":{"type":"string"}},"required":["proposal_id","explanation"]}},
 {"name":"get_latest_strategy_proposals","description":"Return the latest top trade proposals submitted by the ChatGPT strategy conversation for the active account.","inputSchema":{"type":"object","properties":{}}},
 {"name":"get_chart_bundle","description":"Return four-timeframe candle, volume and RSI data for one broker symbol.","inputSchema":{"type":"object","properties":{"symbol":{"type":"string"}},"required":["symbol"]}},
 {"name":"approve_trade","description":"Approve a proposal. Server risk/execution policy still applies; qty is mandatory.","inputSchema":{"type":"object","properties":{"proposal_id":{"type":"string"},"qty":{"type":"number"},"use_tp2":{"type":"boolean"}},"required":["proposal_id","qty"]}},
 {"name":"reject_trade","description":"Reject a proposed trade.","inputSchema":{"type":"object","properties":{"proposal_id":{"type":"string"}},"required":["proposal_id"]}},
 {"name":"create_alert","description":"Create a price alert tied to the active account.","inputSchema":{"type":"object","properties":{"symbol":{"type":"string"},"condition":{"type":"string"},"level":{"type":"number"}},"required":["symbol","condition","level"]}},
]

@app.get("/mcp-tools")
def mcp_tools(): return {"tools":TOOLS}

async def call_tool(name: str, args: dict[str,Any]) -> Any:
    if name=="get_active_account": return public_account(active_account())
    if name=="list_accounts": return [public_account(x) for x in all_accounts()]
    if name=="select_account": return public_account(set_active(args["account_id"]))
    if name=="scan_everything": return scan(active_account(),int(args.get("max_symbols",40)))
    if name=="submit_trade_proposals": return api_strategy_submit(StrategySubmitReq(**args))
    if name=="submit_trade_explanation": return api_strategy_explanation(StrategyExplanationReq(**args))
    if name=="get_latest_strategy_proposals": return {"proposals":latest_strategy_proposals()}
    if name=="get_chart_bundle":
        a=active_account(); inst=next((x for x in instruments_for(a) if x["symbol"]==args["symbol"]),None)
        if not inst: raise ValueError("Symbol not found")
        return {"account":public_account(a),"symbol":args["symbol"],"bundle":bundle_for(a,inst)}
    if name=="approve_trade": return approve(ApproveReq(proposal_id=args["proposal_id"],qty=float(args["qty"]),use_tp2=bool(args.get("use_tp2",False))))
    if name=="reject_trade": return reject(args["proposal_id"])
    if name=="create_alert": return create_alert(AlertReq(**args))
    raise ValueError("Unknown tool")

@app.post("/mcp")
async def mcp(request: Request):
    body=await request.json(); method=body.get("method"); rid=body.get("id")
    try:
        if method=="initialize": result={"protocolVersion":"2025-06-18","capabilities":{"tools":{}},"serverInfo":{"name":"ai-trading-bridge","version":"1.3.0"}}
        elif method=="tools/list": result={"tools":TOOLS}
        elif method=="tools/call":
            p=body.get("params",{}); value=await call_tool(p.get("name"),p.get("arguments") or {})
            result={"content":[{"type":"text","text":json.dumps(value)}],"structuredContent":value}
        else: raise ValueError(f"Unsupported MCP method: {method}")
        return {"jsonrpc":"2.0","id":rid,"result":result}
    except Exception as e:
        return JSONResponse({"jsonrpc":"2.0","id":rid,"error":{"code":-32000,"message":str(e)}},status_code=400)

@app.get("/")
def index(): return FileResponse(ROOT/"index.html")

app.mount("/", StaticFiles(directory=ROOT, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app",host="0.0.0.0",port=int(os.getenv("PORT","8080")),reload=False)
