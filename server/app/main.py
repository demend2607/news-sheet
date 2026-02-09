from fastapi import FastAPI
import json
from utils import get_incidents
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

app = FastAPI()

@app.get("/posts")
def get_home():
    incidents = get_incidents()
    incident = incidents[0]
        
    post = Incident.model_validate(incident)
    return {"data": post}

# @app.get("/students/{date}")
# def get_all_students_course(date: int):
#     incidents = get_incidents()
#     incident_data = incidents["date"][5:7]
#     return_list = []
#     for incident in incidents:
#         if incident["course"] == incident:
#             return_list.append(incident)
#     return return_list


