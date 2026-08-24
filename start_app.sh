#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 -m venv .venv 2>/dev/null || true
. .venv/bin/activate
python -m pip install -q -r requirements.txt
exec python server.py
