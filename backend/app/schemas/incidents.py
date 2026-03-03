from datetime import datetime
from pydantic import BaseModel, ConfigDict, HttpUrl


class IncidentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str | None
    date: str
    images: HttpUrl | None
    link: HttpUrl
    categories: str | None
    color: str | None
