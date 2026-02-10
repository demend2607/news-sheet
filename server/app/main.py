from fastapi import FastAPI, Query
import json
from server.app.utils.utils import get_incidents
# --- 
from pydantic import BaseModel
from datetime import datetime

# --- schema
class Category(BaseModel):
    name: str
    slug: str
    
class Incident(BaseModel):
    id: int
    title: str
    description: str
    categories: list[Category]
    images: str
    # 
    link: str
    date: datetime
    color: str | None
# ---
class Incidents(BaseModel):
    # id: int
    incidents: list[Incident]

app = FastAPI()

@app.get("/posts/")
# def get_home():
#     incidents = get_incidents()
    
#     post = Incidents(incidents)
#     return {"data": post}


def get_posts_by_date(
    id: int | None = Query(None, description="ID"),
    year: int | None = Query(None, description="Год"),
    month: int | None = Query(None, description="Месяц"),
    day: int | None = Query(None, description="День")
):
    incidents = get_incidents()
    sorted_incidents = []
    
    for incident in incidents:
        date_obj = datetime.fromisoformat(incident["date"])
        match = True
        
        if id is not None and incident["id"] != id:
            match = False
        if year is not None and date_obj.year != year:
            match = False
        if month is not None and date_obj.month != month:
            match = False
        if day is not None and date_obj.day != day:
            match = False
        
        if match:
            sorted_incidents.append(incident)
    
    return {"data": sorted_incidents}
