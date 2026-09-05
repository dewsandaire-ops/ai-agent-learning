def calculator(a, b):
    return a + b


def greeting(name):
    return f"Hello, {name}!"


tools = {
    "calculator": calculator,
    "greeting": greeting
}


goal = input("What is your goal? ")

finished = False

while not finished:

    print("\nAgent is thinking...")

    if "add" in goal.lower():
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = tools["calculator"](first_number, second_number)

        print("Agent used calculator.")
        print("Result:", result)

        finished = True

    elif "greet" in goal.lower():
        name = input("What is your name? ")

        result = tools["greeting"](name)

        print("Agent used greeting.")
        print("Result:", result)

        finished = True

    else:
        print("I don't know which tool to use.")
        finished = True