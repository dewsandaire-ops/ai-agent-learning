entry = input("Write today's diary entry: ")

with open("diary.txt", "a") as file:
    file.write(entry + "\n")

print("Diary saved successfully!")