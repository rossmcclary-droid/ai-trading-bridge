# AI Trading Bridge v1.2

A mobile-first PWA + FastAPI/MCP bridge for TradeLocker and MetaTrader 5. The bridge collects 4H / 1H / 15M / 5M candles, volume and RSI, but the linked ChatGPT trading conversation is the strategy source: it ranks the Top 3, submits the trade proposals, and supplies the explanations.

## What is real in v1.2

- Persistent SQLite database for connections, exact broker accounts, alerts, proposals and audit events.
- TradeLocker JWT login, account discovery, broker instrument discovery, historical candle retrieval, positions/orders access and order placement adapter.
- MetaTrader 5 Python adapter for account login, Market Watch symbols, candle retrieval, positions/orders and market order sending. The MT5 backend must run on Windows with the MetaTrader 5 terminal installed.
- RSI(14), volume and four-timeframe market-data collection.
- ChatGPT-strategy proposal inbox: only proposals submitted through `submit_trade_proposals` are approvable.
- Explanations are stored from the ChatGPT strategy conversation; the bridge does not fabricate replacement reasoning.
- Top 3 UI refreshes from the latest ChatGPT strategy submission.
- Mobile PWA with exact active platform/account number, top-3 proposals, EXP / APP / EXP+APP / REJECT workflow and broker connection forms.
- MCP endpoint at `/mcp` plus tool catalog at `/mcp-tools` so the same backend can be exposed to ChatGPT as a custom app when the account/product supports it.
- Encrypted broker credential storage and an audit log.

## Safety defaults

Real order transmission is OFF by default. `APP` records a simulated approval until `TRADING_EXECUTION_ENABLED=true` is set on the server. LIVE accounts have an additional independent lock and remain blocked unless `TRADING_LIVE_EXECUTION_ENABLED=true` is also set.

Start with demo accounts. Do not enable live execution until symbol sizing, broker contract sizes, minimum/step sizes, stop-distance rules and your risk limits have been validated for the exact broker account.

## Run locally

### Windows

Double-click `START_APP.bat`, then open `http://127.0.0.1:8080`.

### macOS / Linux

```bash
./start_app.sh
```

Then open `http://127.0.0.1:8080`.

## Phone use

For a phone on the same Wi-Fi network, run the backend on a computer and open `http://COMPUTER_LAN_IP:8080` from the phone. For reliable Add-to-Home-Screen/PWA installation outside localhost, host the app behind HTTPS.

## Connect TradeLocker

Open **Connect Broker** in the app and enter the TradeLocker email, password, broker server name and DEMO/LIVE environment. The backend logs in, discovers the available accounts, stores credentials encrypted, and adds exact account numbers to the account switcher.

TradeLocker credentials should only be entered into a server you control. Set a strong `TRADING_BRIDGE_SECRET` before using persistent real credentials.

## Connect MetaTrader 5

Run this backend on the Windows machine/VPS where the MT5 terminal is installed. Install the official `MetaTrader5` Python package there, then use **Connect Broker → MetaTrader 5**. The phone/browser frontend can still be used remotely.

## Environment variables

Copy `.env.example` values into your hosting provider's secret/environment settings.

```text
TRADING_BRIDGE_SECRET=<Fernet key>
TRADING_BRIDGE_DB=trading_bridge.db
PORT=8080
TRADING_EXECUTION_ENABLED=false
TRADING_LIVE_EXECUTION_ENABLED=false
```

Generate a Fernet key:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## Enable broker execution only after demo testing

```text
TRADING_EXECUTION_ENABLED=true
TRADING_LIVE_EXECUTION_ENABLED=false
```

This permits execution on connected non-LIVE accounts while retaining the live-account lock. Enabling `TRADING_LIVE_EXECUTION_ENABLED=true` removes the second lock; do this only after broker-specific validation.

## Docker (TradeLocker / PWA backend)

```bash
docker build -t ai-trading-bridge .
docker run --rm -p 8080:8080 \
  -e TRADING_BRIDGE_SECRET='YOUR_KEY' \
  -e TRADING_EXECUTION_ENABLED=false \
  -v "$PWD/data:/data" \
  ai-trading-bridge
```

MT5 is not intended to run in this Linux Docker image; use the Windows MT5 bridge host.

## ChatGPT tool endpoint

`POST /mcp` implements MCP initialize, tools/list and tools/call for:

- `get_active_account`
- `list_accounts`
- `select_account`
- `scan_everything`
- `get_chart_bundle`
- `approve_trade`
- `reject_trade`
- `create_alert`

The desired flow is: existing ChatGPT conversation → `scan_everything` → top 3 proposals → EXP/APP/EXP+APP/REJECT → guarded broker action.

## Important v1 limitations

- The bridge may include a technical-screen snapshot in scan output to help the AI inspect data, but it does not convert that snapshot into an approvable trade. The linked ChatGPT strategy conversation must make the trading decision.
- Automated lot/quantity sizing is not enabled because contract sizes, lot steps, tick values and broker rules vary. Approval requires an explicit quantity/volume.
- The MT5 v1 adapter sends market orders only. Pending-order support can be added after validating the broker's filling/time policies.
- Alerts are persisted but a background alert scheduler is not yet included.
- For a public internet deployment, add authentication for the web UI/API, HTTPS, rate limiting and a production secret manager before exposing it.


## v1.2 strategy workflow

1. The linked ChatGPT conversation calls `scan_everything`.
2. The bridge returns a `scanSessionId` plus broker/account identity and all requested timeframe data.
3. ChatGPT applies the trading rules and context already present in that conversation.
4. ChatGPT calls `submit_trade_proposals` with up to three ranked trades and its explanation for each.
5. The phone app displays those exact proposals. `EXP` reveals the stored ChatGPT explanation.
6. `APP` / `EXP + APP` can only approve a proposal whose `source` is `CHATGPT_STRATEGY`; server risk/execution locks still apply.

Important product limitation: the web app cannot inject a message into an arbitrary consumer ChatGPT conversation by itself. The existing ChatGPT conversation must have the Trading Bridge connected as a supported custom app/MCP tool and invoke these tools from that conversation.
