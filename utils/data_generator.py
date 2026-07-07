"""Dummy data generator for development and testing."""

from models import Course, Student, Teacher


def generate_students():
    return [
        Student("S001", "Sok Dara", "sok.dara@example.com", "Computer Science"),
        Student("S002", "Chan Bopha", "chan.bopha@example.com", "Information Systems"),
        Student("S003", "Kim Vanna", "kim.vanna@example.com", "Software Engineering"),
        Student("S004", "Lim Sophea", "lim.sophea@example.com", "Data Science"),
        Student("S005", "Heng Rotha", "heng.rotha@example.com", "Cybersecurity"),
        Student("S006", "Mao Sreyneang", "mao.sreyneang@example.com", "Computer Science"),
        Student("S007", "Noun Pisey", "noun.pisey@example.com", "Information Systems"),
        Student("S008", "Ouk Rithy", "ouk.rithy@example.com", "Software Engineering"),
        Student("S009", "Pov Chenda", "pov.chenda@example.com", "Data Science"),
        Student("S010", "Teav Malis", "teav.malis@example.com", "Cybersecurity"),
    ]


def generate_teachers():
    return [
        Teacher("T001", "Dr. Somnang", "somnang@example.com", "Computer Science"),
        Teacher("T002", "Prof. Sopheak", "sopheak@example.com", "Information Technology"),
        Teacher("T003", "Ms. Kanika", "kanika@example.com", "Software Engineering"),
    ]


def generate_courses():
    return [
        Course("C001", "Data Structures and Algorithms", 3),
        Course("C002", "Database Systems", 3),
        Course("C003", "Object-Oriented Programming", 3),
        Course("C004", "Computer Networks", 3),
        Course("C005", "Web Development", 3),
    ]
