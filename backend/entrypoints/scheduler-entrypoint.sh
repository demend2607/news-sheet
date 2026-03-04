#!/usr/bin/env sh
set -eu

PY_BIN="$(command -v python3 || command -v python || true)"
if [ -z "$PY_BIN" ]; then
  echo "[scheduler] python not found"
  exit 1
fi

cat > /tmp/scheduler.cron <<EOF
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
0 * * * * cd /app/app && PYTHONPATH=/app/app $PY_BIN -m services.incidents.sync_db >> /proc/1/fd/1 2>&1
EOF

crontab /tmp/scheduler.cron
echo "[scheduler] installed crontab:"
crontab -l

exec cron -f

