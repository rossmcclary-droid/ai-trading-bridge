# Challenge benchmark harness

This workflow provides a narrow replacement for the inaccessible Replit runtime. It runs only from a push to `bridge-replit-live-snapshot-001` whose head commit message contains `[bridge-benchmark-one-shot]`. It never targets or updates `main`.

The `bridge-benchmark` GitHub environment must hold the TradeLocker credentials. Configure any required environment approval there. The workflow checks accepted commit `fcba5a6383f191668c3ad31eee8999b3d495b9eb` as an ancestor and verifies the hashes of the accepted backend patch before any provider-capable job begins. A separate job compiles the backend and runs the 14 pre-benchmark safety tests without secrets.

The benchmark program starts the API locally, makes exactly one `POST /api/scan/Challenge/export-ai/start`, validates the returned 32-character lowercase hexadecimal job ID, and polls only that exact ID. It never retries or restarts the POST. A FAILED job, HTTP 429, unexpected status, invalid ID, or timeout stops the run.

API readiness uses a separate clock. Benchmark wall time and the export deadline both begin immediately before the sole start POST, so runner startup is not misreported as provider/export latency.

Only a sanitized JSON summary is retained for three days. Server logs and the full market/account package are not uploaded.

## Secure configuration

Required environment secrets:

- `TRADELOCKER_DEMO_EMAIL`
- `TRADELOCKER_DEMO_PASSWORD`
- `TRADELOCKER_DEMO_SERVER`

Optional environment secret:

- `TRADELOCKER_DEVELOPER_API_KEY`

The established TradeLocker demo base URL is supplied as non-secret workflow configuration.

MatchTrader secrets are intentionally not requested. The Challenge export treats MatchTrader cross-reference as optional, explicitly marks its failure as non-blocking, and the benchmark is for TradeLocker discovery/deep-analysis completeness. Omitting those credentials also avoids an unrelated external provider call.

The workflow does not alter the frontend, backups, existing durable job evidence, or any production service. GitHub-hosted runner storage is ephemeral.
