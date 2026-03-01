from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=False)

    # Original value from source API (kept 1:1 for exact-match queries).
    date_raw: Mapped[str] = mapped_column(String(40), nullable=False, index=True)
    # Parsed datetime for SQL filtering/ranges/sorting.
    date_ts: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, index=True
    )

    images: Mapped[str | None] = mapped_column(String(500), nullable=False)
    link: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False, index=True
    )
    categories: Mapped[str | None] = mapped_column(String(20), nullable=False)
    color: Mapped[str | None] = mapped_column(String(50), nullable=True)
