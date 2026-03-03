#!/usr/bin/env sh
set -e

# root user crontab: удобно проверять через `crontab -l`
# sh -c "echo '0 10 * * * root cd /app/app && PYTHONPATH=/app/app python -m services.incidents.sync_db >> /proc/1/fd/1 2>&1' > /etc/cron.d/parser-job && chmod 0644 /etc/cron.d/parser-job && cron -f"
printf '%s\n' \
'0 10 * * * cd /app/app && PYTHONPATH=/app/app python -m services.incidents.save_to_db >> /proc/1/fd/1 2>&1' \
| crontab -

echo "[scheduler] installed cron:"
crontab -l

exec cron -f