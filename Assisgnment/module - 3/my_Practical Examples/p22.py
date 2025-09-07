import sqlite3

# Connect to the database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Insert data into table
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bhattji", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Riya", 22))

# Commit changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Data in the students table:")
for row in rows:
    print(row)

# Close the connection
conn.close()
