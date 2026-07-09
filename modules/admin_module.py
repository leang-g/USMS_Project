"""Admin role functions."""

from database import (
    students_db, teachers_db, courses_db,
    undo_stack, get_next_student_id, get_next_teacher_id,
    find_student_by_id, find_course_by_id, find_teacher_by_id
)
from models import Student, Teacher, Course

def admin_menu():
    """Admin Dashboard"""
    while True:
        print("\n" + "="*50)
        print("   👑 ADMIN DASHBOARD")
        print("="*50)
        print("1. Manage Students")
        print("2. Manage Teachers")
        print("3. Manage Courses")
        print("4. Undo Last Action")
        print("5. View All Data")
        print("6. Logout")

        choice = input("\nChoose (1-6): ")

        if choice == "1":
            manage_students()
        elif choice == "2":
            manage_teachers()
        elif choice == "3":
            manage_courses()
        elif choice == "4":
            undo_last_action()
        elif choice == "5":
            view_all_data()
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice!")

# ---------- STUDENT MANAGEMENT ----------
def manage_students():
    while True:
        print("\n--- Manage Students ---")
        print("1. Add Student (Admission)")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("Choose (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice!")

def add_student():
    """Insert - Hash Table O(1)"""
    print("\n--- Add New Student ---")
    name = input("Name: ")
    major = input("Major: ")
    gpa = get_float("GPA (e.g., 3.5): ")
    
    new_id = get_next_student_id()
    student = Student(new_id, name, major, gpa)
    students_db[new_id] = student
    
    # Save for Undo
    undo_stack.push(("add_student", new_id, student))
    
    print(f"✅ Student {name} added successfully! ID: {new_id}")

def view_all_students():
    """Sort - Tree (via sorted list)"""
    if not students_db:
        print("📭 No students found.")
        return
    
    print("\n--- All Students ---")
    # Sort by ID (Tree would do this)
    for sid in sorted(students_db.keys()):
        student = students_db[sid]
        print(f"  {sid}: {student.name} | Major: {student.major} | GPA: {student.gpa}")
    print(f"\nTotal: {len(students_db)} students")

def search_student():
    """Search - Hash Table O(1)"""
    sid = input("Enter Student ID (e.g., ITE-001): ")
    student = find_student_by_id(sid)
    
    if student:
        print(f"\n✅ Found:")
        print(f"  ID: {student.sid}")
        print(f"  Name: {student.name}")
        print(f"  Major: {student.major}")
        print(f"  GPA: {student.gpa}")
        print(f"  Completed: {', '.join(student.completed_courses) if student.completed_courses else 'None'}")
        print(f"  Enrolled: {', '.join(student.enrolled_courses) if student.enrolled_courses else 'None'}")
    else:
        print("❌ Student not found!")

def update_student():
    """Update - Hash Table"""
    sid = input("Enter Student ID to update: ")
    student = find_student_by_id(sid)
    
    if not student:
        print("❌ Student not found!")
        return
    
    print(f"\nUpdating: {student.name} (Current GPA: {student.gpa})")
    new_name = input(f"Name [{student.name}]: ").strip()
    new_major = input(f"Major [{student.major}]: ").strip()
    new_gpa = input(f"GPA [{student.gpa}]: ").strip()
    
    # Save old state for Undo
    undo_stack.push(("update_student", sid, student))
    
    if new_name:
        student.name = new_name
    if new_major:
        student.major = new_major
    if new_gpa:
        student.gpa = float(new_gpa)
    
    print(f"✅ Student {sid} updated successfully!")

def delete_student():
    """Delete - Hash Table O(1)"""
    sid = input("Enter Student ID to delete: ")
    student = find_student_by_id(sid)
    
    if not student:
        print("❌ Student not found!")
        return
    
    confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
    if confirm.lower() == 'y':
        # Save for Undo
        undo_stack.push(("delete_student", sid, student))
        del students_db[sid]
        print(f"✅ Student {sid} deleted successfully! (Use Undo to restore)")
    else:
        print("❌ Deletion cancelled.")

# ---------- TEACHER MANAGEMENT ----------
def manage_teachers():
    while True:
        print("\n--- Manage Teachers ---")
        print("1. Add Teacher")
        print("2. View All Teachers")
        print("3. Search Teacher")
        print("4. Delete Teacher")
        print("5. Back")

        choice = input("Choose (1-5): ")

        if choice == "1":
            add_teacher()
        elif choice == "2":
            view_all_teachers()
        elif choice == "3":
            search_teacher()
        elif choice == "4":
            delete_teacher()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")

def add_teacher():
    name = input("Name: ")
    department = input("Department: ")
    new_id = get_next_teacher_id()
    teacher = Teacher(new_id, name, department)
    teachers_db[new_id] = teacher
    undo_stack.push(("add_teacher", new_id, teacher))
    print(f"✅ Teacher {name} added! ID: {new_id}")

def view_all_teachers():
    if not teachers_db:
        print("📭 No teachers found.")
        return
    print("\n--- All Teachers ---")
    for tid in sorted(teachers_db.keys()):
        teacher = teachers_db[tid]
        print(f"  {tid}: {teacher.name} | Dept: {teacher.department}")

