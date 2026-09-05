def calculator(number1, number2, operation):
    """Perform a basic mathematical calculation."""

    if operation == "+":
        return number1 + number2

    if operation == "-":
        return number1 - number2

    if operation == "*":
        return number1 * number2

    if operation == "/":
        if number2 == 0:
            return "Error: Cannot divide by zero."
        return number1 / number2

    return "Error: Unsupported operation."
