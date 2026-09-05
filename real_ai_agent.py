import os
import json
from datetime import datetime

import requests
from dotenv import load_dotenv
from openai import OpenAI


# -----------------------------
# LOAD API KEY
# -----------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found.")
    exit()

client = OpenAI(api_key=api_key)


# -----------------------------
# TOOLS
# -----------------------------

def calculator(number1, number2, operation):
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

    return "Unknown operation."


def current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")


def greeting(name):
    return f"Hello, {name}! Nice to meet you."


def weather(city):
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

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    data = response.json()

    temperature = data["current"]["temperature_2m"]
    wind_speed = data["current"]["wind_speed_10m"]

    return (
        f"The current temperature in Lagos is "
        f"{temperature}°C, with a wind speed of "
        f"{wind_speed} km/h."
    )


# -----------------------------
# TOOL DEFINITIONS
# -----------------------------

tools = [
    {
        "type": "function",
        "name": "calculator",
        "description": "Perform a mathematical calculation.",
        "parameters": {
            "type": "object",
            "properties": {
                "number1": {
                    "type": "number"
                },
                "number2": {
                    "type": "number"
                },
                "operation": {
                    "type": "string",
                    "enum": ["+", "-", "*", "/"]
                }
            },
            "required": [
                "number1",
                "number2",
                "operation"
            ],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "current_time",
        "description": "Get the current local time.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "greeting",
        "description": "Greet a person by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                }
            },
            "required": ["name"],
            "additionalProperties": False
        }
    },

    {
        "type": "function",
        "name": "weather",
        "description": "Get the current weather for Lagos.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string"
                }
            },
            "required": ["city"],
            "additionalProperties": False
        }
    }
]


# -----------------------------
# RUN THE CORRECT TOOL
# -----------------------------

def run_tool(tool_name, arguments):

    if tool_name == "calculator":
        return calculator(
            arguments["number1"],
            arguments["number2"],
            arguments["operation"]
        )

    elif tool_name == "current_time":
        return current_time()

    elif tool_name == "greeting":
        return greeting(
            arguments["name"]
        )

    elif tool_name == "weather":
        return weather(
            arguments["city"]
        )

    return "Unknown tool."


# -----------------------------
# AI AGENT
# -----------------------------

def run_agent(user_message):

    response = client.responses.create(
        model="gpt-5.6-luna",
        tools=tools,
        input=user_message
    )

    tool_outputs = []

    for item in response.output:

        if item.type == "function_call":

            print(f"\nAI selected tool: {item.name}")

            arguments = json.loads(item.arguments)

            result = run_tool(
                item.name,
                arguments
            )

            print("Tool result:", result)

            tool_outputs.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": str(result)
            })

    if tool_outputs:

        response = client.responses.create(
            model="gpt-5.6-luna",
            tools=tools,
            previous_response_id=response.id,
            input=tool_outputs
        )

    return response.output_text


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():

    print("=== My Real AI Agent ===")
    print("Type 'quit' to stop.")

    while True:

        user_message = input("\nYou: ")

        if user_message.lower() == "quit":
            print("Goodbye!")
            break

        answer = run_agent(user_message)

        print("Agent:", answer)


main()