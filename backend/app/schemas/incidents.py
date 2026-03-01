from datetime import datetime
from pydantic import BaseModel, ConfigDict, HttpUrl


class Incident(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    date_raw: str
    date_ts: datetime
    images: HttpUrl
    link: HttpUrl
    categories: str | None
    color: str | None
