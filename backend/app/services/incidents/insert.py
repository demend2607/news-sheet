from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from models import Incident


async def insert_incidents(session: AsyncSession, rows: list[dict]) -> int:
    if not rows:
        return

    # stmt = insert(user_table).values(name="username", fullname="Full Username") # example
    insert_stmt = insert(Incident).values(rows)
    stmt = insert_stmt.on_conflict_do_nothing(index_elements=[Incident.id])

    result = await session.execute(stmt)

    await session.commit()
    return result.rowcount or 0
