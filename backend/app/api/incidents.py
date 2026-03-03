from datetime import datetime
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, extract

from models import db_helper, Incident

import logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/incidents")


async def get_db_session():
    async for session in db_helper.get_session():
        yield session


@router.get("/")
async def get_incidents(
    db: AsyncSession = Depends(get_db_session),
    month: int | None = Query(None, description="Month", ge=1, le=12),
):
    # "date": "2026-03-03T10:02:00+10:00", how extract datetime?
    # dt = datetime.fromisoformat('month', "2026-03-03T10:02:00+10:00")
    query = select(Incident).order_by(Incident.date.desc()).limit(20)
    if month:
        query = query.filter(extract("month", Incident.date) == month)

    query_result = await db.execute(query)
    incidents_result = query_result.scalars().all()
    if incidents_result == []:
        return {f'No incidents found in month: {month}'}
    return incidents_result


@router.get("/{day}/")
async def get_incident(
    # id: int,
    day: int,
    db: AsyncSession = Depends(get_db_session),
):
    # "date_raw": "2026-03-02T15:15:00+10:00",
    # "date_ts": "2026-03-02T15:15:00+10:00",
    query = select(Incident).where(Incident.date == day)
    result = await db.execute(query)
    incident = result.scalars().one_or_none()

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    return incident
