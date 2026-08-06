with open("students.txt", "r") as file:
    print(file.read)
    import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()