import json


def decide(request):
    request = request.lower()

    if "add" in request or "plus" in request or "sum" in request:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        return {
            "tool": "calculator",
            "arguments": {
                "a": first_number,
                "b": second_number
            }
        }

    return None


def calculator(a, b):
    return a + b


tools = {
    "calculator": calculator
}


user_request = input("What do you want me to do? ")

tool_call = decide(user_request)

if tool_call is None:
    print("I don't know how to handle that request.")

else:
    print("\nAgent decision:")
    print(json.dumps(tool_call, indent=4))

    tool_name = tool_call["tool"]
    arguments = tool_call["arguments"]

    result = tools[tool_name](**arguments)

    print("\nTool result:", result)