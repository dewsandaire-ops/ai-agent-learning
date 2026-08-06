import sqlite3

name = input("Student Name: ")
age = int(input("Student Age: "))

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students(name, age) VALUES (?, ?)",
    (name, age)
)

connection.commit()

connection.close()

print("Student saved.")