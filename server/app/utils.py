import json
import os
from datetime import datetime

path_to_json = os.path.join(os.path.dirname(__file__), 'parser/incidents.json')
def get_incidents():  
    try:
        with open(path_to_json, 'r', encoding='utf-8') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
            
            date = datetime.fromisoformat(dict_list[0]["date"])
            date_year = date.year
            print(date_year)
    
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None


if __name__ == '__main__':
    get_incidents()