from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from core.config import settings
from dotenv import load_dotenv
import os

load_dotenv()

DB = {
    "user": os.getenv("DB_USER"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "name": os.getenv("DB_NAME"),
    "password": os.getenv("DB_PASSWORD")
}

ASYNC_DB_URL = f"postgresql+asyncpg://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['name']}"
# sync db for alembic migrations
SYNC_DB_URL = f"postgresql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['name']}"


class DatabaseHelper:
    def __init__(
            self,
            url: str = ASYNC_DB_URL,
            echo: bool = False,
            echo_pool: bool = False,
            max_overflow: int = 10,
            pool_size: int = 10):
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

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self):
        async with self.async_session() as session:
            yield session


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)
