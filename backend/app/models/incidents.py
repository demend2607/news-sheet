from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True, )
    title: Mapped[str] = mapped_column(String(500), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(
        Text, nullable=False)
    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, index=True)
    # date: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    images: Mapped[str | None] = mapped_column(String(500), nullable=False)
    link: Mapped[str] = mapped_column(
        String(500), unique=True, nullable=False, index=True
    )
    categories: Mapped[str | None] = mapped_column(String(50), nullable=False)
    color: Mapped[str | None] = mapped_column(String(50), nullable=True)
