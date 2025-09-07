import sqlite3

# Connect to SQLite database (creates the database if it doesn't exist)
database_connection = sqlite3.connect("school_database.db")

# Create a cursor object
db_cursor = database_connection.cursor()

# Create a table
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS students_info (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_age INTEGER
)
""")

print("Database and table created successfully!")

# Commit changes and close the connection
database_connection.commit()
database_connection.close()
