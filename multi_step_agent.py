def calculator(a, b):
    return a + b


def greeting(name):
    return f"Hello, {name}!"


tools = {
    "calculator": calculator,
    "greeting": greeting
}


print("=== Multi-Step Agent ===")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("\nAgent is thinking...")
print("Step 1: Using calculator...")

result = tools["calculator"](first_number, second_number)

print("Calculation result:", result)

print("\nAgent is thinking...")
print("Step 2: Using greeting...")

name = input("What is your name? ")

message = tools["greeting"](name)

print("Greeting result:", message)

print("\nAgent completed the goal.")