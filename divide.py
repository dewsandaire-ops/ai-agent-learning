try:
    number = int(input("Enter a number: "))
    answer = 100 / number

    print(answer)

except ZeroDivisionError:
    print("You cannot divide by zero.")