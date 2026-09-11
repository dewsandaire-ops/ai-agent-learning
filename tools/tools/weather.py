import json
import urllib.error
import urllib.parse
import urllib.request


def get_weather(location):
    """Return current weather information for a location."""

    if not location or not str(location).strip():
        return "Please provide a location."

    location = str(location).strip()

    geocode_url = (
        "https://geocoding-api.open-meteo.com/v1/search?"
        + urllib.parse.urlencode(
            {
                "name": location,
                "count": 1,
                "language": "en",
                "format": "json",
            }
        )
    )

    geocode_request = urllib.request.Request(
        geocode_url,
        headers={
            "User-Agent": "AI-Agent-Learning/1.0"
        },
    )

    try:
        with urllib.request.urlopen(
            geocode_request,
            timeout=10,
        ) as response:
            geocode_data = json.loads(
                response.read().decode("utf-8")
            )

    except urllib.error.HTTPError as error:
        return (
            "Unable to get weather information: "
            f"HTTP error {error.code}."
        )

    except urllib.error.URLError as error:
        return (
            "Unable to get weather information: "
            f"{error.reason}."
        )

    except (json.JSONDecodeError, UnicodeDecodeError):
        return (
            "Unable to get weather information: "
            "invalid location data."
        )

    except TimeoutError:
        return (
            "Unable to get weather information: "
            "the request timed out."
        )

    except Exception as error:  # noqa: BLE001
        return (
            "Unable to get weather information: "
            f"{error}"
        )

    results = geocode_data.get("results", [])

    if not results:
        return f"Location not found: {location}"

    place = results[0]

    latitude = place.get("latitude")
    longitude = place.get("longitude")

    if latitude is None or longitude is None:
        return f"Coordinates unavailable for: {location}"

    place_name = place.get("name", location)
    country = place.get("country", "")

    weather_url = (
        "https://api.open-meteo.com/v1/forecast?"
        + urllib.parse.urlencode(
            {
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "apparent_temperature,"
                    "precipitation,"
                    "weather_code,"
                    "wind_speed_10m"
                ),
                "timezone": "auto",
            }
        )
    )

    weather_request = urllib.request.Request(
        weather_url,
        headers={
            "User-Agent": "AI-Agent-Learning/1.0"
        },
    )

    try:
        with urllib.request.urlopen(
            weather_request,
            timeout=10,
        ) as response:
            weather_data = json.loads(
                response.read().decode("utf-8")
            )

    except urllib.error.HTTPError as error:
        return (
            "Unable to get weather information: "
            f"HTTP error {error.code}."
        )

    except urllib.error.URLError as error:
        return (
            "Unable to get weather information: "
            f"{error.reason}."
        )

    except (json.JSONDecodeError, UnicodeDecodeError):
        return (
            "Unable to get weather information: "
            "invalid weather data."
        )

    except TimeoutError:
        return (
            "Unable to get weather information: "
            "the request timed out."
        )

    except Exception as error:  # noqa: BLE001
        return (
            "Unable to get weather information: "
            f"{error}"
        )

    current = weather_data.get("current", {})

    temperature = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")
    feels_like = current.get("apparent_temperature")
    precipitation = current.get("precipitation")
    wind_speed = current.get("wind_speed_10m")
    weather_code = current.get("weather_code")

    return (
        f"Current weather for {place_name}, {country}:\n"
        f"Temperature: {temperature}°C\n"
        f"Feels like: {feels_like}°C\n"
        f"Humidity: {humidity}%\n"
        f"Precipitation: {precipitation} mm\n"
        f"Wind speed: {wind_speed} km/h\n"
        f"Weather code: {weather_code}"
    )