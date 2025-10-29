
import sqlite3


conn = sqlite3.connect("college.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS college_students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    city TEXT,
    marks INTEGER,
    attendance REAL,
    teacher TEXT,
    course TEXT
)
""")


cursor.executemany("""
INSERT INTO college_students 
(name, age, gender, city, marks, attendance, teacher, course)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", [
    ("Arjun", 19, "Male", "Chennai", 88, 95.5, "Dr. Kumar", "CSE"),
    ("Meena", 18, "Female", "Coimbatore", 92, 97.0, "Dr. Latha", "ECE"),
    ("Ravi", 20, "Male", "Madurai", 76, 89.0, "Dr. Rajesh", "BME"),
    ("Priya", 19, "Female", "Trichy", 85, 93.0, "Dr. Deepa", "EEE"),
    ("Vikram", 21, "Male", "Salem", 90, 96.2, "Dr. Arun", "CSE"),
    ("Anjali", 18, "Female", "Erode", 78, 91.5, "Dr. Nisha", "IT"),
    ("Sanjay", 19, "Male", "Chennai", 82, 88.3, "Dr. Kumar", "ECE"),
    ("Divya", 18, "Female", "Coimbatore", 94, 99.0, "Dr. Latha", "EEE"),
])


conn.commit()
conn.close()

print("🎓 College database created successfully with 9 columns!")
