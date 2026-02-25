from pydantic import BaseModel, HttpUrl
from datetime import datetime


class Incident(BaseModel):
    id: int
    title: str
    description: str | None
    date: datetime
    images: HttpUrl | None
    link: HttpUrl
    categories: str | None
    color: str | None
