# models.py

class Student:
    def __init__(self, sid, name, major, gpa, completed_courses=None):
        self.sid = sid
        self.name = name
        self.major = major
        self.gpa = gpa
        self.completed_courses = completed_courses if completed_courses else []
        self.enrolled_courses = []
        self.attendance = {}  # course_id -> percentage

    def __str__(self):
        return f"{self.sid}: {self.name} | GPA: {self.gpa}"

class Teacher:
    def __init__(self, tid, name, department):
        self.tid = tid
        self.name = name
        self.department = department
        self.assigned_courses = []

    def __str__(self):
        return f"{self.tid}: {self.name} | Dept: {self.department}"

class Course:
    def __init__(self, cid, name, credits, semester, prerequisites=None):
        self.cid = cid
        self.name = name
        self.credits = credits
        self.semester = semester
        self.prerequisites = prerequisites if prerequisites else []

    def __str__(self):
        return f"{self.cid}: {self.name} ({self.semester})"