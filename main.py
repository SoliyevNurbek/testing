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


def get_sum(numbers: list) -> int:
    return sum(numbers)

file_name = 'data.txt'

data = read_file(file_name)
numbers = to_dict(data)
print(get_sum(numbers['numbers']))