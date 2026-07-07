"""Core model classes for the University Student Management System."""


class Student:
    def __init__(self, student_id, name, email, major):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major
        self.enrolled_courses = []

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"


class Teacher:
    def __init__(self, teacher_id, name, email, department):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email
        self.department = department
        self.assigned_courses = []

    def __repr__(self):
        return f"Teacher({self.teacher_id}, {self.name})"


class Course:
    def __init__(self, course_id, title, credits):
        self.course_id = course_id
        self.title = title
        self.credits = credits
        self.prerequisites = []

    def __repr__(self):
        return f"Course({self.course_id}, {self.title})"
