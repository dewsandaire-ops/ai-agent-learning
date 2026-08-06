import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Learning Python",
    "body": "I am becoming an AI Engineer.",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())