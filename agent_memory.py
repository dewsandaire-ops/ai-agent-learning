memory = {}


def remember(key, value):
    memory[key] = value


def recall(key):
    return memory.get(key, "I don't know that yet.")


print("=== Agent Memory ===")

name = input("What is your name? ")
remember("name", name)

favorite_language = input("What programming language are you learning? ")
remember("favorite_language", favorite_language)

print("\nAgent memory:")
print("Name:", recall("name"))
print("Programming language:", recall("favorite_language"))