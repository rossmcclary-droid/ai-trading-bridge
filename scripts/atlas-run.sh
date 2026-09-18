#!/usr/bin/env bash
set -e

cleanup() {
  kill "$API_PID" "$UI_PID" 2>/dev/null || true
}

trap cleanup EXIT INT TERM

cd ~/workspace/artifacts/api-server
python -m uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8080 &
API_PID=$!

cd ~/workspace/artifacts/mockup-sandbox
PORT=5173 BASE_PATH=/ pnpm exec vite \
  --host 0.0.0.0 \
  --port 5173 \
  --strictPort &
UI_PID=$!

echo "Atlas API PID: $API_PID"
echo "Atlas UI PID:  $UI_PID"
echo "Atlas AI Bridge running."

wait -n "$API_PID" "$UI_PID"

echo "One Atlas process stopped; shutting down both."
exit 1
