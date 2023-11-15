import json

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
    return max(persons, key=lambda person: person['age'])

file_name = 'data.json'

data = read_file(file_name)
persons = to_dict(data)
print(get_oldest(persons))