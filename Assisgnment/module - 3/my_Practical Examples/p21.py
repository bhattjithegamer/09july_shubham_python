import sqlite3

# Connect to SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect("mydatabase.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")

print("Database and table created successfully!")

# Commit changes and close the connection
conn.commit()
conn.close()
