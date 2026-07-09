"""Global in-memory data storage for USMS."""

from models import Student, Teacher, Course

# ---------- GLOBAL DATABASES (Act as Hash Tables) ----------
students_db = {}      # Key: "ITE-001", Value: Student object
teachers_db = {}      # Key: "T001", Value: Teacher object
courses_db = {}       # Key: "CS101", Value: Course object
assignments_db = {}   # Key: "A001", Value: grades dict

# ---------- UNDO STACK (We will import Stack later) ----------
# We'll use a simple Python list as a Stack placeholder for now
undo_stack = []

# ---------- HELPER FUNCTIONS (For Admin) ----------
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