"""Dummy data generator for development and testing."""

from database import students_db, teachers_db, courses_db
from models import Student, Teacher, Course

def seed_database():
    """Fill the database with sample data"""
    print("🌱 Seeding database...")

    # --- 1. Add Courses ---
    courses = [
        Course("CS101", "Programming I", 3, "Year 1 - Semester 1"),
        Course("CS102", "Programming II", 3, "Year 1 - Semester 2", ["CS101"]),
        Course("CS201", "Data Structures I", 3, "Year 2 - Semester 1", ["CS102"]),
        Course("CS202", "Data Structures II", 3, "Year 2 - Semester 2", ["CS201"]),
        Course("CS301", "Database Systems", 3, "Year 3 - Semester 1", ["CS202"]),
        Course("CS302", "Software Engineering", 3, "Year 3 - Semester 2", ["CS301"]),
        Course("ITE100", "Intro to ITE", 3, "Year 1 - Semester 1"),
        Course("ITE200", "Web Development", 3, "Year 2 - Semester 2", ["CS101"]),
        Course("ITE300", "Networking", 3, "Year 3 - Semester 1", ["CS102"]),
        Course("ITE400", "Machine Learning", 3, "Year 4 - Semester 1", ["CS301"]),
    ]
    for course in courses:
        courses_db[course.cid] = course

    # --- 2. Add Students ---
    students_data = [
        ("ITE-001", "Sokha", "ITE", 3.6, ["CS101", "CS102"]),
        ("ITE-002", "Dara", "ITE", 3.8, ["CS101", "CS102", "CS201"]),
        ("ITE-003", "Srey Nich", "ITE", 3.2, ["CS101"]),
        ("ITE-004", "Vannak", "ITE", 2.8, ["CS101", "CS102"]),
        ("ITE-005", "Rithy", "ITE", 3.9, ["CS101", "CS102", "CS201", "CS202"]),
        ("ITE-006", "Sovann", "ITE", 3.0, ["CS101"]),
        ("ITE-007", "Sreyleak", "ITE", 3.5, ["CS101", "CS102", "ITE100"]),
        ("ITE-008", "Bora", "ITE", 2.5, ["CS101"]),
        ("ITE-009", "Chantou", "ITE", 3.3, ["CS101", "CS102", "CS201"]),
        ("ITE-010", "Kimsan", "ITE", 3.7, ["CS101", "CS102", "CS201", "CS202"]),
    ]
    
    for sid, name, major, gpa, completed in students_data:
        student = Student(sid, name, major, gpa, completed)
        students_db[sid] = student
        # Add dummy attendance (Graph data)
        for cid in completed:
            student.attendance[cid] = 80 + (gpa * 5)

    # --- 3. Add Teachers ---
    teachers_data = [
        ("T001", "Dr. Chhoeum", "ITE"),
        ("T002", "Prof. Sok", "ITE"),
        ("T003", "Dr. Vantha", "ITE"),
    ]
    for tid, name, dept in teachers_data:
        teachers_db[tid] = Teacher(tid, name, dept)

    print(f"✅ Database seeded! {len(students_db)} students, {len(teachers_db)} teachers, {len(courses_db)} courses.")
