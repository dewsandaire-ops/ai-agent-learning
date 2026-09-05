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
# PERMANENT MEMORY
# =========================

MEMORY_FILE = "agent_memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


# =========================
# TOOLS
# =========================

def calculator(number1, number2, operation):
    if operation == "+":
        return number1 + number2

    if operation == "-":
        return number1 - number2

    if operation == "*":
        return number1 * number2

    if operation == "/":
        if number2 == 0:
            return "Cannot divide by zero."

        return number1 / number2

    return "Unknown operation."


def current_time():
    return datetime.now().strftime("%I:%M %p")


def greeting(name):
    return f"Hello, {name}! Nice to meet you."


def weather(city):
    if city.lower() != "lagos":
        return "For now, I only have weather data for Lagos."

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 6.5244,
        "longitude": 3.3792,
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
                "number1": {"type": "number"},
                "number2": {"type": "number"},
                "operation": {
                    "type": "string",
                    "enum": ["+", "-", "*", "/"]
                }
            },
            "required": ["number1", "number2", "operation"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "current_time",
        "description": "Get the current time.",
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
                "name": {"type": "string"}
            },
            "required": ["name"],
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
                "city": {"type": "string"}
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

    if name == "calculator":
        return calculator(
            arguments["number1"],
            arguments["number2"],
            arguments["operation"]
        )

    if name == "current_time":
        return current_time()

    if name == "greeting":
        return greeting(arguments["name"])

    if name == "weather":
        return weather(arguments["city"])

    return "Unknown tool."


# =========================
# AI
# =========================

def run_agent(conversation):

    response = client.responses.create(
        model="gpt-5.6-luna",
        tools=tools,
        input=conversation
    )

    tool_outputs = []

    for item in response.output:

        if item.type == "function_call":

            print(f"\nTool selected: {item.name}")

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

    return response


# =========================
# MAIN
# =========================

def main():

    print("=== My AI Agent With Permanent Memory ===")
    print("Type 'quit' to stop.")

    memory = load_memory()

    conversation = memory.copy()

    while True:

        user_message = input("\nYou: ")

        if user_message.lower() == "quit":
            save_memory(conversation)
            print("Memory saved.")
            print("Goodbye!")
            break

        conversation.append({
            "role": "user",
            "content": user_message
        })

        response = run_agent(conversation)

        answer = response.output_text

        print("Agent:", answer)

        conversation.append({
            "role": "assistant",
            "content": answer
        })

        save_memory(conversation)


main()