def search_teacher():
    tid = input("Enter Teacher ID (e.g., T001): ")
    teacher = find_teacher_by_id(tid)
    if teacher:
        print(f"\n✅ Found: {teacher.name} | Dept: {teacher.department}")
    else:
        print("❌ Teacher not found!")

def delete_teacher():
    tid = input("Enter Teacher ID to delete: ")
    if tid in teachers_db:
        undo_stack.push(("delete_teacher", tid, teachers_db[tid]))
        del teachers_db[tid]
        print(f"✅ Teacher {tid} deleted!")
    else:
        print("❌ Teacher not found!")

# ---------- COURSE MANAGEMENT ----------
def manage_courses():
    while True:
        print("\n--- Manage Courses ---")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Delete Course")
        print("4. Back")

        choice = input("Choose (1-4): ")

        if choice == "1":
            add_course()
        elif choice == "2":
            view_all_courses()
        elif choice == "3":
            delete_course()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice!")

def add_course():
    """Insert course into Tree (organized by semester)"""
    cid = input("Course ID (e.g., CS301): ").upper()
    name = input("Course Name: ")
    credits = int(input("Credits: "))
    semester = input("Semester (e.g., Year 3 - Sem 1): ")
    
    prereq_input = input("Prerequisites (comma-separated, e.g., CS101,CS102) or leave empty: ")
    prerequisites = [p.strip().upper() for p in prereq_input.split(',')] if prereq_input else []
    
    course = Course(cid, name, credits, semester, prerequisites)
    courses_db[cid] = course
    undo_stack.push(("add_course", cid, course))
    print(f"✅ Course {cid} added successfully!")

def view_all_courses():
    """Tree: Browse curriculum by semester"""
    if not courses_db:
        print("📭 No courses found.")
        return
    
    print("\n--- All Courses ---")
    # Group by semester (Tree would do this hierarchically)
    by_semester = {}
    for cid, course in courses_db.items():
        if course.semester not in by_semester:
            by_semester[course.semester] = []
        by_semester[course.semester].append(course)
    
    for semester in sorted(by_semester.keys()):
        print(f"\n📁 {semester}")
        for course in by_semester[semester]:
            prereq = f" (Prereq: {', '.join(course.prerequisites)})" if course.prerequisites else ""
            print(f"  📘 {course.cid}: {course.name}{prereq}")

def delete_course():
    cid = input("Enter Course ID to delete: ")
    if cid in courses_db:
        undo_stack.push(("delete_course", cid, courses_db[cid]))
        del courses_db[cid]
        print(f"✅ Course {cid} deleted!")
    else:
        print("❌ Course not found!")

# ---------- UNDO FUNCTION (Stack) ----------
def undo_last_action():
    """Undo using Stack (LIFO)"""
    if undo_stack.is_empty():
        print("📭 Nothing to undo!")
        return
    
    action = undo_stack.pop()
    action_type = action[0]
    
    if action_type == "add_student":
        _, sid, student = action
        if sid in students_db:
            del students_db[sid]
            print(f"✅ Undo: Removed student {student.name}")
        else:
            print("⚠️ Student already removed.")
    
    elif action_type == "delete_student":
        _, sid, student = action
        students_db[sid] = student
        print(f"✅ Undo: Restored student {student.name}")
    
    elif action_type == "update_student":
        _, sid, student = action
        students_db[sid] = student
        print(f"✅ Undo: Restored previous state of {student.name}")
    
    elif action_type == "add_teacher":
        _, tid, teacher = action
        if tid in teachers_db:
            del teachers_db[tid]
            print(f"✅ Undo: Removed teacher {teacher.name}")
    
    elif action_type == "delete_teacher":
        _, tid, teacher = action
        teachers_db[tid] = teacher
        print(f"✅ Undo: Restored teacher {teacher.name}")
    
    elif action_type == "add_course":
        _, cid, course = action
        if cid in courses_db:
            del courses_db[cid]
            print(f"✅ Undo: Removed course {course.name}")
    
    elif action_type == "delete_course":
        _, cid, course = action
        courses_db[cid] = course
        print(f"✅ Undo: Restored course {course.name}")
    
    else:
        print(f"⚠️ Unknown action: {action_type}")

# ---------- VIEW ALL DATA ----------
def view_all_data():
    """View everything in the system"""
    print("\n" + "="*50)
    print("   📊 SYSTEM OVERVIEW")
    print("="*50)
    
    print(f"\n👨‍🎓 Students: {len(students_db)}")
    for sid in sorted(students_db.keys()):
        student = students_db[sid]
        print(f"  {sid}: {student.name} (GPA: {student.gpa})")
    
    print(f"\n👨‍🏫 Teachers: {len(teachers_db)}")
    for tid in sorted(teachers_db.keys()):
        teacher = teachers_db[tid]
        print(f"  {tid}: {teacher.name} ({teacher.department})")
    
    print(f"\n📚 Courses: {len(courses_db)}")
    for cid in sorted(courses_db.keys()):
        course = courses_db[cid]
        print(f"  {cid}: {course.name} ({course.semester})")

# Import for input validation
from utils.input_validator import get_float