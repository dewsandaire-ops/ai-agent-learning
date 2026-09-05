import json


def calculator(a, b):
    return a + b


tools = {
    "calculator": calculator
}


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))


tool_call = {
    "tool": "calculator",
    "arguments": {
        "a": first_number,
        "b": second_number
    }
}


print("\nGenerated tool call:")
print(json.dumps(tool_call, indent=4))


tool_name = tool_call["tool"]
arguments = tool_call["arguments"]

result = tools[tool_name](**arguments)


print("\nTool result:", result)