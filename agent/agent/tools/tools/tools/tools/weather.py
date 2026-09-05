import urllib.request
import json


def weather(city):
    """Get current weather information for a city."""

    city = city.strip()

    if not city:
        return "Please provide a city."

    try:
        url = (
            "https://wttr.in/"
            + urllib.parse.quote(city)
            + "?format=j1"
        )

        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        current = data["current_condition"][0]

        return {
            "city": city,
            "temperature": current["temp_C"],
            "feels_like": current["FeelsLikeC"],
            "condition": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind_speed": current["windspeedKmph"],
        }

    except Exception as error:
        return f"Unable to get weather information: {error}"
