from typing import Any

import requests


COOKIES = {
    '_ga': 'GA1.1.1446923521.1769143658',
    '_ga_J9N3D9YFK9': 'GS2.1.s1770271791$o8$g1$t1770272584$j29$l0$h0$dmPA7HMywgvDN5PaPPs0wpKFkNQPTVgLMUw',
}

HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.7',
    'referer': 'https://www.dvnovosti.ru/incidents/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.1446923521.1769143658; _ga_J9N3D9YFK9=GS2.1.s1770271791$o8$g1$t1770272584$j29$l0$h0$dmPA7HMywgvDN5PaPPs0wpKFkNQPTVgLMUw',
}


def fetch_incidents(url) -> dict[str, Any]:
    with requests.Session() as session:
        response = session.get(url, headers=HEADERS,
                               cookies=COOKIES, timeout=20)
        response.raise_for_status()
        return response.json()
