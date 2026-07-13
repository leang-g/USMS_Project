"""Global in-memory data storage for USMS."""

from models import Student, Teacher, Course
from data_structures.graph import Graph  # (from graph): build the course prereq graph

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

# ---------- COURSE PREREQUISITE GRAPH (Directed DAG) ----------
# (from graph): edge prereq -> course means the prerequisite must be completed first.
prereq_graph = Graph()  # (from graph)

# ---------- ATTENDANCE GRAPH (Directed) ----------
# (from graph): edge student -> course means the student has an attendance
# record for that course. Separate from prereq_graph so sorting/cycle checks
# on prerequisites are never affected by attendance data.
attendance_graph = Graph()  # (from graph)

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

def build_prereq_graph():  # (from graph)
    """Rebuild the course prerequisite DAG from courses_db.

    For every course, each prerequisite becomes a directed edge
    ``prereq -> course``. Safe to call after courses are added/removed.
    """
    prereq_graph.adjacency_list.clear()  # (from graph)
    for course in courses_db.values():
        prereq_graph.add_vertex(course.cid)  # (from graph)
        for prereq in course.prerequisites:
            prereq_graph.add_edge(prereq, course.cid)  # (from graph)
    return prereq_graph

def build_attendance_graph():  # (from graph): build attendance graph from students_db
    """Rebuild the attendance graph from students_db.

    For every student, each course with an attendance record becomes a
    directed edge ``student -> course``. Call after attendance is set/changed.
    """
    attendance_graph.adjacency_list.clear()  # (from graph)
    for student in students_db.values():
        attendance_graph.add_vertex(student.sid)  # (from graph)
        for cid in student.attendance:
            attendance_graph.add_edge(student.sid, cid)  # (from graph)
    return attendance_graph