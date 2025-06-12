
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["school"]

db.students.insert_many([
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 22}
])

db.courses.insert_many([
    {"course": "Math", "instructor": "Dr. Smith"},
    {"course": "Science", "instructor": "Dr. Jane"}
])

db.enrollments.insert_many([
    {"student": "Alice", "course": "Math"},
    {"student": "Charlie", "course": "Math"},
    {"student": "Bob", "course": "Science"}
])

print("Sample data inserted.")
