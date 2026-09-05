def calculator(a, b):
    return a + b


def greeting(name):
    return f"Hello, {name}!"


def choose_tool(request):
    request = request.lower()

    if any(word in request for word in ["add", "sum", "plus", "calculate"]):
        return "calculator"

    if any(word in request for word in ["hello", "hi", "greet"]):
        return "greeting"

    return None


tools = {
    "calculator": calculator,
    "greeting": greeting
}


user_request = input("What do you want me to do? ")

selected_tool = choose_tool(user_request)

if selected_tool is None:
    print("I don't know which tool to use.")

elif selected_tool == "calculator":
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    result = tools[selected_tool](first_number, second_number)

    print("Selected tool:", selected_tool)
    print("Result:", result)

elif selected_tool == "greeting":
    name = input("What is your name? ")

    result = tools[selected_tool](name)

    print("Selected tool:", selected_tool)
    print("Result:", result)