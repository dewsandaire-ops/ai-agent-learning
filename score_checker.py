try:
    score = int(input("Enter your score: "))

    if score >= 50:
        print("Pass")
    else:
        print("Fail")

except ValueError:
    print("Please enter numbers only.")