import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute(
    "UPDATE students SET age=? WHERE name=?",
    (25, "John")
)

connection.commit()

print("Updated!")

connection.close()