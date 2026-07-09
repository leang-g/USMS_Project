"""Global in-memory data storage for USMS."""

from models import Student, Teacher, Course

# ---------- SIMPLE STACK ----------
class SimpleStack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def is_empty(self):
        return len(self.items) == 0

# ---------- GLOBAL DATABASES (Act as Hash Tables) ----------
students_db = {}      # Key: "ITE-001", Value: Student object
teachers_db = {}      # Key: "T001", Value: Teacher object
courses_db = {}       # Key: "CS101", Value: Course object

# ---------- UNDO STACK ----------
undo_stack = SimpleStack()

# ---------- HELPER FUNCTIONS ----------
def get_next_student_id():
    if not students_db:
        return "ITE-001"
    numbers = [int(sid.split("-")[1]) for sid in students_db.keys()]
    return f"ITE-{max(numbers) + 1:03d}"

def get_next_teacher_id():
    if not teachers_db:
        return "T001"
    numbers = [int(tid[1:]) for tid in teachers_db.keys()]
    return f"T{max(numbers) + 1:03d}"

def find_student_by_id(student_id):
    """Hash Table lookup - O(1)"""
    return students_db.get(student_id)

def find_course_by_id(course_id):
    """Hash Table lookup - O(1)"""
    return courses_db.get(course_id)

def find_teacher_by_id(teacher_id):
    """Hash Table lookup - O(1)"""
    return teachers_db.get(teacher_id)