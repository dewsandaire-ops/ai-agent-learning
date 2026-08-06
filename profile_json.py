import json

profile = {
    "name": input("Name: "),
    "age": int(input("Age: ")),
    "country": input("Country: ")
}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

print("Profile saved.")