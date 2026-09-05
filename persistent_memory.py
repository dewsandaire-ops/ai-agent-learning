import json
import os


MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(memory, key, value):
    memory[key] = value
    save_memory(memory)


def recall(memory, key):
    return memory.get(key)


memory = load_memory()

print("=== Persistent AI Agent Memory ===")

name = recall(memory, "name")

if name:
    print("I remember your name:", name)
else:
    name = input("What is your name? ")
    remember(memory, "name", name)

language = recall(memory, "language")

if language:
    print("I remember you are learning:", language)
else:
    language = input("What programming language are you learning? ")
    remember(memory, "language", language)

print("\nMemory check:")
print("Name:", name)
print("Language:", language)