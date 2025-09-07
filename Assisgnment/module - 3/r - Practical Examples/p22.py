import sqlite3

# Connect to the database
database_connection = sqlite3.connect("school_database.db")
db_cursor = database_connection.cursor()

# Insert data into table
db_cursor.execute("INSERT INTO students_info (student_name, student_age) VALUES (?, ?)", ("User1", 20))
db_cursor.execute("INSERT INTO students_info (student_name, student_age) VALUES (?, ?)", ("User2", 22))

# Commit changes
database_connection.commit()

# Fetch data
db_cursor.execute("SELECT * FROM students_info")
all_students = db_cursor.fetchall()

print("Data in the students_info table:")
for student in all_students:
    print(student)

# Close the connection
database_connection.close()
