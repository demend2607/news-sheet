from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models import db_helper, Incident


router = APIRouter(prefix="/incidents")


async def get_db_session():
    async for session in db_helper.get_session():
        yield session


@router.get("/")
async def get_incidents(
    db: AsyncSession = Depends(get_db_session),
    day: int | None = Query(None, description="day"),
):
    query = select(Incident)

    if day:
        query = query.where(Incident.date.day == day)

    result = await db.execute(query)

    incidents = result.scalars().all()
    return incidents
