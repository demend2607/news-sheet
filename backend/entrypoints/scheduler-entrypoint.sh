#!/usr/bin/env sh
set -e

printf '%s\n' \
'0 10 * * * cd /app/app && PYTHONPATH=/app/app python -m services.incidents.save_to_db >> /proc/1/fd/1 2>&1' \
| crontab -

echo "[scheduler] installed cron:"
crontab -l

exec cron -f