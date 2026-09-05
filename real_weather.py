import requests


city = input("Enter a city: ")

geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

geocoding_params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

response = requests.get(geocoding_url, params=geocoding_params)

data = response.json()

if "results" not in data:
    print("City not found.")
else:
    location = data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]
    city_name = location["name"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params
    )

    weather_data = weather_response.json()

    current = weather_data["current"]

    print()
    print("City:", city_name)
    print("Temperature:", current["temperature_2m"], "°C")
    print("Wind speed:", current["wind_speed_10m"], "km/h")