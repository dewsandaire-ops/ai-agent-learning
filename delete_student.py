import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute(
    "DELETE FROM students WHERE name=?",
    ("John",)
)

connection.commit()

print("Deleted!")

connection.close()