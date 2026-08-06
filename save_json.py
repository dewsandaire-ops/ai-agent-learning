import json

student = {
    "name": "Dews",
    "course": "Python",
    "country": "Nigeria"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Saved!")