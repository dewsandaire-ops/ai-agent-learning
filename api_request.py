import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("Post ID:", data["id"])
        print("Title:", data["title"])

    else:
        print("API request failed.")
        print("Status code:", response.status_code)

except requests.RequestException as error:
    print("Could not connect to the API.")
    print("Error:", error)