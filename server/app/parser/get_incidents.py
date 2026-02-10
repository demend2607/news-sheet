from bs4 import BeautifulSoup
import requests

import os
import json
import time
import random
from datetime import datetime

cookies = {
    '_ga': 'GA1.1.1446923521.1769143658',
    '_ga_J9N3D9YFK9': 'GS2.1.s1770271791$o8$g1$t1770272584$j29$l0$h0$dmPA7HMywgvDN5PaPPs0wpKFkNQPTVgLMUw',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://www.dvnovosti.ru/incidents/',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.1446923521.1769143658; _ga_J9N3D9YFK9=GS2.1.s1770271791$o8$g1$t1770272584$j29$l0$h0$dmPA7HMywgvDN5PaPPs0wpKFkNQPTVgLMUw',
}

script_dir = os.path.dirname(os.path.abspath(__file__))

def get_raw_data():
    s = requests.Session()
    try:
        responce = s.get('https://www.dvnovosti.ru/ajax/v1/content/category/incidents/', cookies=cookies, headers=headers)
        data = responce.json()
        with open(script_dir + '/raw_incidents.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return "[INFO] Raw data collected successfully"
    except:
        data = None
        return "error"
    
    
    

def prepare_data():
    with open(script_dir + '/raw_incidents.json', 'r', encoding='utf-8') as file:
        raw_data = json.load(file)
        
    stories = raw_data['stories']
    data_for_db = []
    iteraction = 0
    try:
        for story in stories:
            # dvnovosti.ru/incidents/2026/02/05/190424/
            publishedAt = story['publishedAt']
            link = "https://www.dvnovosti.ru/incidents/" + publishedAt[0:4] + "/" + publishedAt[5:7] + "/" + publishedAt[8:10] + "/" + str(story['id']) + "/"
            data_for_db.append({
                "id": story['id'],
                'title': story['title'],
                'description': story['lead'],
                'date': publishedAt,
                'images': story['images'][0]["image"]["files"]["default"],
                "link": link,
                'categories': story['categories'],
                'color': story['images'][0]['image']['color'],})  
            
            iteraction += 1
            print(f'[INFO] Collecting data {iteraction}/{len(stories)}')  
            
        with open(script_dir + '/incidents.json', 'w', encoding='utf-8') as file:
            json.dump(data_for_db, file, indent=4, ensure_ascii=False)
        return "[INFO] Data collected successfully"
    except Exception as e:
        return f"error: {e}"

    

def main():
    with open(script_dir + '/scheduler.txt', 'a', encoding='utf-8') as file:
        file.write(f'Запущено get_incidents🔄: {datetime.now().strftime("%d.%m.%Y %H:%M")}\n')
    print(get_raw_data())
    print(prepare_data())
    with open(script_dir + '/scheduler.txt', 'a', encoding='utf-8') as file:
        file.write(f'Завершено get_incidents✅: {datetime.now().strftime("%d.%m.%Y %H:%M")}\n\n')


if __name__ == '__main__':
    main()