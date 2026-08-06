import sqlite3

connection = sqlite3.connect("school.db")

print("Database created successfully!")

connection.close()
import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

connection.commit()

print("Table created!")

connection.close()