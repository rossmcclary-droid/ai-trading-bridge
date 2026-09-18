# AI Trading Bridge

Read-only FastAPI backend for safely observing trading account data, with extension points for TradeLocker and Match-Trader.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the FastAPI server (port 8080)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `python -m compileall -q artifacts/api-server/app` — validate Python bytecode compilation

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Python + FastAPI + Uvicorn
- Broker boundary: read-only `ReadOnlyConnector` interface
- API codegen: Orval (from OpenAPI spec)

## Where things live

- `artifacts/api-server/app/main.py` — FastAPI application entrypoint
- `artifacts/api-server/app/routes/health.py` — `/health` contract
- `artifacts/api-server/app/connectors/base.py` — read-only broker interface
- `artifacts/api-server/app/connectors/tradelocker.py` — TradeLocker connector placeholder
- `artifacts/api-server/app/connectors/match_trader.py` — Match-Trader connector placeholder
- `lib/api-spec/openapi.yaml` — API contract source of truth

## Architecture decisions

- The backend is intentionally Python/FastAPI even though the surrounding workspace includes TypeScript services.
- Connector interfaces expose observation-only methods; trade execution methods are deliberately absent.
- Broker implementations remain unconfigured placeholders until provider credentials and API details are supplied.

## Product

The bridge currently exposes service health and establishes a safe foundation for future read-only account, balance, position, order, and market-data access.

## User preferences

The bridge must remain read-only for this phase: never place, modify, or close trades.

## Gotchas

- The proxied health URL is `/api/health`; the application route itself is `/health`.
- Run API codegen after changing `lib/api-spec/openapi.yaml`.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
