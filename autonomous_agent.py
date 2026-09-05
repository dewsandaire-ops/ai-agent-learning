import os
import json
from datetime import datetime

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
    }
]


# =========================
# RUN TOOLS
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

    return "Unknown tool."


# =========================
# AGENT LOOP
# =========================

def run_agent(goal):

    response = client.responses.create(
        model="gpt-5.6-luna",
        tools=tools,
        input=goal
    )

    while True:

        tool_outputs = []

        for item in response.output:

            if item.type == "function_call":

                print(f"\nAI selected: {item.name}")

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

        if not tool_outputs:
            return response.output_text

        response = client.responses.create(
            model="gpt-5.6-luna",
            tools=tools,
            previous_response_id=response.id,
            input=tool_outputs
        )


# =========================
# MAIN
# =========================

def main():

    print("=== My Autonomous AI Agent ===")
    print("Type 'quit' to stop.")

    while True:

        goal = input("\nGive the agent a task: ")

        if goal.lower() == "quit":
            print("Goodbye!")
            break

        answer = run_agent(goal)

        print("\nAgent:", answer)


main()