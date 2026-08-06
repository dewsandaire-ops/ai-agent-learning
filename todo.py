task = input("Enter a task: ")

with open("todo.txt", "a") as file:
    file.write(task + "\n")

print("Task added!")