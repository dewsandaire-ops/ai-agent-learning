name = input("Student Name: ")
score = input("Score: ")

with open("students.txt", "a") as file:
    file.write(name + " - " + score + "\n")

print("Student record saved.")