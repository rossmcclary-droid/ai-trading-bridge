# Put AI Trading Bridge on the web (test setup)

This package is ready to deploy as a Render Web Service using the included `render.yaml` and `Dockerfile`.

## Recommended test path

1. Create a free GitHub repository named `ai-trading-bridge`.
2. Upload the **contents of this folder** to the repository root (not the outer ZIP).
3. Sign in to Render and choose **New > Blueprint**.
4. Connect the GitHub repository.
5. Render detects `render.yaml`. Create the service.
6. After deployment finishes, Render gives you an HTTPS address ending in `.onrender.com`.
7. Open that address in Chrome on Android.
8. In Chrome, use **Add to Home screen** / **Install app**.

The initial hosted app uses simulated accounts until you connect a broker. Broker order execution is disabled by default.

## Safety switches

These are intentionally set in `render.yaml`:

- `TRADING_EXECUTION_ENABLED=false`
- `TRADING_LIVE_EXECUTION_ENABLED=false`

Do not change them during initial testing.

## Free-hosting limitation

The free Render web service can sleep when idle and its local filesystem is ephemeral. This is suitable for UI and workflow testing. Before storing broker credentials for ongoing use, move to persistent storage (paid disk or external database) and keep the encryption secret stable.
