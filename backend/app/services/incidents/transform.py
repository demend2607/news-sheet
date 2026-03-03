from datetime import datetime
from typing import Any

from .fetch import fetch_incidents

URL = 'https://www.dvnovosti.ru/ajax/v1/content/category/incidents/'


def incident_dict(story: dict[str, Any]) -> dict[str, Any]:
    publishedAt = story["publishedAt"]
    date_value = datetime.fromisoformat(publishedAt)
    images = story.get("images") or []
    image_url = None
    color = None
    if images and images[0].get("image"):
        image_obj = images[0]["image"]
        image_url = (image_obj.get("files") or {}).get("default")
        color = image_obj.get("color")

    categories = story.get("categories") or []
    category = categories[0]["slug"] if categories else None
    return {
        "id": story["id"],
        "title": story["title"],
        "description": story.get("lead"),
        "date": date_value,
        "images": image_url,
        "link": f"https://www.dvnovosti.ru/incidents/{publishedAt[0:4]}/{publishedAt[5:7]}/{publishedAt[8:10]}/{story['id']}/",
        "categories": category,
        "color": color,
    }


def prepare_rows() -> list[dict[str, Any]]:
    payload = fetch_incidents(URL)
    stories = payload.get("stories", [])
    rows: list[dict[str, Any]] = []

    for i, story in enumerate(stories, start=1):
        try:
            rows.append(incident_dict(story))
            print(f"[INFO] Prepared {i}/{len(stories)}")
        except Exception as exc:
            print(f"[WARN] Skip story id={story.get('id')} reason={exc}")

    return rows
