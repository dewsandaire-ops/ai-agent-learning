def calculator(a, b):
    return a + b


tools = {
    "calculator": calculator
}


def decide(request):
    if "add" in request.lower() or "plus" in request.lower():
        return {
            "tool": "calculator",
            "arguments": {
                "a": 25,
                "b": 17
            }
        }

    return None


user_request = input("What do you want me to do? ")

print("\n--- AGENT DECISION ---")

tool_call = decide(user_request)

if tool_call is None:
    print("I don't know how to handle that.")
else:
    print("Tool selected:", tool_call["tool"])

    print("\n--- TOOL EXECUTION ---")

    tool_name = tool_call["tool"]
    arguments = tool_call["arguments"]

    result = tools[tool_name](**arguments)

    print("Tool result:", result)

    print("\n--- AGENT OBSERVATION ---")

    print("The agent received:", result)

    print("\n--- FINAL ANSWER ---")

    print(f"The answer is {result}.")