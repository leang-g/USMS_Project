"""Dummy data generator for development and testing."""

from database import students_db, teachers_db, courses_db, build_prereq_graph, prereq_graph, build_attendance_graph, attendance_graph  # (from graph)
from models import Student, Teacher, Course

def seed_database():
    """Fill the database with sample data so the dashboard shows real info."""
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
    ]
    for course in courses:
        courses_db[course.cid] = course

    # --- 2. Add Students with REAL ENROLLED COURSES ---
    students_data = [
        # (ID, Name, Major, GPA, Completed, Enrolled)
        ("ITE-001", "Sokha", "ITE", 3.6, ["CS101", "CS102"], ["CS201"]),
        ("ITE-002", "Dara", "ITE", 3.8, ["CS101", "CS102", "CS201"], ["CS202"]),
        ("ITE-003", "Srey Nich", "ITE", 3.2, ["CS101"], ["CS102"]),
        ("ITE-004", "Vannak", "ITE", 2.8, ["CS101", "CS102"], []),
        ("ITE-005", "Rithy", "ITE", 3.9, ["CS101", "CS102", "CS201", "CS202"], ["CS301"]),
        ("ITE-006", "Sovann", "ITE", 3.0, ["CS101"], ["ITE100"]),
        ("ITE-007", "Sreyleak", "ITE", 3.5, ["CS101", "CS102"], ["ITE200"]),
        ("ITE-008", "Bora", "ITE", 2.5, [], ["CS101"]),
        ("ITE-009", "Chantou", "ITE", 3.3, ["CS101", "CS102", "CS201"], ["CS301"]),
        ("ITE-010", "Kimsan", "ITE", 3.7, ["CS101", "CS102", "CS201", "CS202"], ["ITE400"]),
    ]
    
    # Add courses to database and set attendance
    for sid, name, major, gpa, completed, enrolled in students_data:
        student = Student(sid, name, major, gpa, completed)
        student.enrolled_courses = enrolled  # 👈 KEY FIX: Adds enrolled courses!
        students_db[sid] = student
        
        # Add dummy attendance for completed AND enrolled courses (Graph data)
        all_courses = completed + enrolled
        for cid in all_courses:
            if cid in courses_db:
                # Random-looking attendance between 75% and 98%
                student.attendance[cid] = 80 + (gpa * 4) + (hash(cid) % 5)

    # --- 3. Add Teachers ---
    teachers_data = [
        ("T001", "Dr. Chhoeum", "ITE"),
        ("T002", "Prof. Sok", "ITE"),
        ("T003", "Dr. Vantha", "ITE"),
    ]
    for tid, name, dept in teachers_data:
        teachers_db[tid] = Teacher(tid, name, dept)

    # (from graph): build the course prerequisite DAG and validate it is acyclic.
    build_prereq_graph()  # (from graph)
    if prereq_graph.has_cycle():  # (from graph)
        print("⚠️ Warning: course prerequisites contain a cycle!")

    # (from graph): build the attendance graph (student -> course edges).
    build_attendance_graph()  # (from graph)

    print(f"✅ Database seeded! {len(students_db)} students, {len(teachers_db)} teachers, {len(courses_db)} courses.")