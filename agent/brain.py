import json
import os

from dotenv import load_dotenv
from openai import OpenAI

try:
    from .agent.tool_definitions import TOOLS
    from .tool_registry import get_tool
except ImportError:  # pragma: no cover - supports script execution
    from agent.tool_definitions import TOOLS  # type: ignore[import-not-found]
    from tool_registry import get_tool  # type: ignore[import-not-found]


# Load the API key from .env


# Load the API key from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found.")
    raise SystemExit

print("API key found!")


# Connect to OpenAI
client = OpenAI(api_key=api_key)


def ask_ai(user_message):
    response = client.responses.create(
        model="gpt-5.6",
        input=user_message,
        tools=TOOLS,
    )

    # Check whether the AI wants to use a tool
    tool_outputs = []

    for item in response.output:
        if item.type == "function_call":
            tool_name = item.name
            arguments = json.loads(item.arguments)

            tool_function = get_tool(tool_name)

            if tool_function is None:
                result = {
                    "error": f"Tool '{tool_name}' was not found."
                }
            else:
                try:
                    result = tool_function(**arguments)
                except (TypeError, ValueError, KeyError) as error:
                    result = {
                        "error": str(error)
                    }

            tool_outputs.append(
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(result),
                }
            )

    # If the AI used a tool, send the tool result back to the AI
    if tool_outputs:
        final_response = client.responses.create(
            model="gpt-5.6",
            previous_response_id=response.id,
            input=tool_outputs,
            tools=TOOLS,
        )

        return final_response.output_text

    return response.output_text


def main():
    print("=== My AI Brain ===")
    print("Type 'quit' to stop.")

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "quit":
            print("Goodbye!")
            break

        answer = ask_ai(user_message)

        print("AI:", answer)


if __name__ == "__main__":
    main()
