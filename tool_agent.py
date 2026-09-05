import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found.")
    exit()

client = OpenAI(api_key=api_key)


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
    else:
        return "Unknown operation."


tools = [
    {
        "type": "function",
        "name": "calculator",
        "description": "Performs a mathematical calculation using two numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "number1": {
                    "type": "number",
                    "description": "The first number."
                },
                "number2": {
                    "type": "number",
                    "description": "The second number."
                },
                "operation": {
                    "type": "string",
                    "enum": ["+", "-", "*", "/"],
                    "description": "The mathematical operation."
                }
            },
            "required": ["number1", "number2", "operation"],
            "additionalProperties": False
        }
    }
]


def run_agent(user_message):

    response = client.responses.create(
        model="gpt-5.6-luna",
        tools=tools,
        input=user_message
    )

    for item in response.output:

        if item.type == "function_call":

            print("AI chose the calculator tool.")

            arguments = item.arguments

            import json

            args = json.loads(arguments)

            result = calculator(
                args["number1"],
                args["number2"],
                args["operation"]
            )

            print("Tool result:", result)

            return result

    return response.output_text


def main():

    print("=== My First Tool-Calling AI Agent ===")
    print("Type 'quit' to stop.")

    while True:

        user_message = input("\nYou: ")

        if user_message.lower() == "quit":
            print("Goodbye!")
            break

        answer = run_agent(user_message)

        print("Agent:", answer)


main()