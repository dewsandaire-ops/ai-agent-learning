try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    print("Answer:", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")
    