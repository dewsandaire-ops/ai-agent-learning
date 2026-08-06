import requests

response = requests.get(
    "https://api.quotable.io/random"
)

if response.status_code == 200:
    quote = response.json()
    print(quote["content"])
    print("- " + quote["author"])
else:
    print("Could not retrieve a quote.")