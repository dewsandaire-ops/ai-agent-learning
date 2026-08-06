import requests

response = requests.get(
    "https://randomuser.me/api/"
)

user = response.json()

print(user["results"][0]["name"]["first"])
print(user["results"][0]["email"])