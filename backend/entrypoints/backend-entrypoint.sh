#!/usr/bin/env sh
set -e

echo "[backend] initial incidents sync..."
PYTHONPATH=/app/app python -m services.incidents.sync_db || true
exec "$@"