tools = {
    "calculator": {
        "description": "Adds two numbers together.",
        "parameters": {
            "a": "first number",
            "b": "second number"
        }
    },

    "greeting": {
        "description": "Greets a person by name.",
        "parameters": {
            "name": "person's name"
        }
    }
}


for name, tool in tools.items():
    print("Tool:", name)
    print("Description:", tool["description"])
    print("Parameters:", tool["parameters"])
    print()