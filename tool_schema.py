import json


calculator_schema = {
    "name": "calculator",
    "description": "Adds two numbers together.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {
                "type": "number",
                "description": "The first number."
            },
            "b": {
                "type": "number",
                "description": "The second number."
            }
        },
        "required": ["a", "b"]
    }
}


print(json.dumps(calculator_schema, indent=4))