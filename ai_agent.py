import os
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv
from openai import OpenAI


# Load API key
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found.")
    exit()

client = OpenAI(api_key=api_key)


# -------------------------
# TOOL 1: Calculator
# -------------------------

def calculator():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    operation = input("Choose +, -, *, or /: ")

    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 == 0:
            return "Cannot divide by zero."
        return number1 / number2
    else:
        return "Unknown operation."


# -------------------------
# TOOL 2: Greeting
# -------------------------

def greeting():
    name = input("What is your name? ")
    return f"Hello, {name}! Nice to meet you."


# -------------------------
# TOOL 3: Weather
# -------------------------

def weather():
    city = input("What city are you in? ")

    if city.lower() != "lagos":
        return "For now, I only have weather data for Lagos."

    latitude = 6.5244
    longitude = 3.3792

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

    return (
        f"The current temperature in Lagos is {temperature}°C, "
        f"with a wind speed of {wind_speed} km/h."
    )


# -------------------------
# TOOL 4: Current Time
# -------------------------

def current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")


# -------------------------
# TOOL REGISTRY
# -------------------------

tools = {
    "calculator": calculator,
    "greeting": greeting,
    "weather": weather,
    "current_time": current_time
}


# -------------------------
# AI BRAIN
# -------------------------

def ask_ai(user_message):
    response = client.responses.create(
        model="gpt-5.6",
        input=user_message
    )

    return response.output_text


# -------------------------
# AGENT
# -------------------------

def ai_agent():
    print("=== My AI Agent ===")
    print("Type 'quit' to stop.")

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "quit":
            print("Goodbye!")
            break

        answer = ask_ai(user_message)

        print("AI:", answer)


ai_agent()