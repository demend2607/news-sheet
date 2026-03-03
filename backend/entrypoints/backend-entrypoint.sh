#!/usr/bin/env sh
set -e

echo "[backend] initial incidents sync..."
PYTHONPATH=/app/app python -m services.incidents.save_to_db || true
exec "$@"