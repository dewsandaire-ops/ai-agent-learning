import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Learning AI Agents",
    "body": "I am learning how APIs work.",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:", response.json())