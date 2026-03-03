from typing import Any

import requests


HTTPS_HEAD = {
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://www.dvnovosti.ru/incidents/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
}


def fetch_incidents(url) -> dict[str, Any]:
    with requests.Session() as session:
        session.headers.update({
            "accept": HTTPS_HEAD['accept'],
            "referer": HTTPS_HEAD['referer'],
            "user-agent": HTTPS_HEAD['user-agent'],
        })
        response = session.get(url, timeout=20)
        response.raise_for_status()
        return response.json()
