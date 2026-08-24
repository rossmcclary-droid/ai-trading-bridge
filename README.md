# AI Trading Bridge v1.3

A mobile-first PWA + FastAPI/MCP bridge for TradeLocker and MetaTrader 5. v1.3 adds an OpenAI API strategy brain initialized from `strategy_bootstrap.json`, which was exported from the existing AI Trading 5k funded ChatGPT conversation. The bridge collects 4H / 1H / 15M / 5M candles, volume and RSI; the API strategy applies those exported rules to rank zero to three A/A+ setups and generates the explanation attached to each proposal.

## What is real in v1.3

- Persistent SQLite database for connections, exact broker accounts, alerts, proposals and audit events.
- TradeLocker JWT login, account discovery, broker instrument discovery, historical candle retrieval, positions/orders access and order placement adapter.
- MetaTrader 5 Python adapter for account login, Market Watch symbols, candle retrieval, positions/orders and market order sending. The MT5 backend must run on Windows with the MetaTrader 5 terminal installed.
- RSI(14), volume and four-timeframe market-data collection.
- Bundled `strategy_bootstrap.json` containing the permanent strategy exported from the existing ChatGPT trading conversation.
- OpenAI Responses API strategy service. When `OPENAI_API_KEY` is configured, Scan Everything automatically sends the complete scan session to the bootstrapped strategy brain.
- The strategy may return zero to three proposals; only A/A+ setups are eligible. It is explicitly instructed not to force three trades.
- Each proposal stores the AI strategy explanation and response reference. EXP displays that exact explanation rather than generating separate local RSI text.
- The older MCP submission path remains available for a future direct ChatGPT custom-app connection.
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
OPENAI_API_KEY=<server-side OpenAI API key>
OPENAI_MODEL=gpt-5.6-terra
```

Generate a Fernet key:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## Enable broker execution only after demo testing

```text
TRADING_EXECUTION_ENABLED=true
TRADING_LIVE_EXECUTION_ENABLED=false
OPENAI_API_KEY=<server-side OpenAI API key>
OPENAI_MODEL=gpt-5.6-terra
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


## v1.3 Plus-compatible strategy workflow

Because a Plus consumer chat cannot currently be treated as an external API endpoint, v1.3 uses the exported strategy bootstrap as the persistent rules for a separate OpenAI API strategy session. This is intentionally labeled **Bootstrapped API strategy** in the app; it does not claim to be the literal consumer ChatGPT thread.

1. Press **Scan Everything**.
2. The bridge collects every broker-visible symbol with 4H / 1H / 15M / 5M candles, volume and RSI.
3. If `OPENAI_API_KEY` is configured, the server sends that scan plus `strategy_bootstrap.json` to the OpenAI Responses API.
4. The strategy returns zero to three A/A+ proposals. No clean setup is a valid result.
5. The phone app displays only those proposals.
6. **EXP** displays the explanation generated by the same strategy response that proposed the trade.
7. **APP / EXP+APP** still pass through the server execution locks. Live broker execution remains disabled by default.

If the original ChatGPT trading conversation learns or changes permanent rules later, export a new bootstrap and replace `strategy_bootstrap.json` so the API strategy stays synchronized with that conversation's framework.

## Add the OpenAI API key on Render

Never commit an API key to GitHub. Add it only in Render → service → Environment:

- `OPENAI_API_KEY` = your API project key
- `OPENAI_MODEL` = `gpt-5.6-terra` (default)

The API is billed separately from a ChatGPT Plus subscription. The `/health` and `/api/strategy/status` endpoints show whether the strategy key is configured without revealing the key.
