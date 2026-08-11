import json

data = {
    "name": "Dews",
    "course": "AI Engineering",
    "level": "Beginner"
}

json_data = json.dumps(data)

python_data = json.loads(json_data)

print(python_data["name"])
print(python_data["course"])
print(python_data["level"])