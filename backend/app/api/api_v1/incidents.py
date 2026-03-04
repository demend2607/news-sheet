from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import asc, desc, select

from core.config import settings
from models import db_helper, Incident

router = APIRouter(prefix=settings.api.v1.incidents, tags=["Incidents"])


async def get_db_session():
    async for session in db_helper.get_session():
        yield session


@router.get("")
async def get_incidents(
    db: AsyncSession = Depends(get_db_session),
    limit: int = Query(30, ge=1, le=100),
    offset: int = Query(0, ge=0),
    sort_by: str = Query(
        "date", description="Поле для сортировки (date, id, title)"),
    order: str = Query("desc", description="Направление: asc или desc"),
):

    allowed_fields = {"date", "id", "title"}
    if sort_by not in allowed_fields:
        raise HTTPException(
            status_code=400, detail=f"sort_by must be one of {allowed_fields}")

    order_func = desc if order.lower() == "desc" else asc

    query = select(Incident).order_by(order_func(
        getattr(Incident, sort_by))).limit(limit).offset(offset)

    result = await db.execute(query)
    incidents = result.scalars().all()
    return incidents
    return incidents_result


@router.get("/{id}")
async def get_incident_by_id(
    id: int,
    db: AsyncSession = Depends(get_db_session),
):
    incident = await db.get(Incident, id)

    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")

    return incident
