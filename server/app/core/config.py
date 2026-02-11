from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings

from dotenv import load_dotenv
import os

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


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080


class DatabaseConfig(BaseModel):
    url: str = ASYNC_DB_URL
    echo: bool = False,
    echo_pool: bool = False,
    pool_size = 10,
    max_overflow = 10


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
