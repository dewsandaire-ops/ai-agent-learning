password = "python123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    user_input = input("Enter the password: ")

    attempts += 1

    if user_input == password:
        print("Access granted!")
        break

    print("Incorrect password.")

else:
    print("Too many attempts. Access denied.")