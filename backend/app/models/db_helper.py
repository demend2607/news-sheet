from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core import settings


class DatabaseHelper:
    def __init__(
            self,
            url: str,
            echo: bool = settings.db.echo,
            echo_pool: bool = settings.db.echo_pool,
            max_overflow: int = settings.db.max_overflow,
            pool_size: int = settings.db.pool_size,):
        self.engine = create_async_engine(
            url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow
        )

        self.async_session = async_sessionmaker(
            self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session() as session:
            yield session


db_helper = DatabaseHelper(
    url=str(settings.db.async_url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)
