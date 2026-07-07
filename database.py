"""Global in-memory data storage for USMS."""

from utils.data_generator import generate_courses, generate_students, generate_teachers

students = []
teachers = []
courses = []


def seed_database():
    """Load dummy data for development and testing."""
    if students or teachers or courses:
        return

    students.extend(generate_students())
    teachers.extend(generate_teachers())
    courses.extend(generate_courses())
