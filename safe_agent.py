import os
import json
from datetime import datetime

import requests
from dotenv import load_dotenv
from openai import OpenAI


# =========================
# SETUP
# =========================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found.")
    exit()

client = OpenAI(api_key=api_key)


# =========================
# TOOLS
# =========================

def calculator(number1, number2, operation):
    try:
        if operation == "+":
            return number1 + number2

        if operation == "-":
            return number1 - number2

        if operation == "*":
            return number1 * number2

        if operation == "/":
            if number2 == 0:
                return "Error: Cannot divide by zero."

            return number1 / number2

        return "Error: Unknown operation."

    except Exception as error:
        return f"Calculator error: {error}"


def current_time():
    try:
        return datetime.now().strftime("%I:%M %p")

    except Exception as error:
        return f"Time error: {error}"


def weather(city):
    try:
        if city.lower() != "lagos":
            return "For now, I only have weather data for Lagos."

        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": 6.5244,
            "longitude": 3.3792,
            "current": "temperature_2m,wind_speed_10m"
        }

        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        temperature = data["current"]["temperature_2m"]
        wind_speed = data["current"]["wind_speed_10m"]

        return (
            f"The current temperature in Lagos is "
            f"{temperature}°C, with a wind speed of "
            f"{wind_speed} km/h."
        )

    except requests.RequestException:
        return "Weather service is currently unavailable."

    except Exception as error:
        return f"Weather error: {error}"


# =========================
# TOOL DEFINITIONS
# =========================

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
        "name": "weather",
        "description": "Get current weather information for Lagos.",
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


# =========================
# TOOL RUNNER
# =========================

def run_tool(name, arguments):

    try:

        if name == "calculator":
            return calculator(
                arguments["number1"],
                arguments["number2"],
                arguments["operation"]
            )

        if name == "current_time":
            return current_time()

        if name == "weather":
            return weather(
                arguments["city"]
            )

        return "Error: Unknown tool."

    except KeyError as error:
        return f"Error: Missing tool argument {error}"

    except Exception as error:
        return f"Tool error: {error}"


# =========================
# AGENT
# =========================

def run_agent(user_message):

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            tools=tools,
            input=user_message
        )

        while True:

            tool_outputs = []

            for item in response.output:

                if item.type == "function_call":

                    print(f"\nTool selected: {item.name}")

                    try:
                        arguments = json.loads(item.arguments)

                        result = run_tool(
                            item.name,
                            arguments
                        )

                    except json.JSONDecodeError:
                        result = "Error: The tool arguments were invalid."

                    print("Tool result:", result)

                    tool_outputs.append({
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result)
                    })

            if not tool_outputs:
                return response.output_text

            response = client.responses.create(
                model="gpt-5.6-luna",
                tools=tools,
                previous_response_id=response.id,
                input=tool_outputs
            )

    except Exception as error:
        return f"Agent error: {error}"


# =========================
# MAIN
# =========================

def main():

    print("=== My Safe AI Agent ===")
    print("Type 'quit' to stop.")

    while True:

        user_message = input("\nYou: ")

        if user_message.lower() == "quit":
            print("Goodbye!")
            break

        answer = run_agent(user_message)

        print("\nAgent:", answer)


main()