import json
from datetime import datetime as dt
def read_file(filename: str) -> str:
    with open(filename) as f:
        data = f.read()
    
    return data

def to_dict(data: str) -> dict:
    try:
        numbers = json.loads(data)
    except json.decoder.JSONDecodeError:
        numbers = {
            "numbers": []
        }

    return numbers

def get_oldest(persons: list) -> dict:
    return min(persons, key=lambda person: dt.strptime(person["birthday"],"%Y-%m-%d"))

file_name = 'data.json'

data = read_file(file_name)
persons = to_dict(data)
print(get_oldest(persons))