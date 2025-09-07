import sqlite3

# ---- Connect to Database (or create if not exists) ----
connection = sqlite3.connect("students_db.db")
cur = connection.cursor()

# ---- Create Table ----
cur.execute("""
CREATE TABLE IF NOT EXISTS learners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
print("Table created successfully!")

# ---- Insert Data ----
cur.execute("INSERT INTO learners (name, age, course) VALUES (?, ?, ?)", 
            ("Bhatt Ji", 21, "BCA"))
cur.execute("INSERT INTO learners (name, age, course) VALUES (?, ?, ?)", 
            ("Raj", 22, "MCA"))
connection.commit()
print("Data inserted successfully!")

# ---- Fetch Data ----
cur.execute("SELECT * FROM learners")
records = cur.fetchall()

print("\n=== Learner Records ===")
for record in records:
    print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Course: {record[3]}")

# ---- Close Connection ----
connection.close()
