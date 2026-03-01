from typing import Any
import json

import asyncio

from models import db_helper
from .transform import prepare_rows
from .insert import insert_incidents


def write_json_snapshot(rows: list[dict[str, Any]]) -> None:
    # datetime в JSON напрямую не сериализуется, переводим в ISO-строку.
    payload = [{**r, "date_ts": r["date_ts"].isoformat()} for r in rows]
    with open('services/incidents/incidents.json', "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=4, ensure_ascii=False)


async def save_to_db(rows: list[dict]) -> int:
    async for session in db_helper.get_session():
        return await insert_incidents(session, rows)
    return 0


def incidents_sync_db():
    rows = prepare_rows()
    write_json_snapshot(rows)  # optional json snapshot
    inserted = asyncio.run(save_to_db(rows))
    print(f"[INFO] DB affected rows: {inserted}")


if __name__ == "__main__":
    incidents_sync_db()
