#!/usr/bin/env sh
set -eu

cat > /tmp/scheduler.cron <<EOF
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PYTHONPATH=/app/app
DB__ASYNC_URL=${DB__ASYNC_URL}
DB__SYNC_URL=${DB__SYNC_URL}
0 * * * * cd /app/app && /usr/local/bin/python -m services.incidents.sync_db >> /proc/1/fd/1 2>&1
EOF

crontab /tmp/scheduler.cron
crontab -l
exec cron -f
