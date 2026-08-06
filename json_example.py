import json

person = {
    "name": "John",
    "age": 25,
    "country": "Nigeria"
}

json_data = json.dumps(person)

print(json_data)