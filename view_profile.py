import json

with open("profile.json", "r") as file:
    profile = json.load(file)

print("Name:", profile["name"])
print("Age:", profile["age"])
print("Country:", profile["country"])