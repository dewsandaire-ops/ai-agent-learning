try:
    with open("message.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist.")