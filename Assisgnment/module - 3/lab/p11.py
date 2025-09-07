import sqlite3

# ---- Connect to Database (or create if not exists) ----
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# ---- Create Table ----
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
print("Table created successfully!")

# ---- Insert Data ----
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", 
               ("Bhatt Ji", 21, "BCA"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", 
               ("Raj", 22, "MCA"))
conn.commit()
print("Data inserted successfully!")

# ---- Fetch Data ----
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\n=== Student Records ===")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

# ---- Close Connection ----
conn.close()
