import requests
from datetime import datetime


def calculator():
    print("Calculator tool selected.")

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    operation = input("Choose +, -, *, or /: ")

    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print("Cannot divide by zero.")
            return
        result = number1 / number2
    else:
        print("Unknown operation.")
        return

    print("Result:", result)


def greeting():
    name = input("What is your name? ")
    return f"Hello, {name}! Nice to meet you."


def weather():
    city = input("What city are you in? ")

    if city.lower() == "lagos":
        latitude = 6.5244
        longitude = 3.3792
    else:
        print("For now, I only have weather data set up for Lagos.")
        return

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"
    }

    response = requests.get(url, params=params, timeout=20)
    data = response.json()

    temperature = data["current"]["temperature_2m"]
    wind_speed = data["current"]["wind_speed_10m"]

    return f"The current temperature in Lagos is {temperature}°C, with a wind speed of {wind_speed} km/h."


def current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")


tools = {
    "calculator": calculator,
    "greeting": greeting,
    "weather": weather,
    "current_time": current_time
}


def mini_agent():
    print("=== My First Mini AI Agent ===")
    print("Type 'quit' when you want to stop.")

    while True:
        user_request = input("\nWhat do you want me to do? ")
        request = user_request.lower()
        words = request.replace("?", "").replace(",", "").split()

        if request == "quit":
            print("Goodbye!")
            break

        if any(word in words for word in ["calculate", "add", "subtract", "multiply", "divide"]):
            print("I understand that you want to calculate something.")
            tools["calculator"]()

        elif any(word in words for word in ["greet", "hello", "hi", "greeting"]):
            print("I understand that you want a greeting.")
            result = tools["greeting"]()
            print("Tool used: greeting")
            print("Result:", result)

        elif any(word in words for word in ["weather", "temperature", "hot", "cold"]):
            print("I understand that you want weather information.")
            result = tools["weather"]()

            if result:
                print("Tool used: weather")
                print("Result:", result)

        elif any(word in words for word in ["time", "clock"]):
            result = tools["current_time"]()
            print("Tool used: current_time")
            print("Result:", result)

        else:
            print("I don't know how to handle that task yet.")


mini_agent()