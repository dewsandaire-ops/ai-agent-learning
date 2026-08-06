import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students(name, age) VALUES (?, ?)",
    ("John", 20)
)

connection.commit()

print("Student added!")

connection.close()