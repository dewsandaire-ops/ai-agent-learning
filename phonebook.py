phonebook = {
    "John": "08011111111",
    "Mary": "08022222222",
    "Peter": "08033333333"
}

name = input("Enter a name: ")

if name in phonebook:
    print("Phone Number:", phonebook[name])
else:
    print("Contact not found.")