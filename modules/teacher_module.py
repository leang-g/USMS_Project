"""Teacher role functions."""

from database import students_db, courses_db, find_student_by_id, find_teacher_by_id

def teacher_menu(teacher_id):
    """Teacher Dashboard"""
    teacher = find_teacher_by_id(teacher_id)
    if not teacher:
        print("❌ Teacher not found!")
        return

    while True:
        print("\n" + "="*50)
        print(f"   👨‍🏫 TEACHER DASHBOARD")
        print(f"   Welcome, {teacher.name}!")
        print("="*50)
        print("1. Grade Assignment")
        print("2. View Student Attendance")
        print("3. View Class Structure")
        print("4. Generate Reports")
        print("5. View All Students")
        print("6. View Course Prerequisite Graph")  # (from graph)
        print("7. Logout")

        choice = input("\nChoose (1-7): ")

        if choice == "1":
            grade_assignment()
        elif choice == "2":
            view_student_attendance()
        elif choice == "3":
            view_class_structure()
        elif choice == "4":
            generate_reports()
        elif choice == "5":
            view_all_students()
        elif choice == "6":
            view_prerequisite_graph()  # (from graph)
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice!")

def grade_assignment():
    """Grade Assignment - Hash Table"""
    sid = input("Enter Student ID to grade: ")
    student = find_student_by_id(sid)
    
    if not student:
        print("❌ Student not found!")
        return
    
    print(f"\nGrading: {student.name} (ID: {student.sid})")
    print(f"  Completed: {', '.join(student.completed_courses) if student.completed_courses else 'None'}")
    print(f"  Enrolled: {', '.join(student.enrolled_courses) if student.enrolled_courses else 'None'}")
    
    grade = input("Enter grade (A/B/C/D/F): ").upper()
    if grade in ['A', 'B', 'C', 'D', 'F']:
        print(f"✅ Grade {grade} assigned to {student.name}")
        # Store grade (simplified)
        if not hasattr(student, 'grades'):
            student.grades = {}
        assignment_name = input("Assignment name: ").strip()
        student.grades[assignment_name] = grade
        print(f"✅ {assignment_name}: {grade} recorded!")
    else:
        print("❌ Invalid grade!")

def view_student_attendance():
    """View Attendance - Graph (traverse student's course connections)"""
    sid = input("Enter Student ID to view attendance: ").strip()
    student = students_db.get(sid)
    
    if not student:
        print("❌ Student not found!")
        return
    
    print(f"\n📊 Attendance for {student.name}")
    
    if not student.attendance:
        print("📭 No attendance records found.")
        return
    
    print("\nCourse Attendance:")
    for cid, percentage in student.attendance.items():
        course = courses_db.get(cid)
        name = course.name if course else cid
        pct = int(percentage)
        bar = "█" * (pct // 5) + "░" * (20 - (pct // 5))
        print(f"  {cid}: {name} - {pct}% {bar}")

def view_class_structure():
    """View Class Structure - Tree (organized by semester)"""
    print("\n📁 Class Structure by Semester:")
    
    if not courses_db:
        print("📭 No courses found.")
        return
    
    # Group by semester (Tree would do this hierarchically)
    by_semester = {}
    for cid, course in courses_db.items():
        if course.semester not in by_semester:
            by_semester[course.semester] = []
        by_semester[course.semester].append(course)
    
    for semester in sorted(by_semester.keys()):
        print(f"\n📁 {semester}")
        for course in sorted(by_semester[semester], key=lambda x: x.cid):
            prereq = f" (Prereq: {', '.join(course.prerequisites)})" if course.prerequisites else ""
            print(f"  📘 {course.cid}: {course.name}{prereq}")

def generate_reports():
    """Generate Reports - Tree (in-order traversal for sorted data)"""
    print("\n📊 REPORTS")
    
    # Report 1: All Students sorted by GPA (Tree would sort)
    if students_db:
        print("\n--- Students Sorted by GPA (Highest to Lowest) ---")
        sorted_students = sorted(students_db.values(), key=lambda s: s.gpa, reverse=True)
        for student in sorted_students:
            print(f"  {student.sid}: {student.name} - GPA: {student.gpa}")
    
    # Report 2: All courses
    if courses_db:
        print("\n--- All Courses ---")
        for cid in sorted(courses_db.keys()):
            course = courses_db[cid]
            print(f"  {cid}: {course.name} ({course.semester})")
 
def view_all_students():
    """View all students - Hash Table"""
    if not students_db:
        print("📭 No students found.")
        return
    
    print("\n--- All Students ---")
    for sid in sorted(students_db.keys()):
        student = students_db[sid]
        print(f"  {sid}: {student.name} | GPA: {student.gpa}")

# (from graph): visualize the course prerequisite DAG using the Graph structure.
def view_prerequisite_graph():  # (from graph)
    """Course Prerequisite Graph - topological order + cycle detection."""
    from database import prereq_graph, courses_db  # (from graph)

    print("\n🕸️ COURSE PREREQUISITE GRAPH")

    if prereq_graph.has_cycle():  # (from graph)
        print("⚠️ Invalid curriculum: prerequisites contain a CYCLE!")
        print("   Some courses can never be unlocked. Fix the prerequisites.")
        return

    order = prereq_graph.topological_sort()  # (from graph)
    if not order:
        print("📭 No courses in the graph.")
        return

    print("\n📚 Suggested course order (topological sort):")
    for step, cid in enumerate(order, 1):
        course = courses_db.get(cid)
        name = course.name if course else cid
        prereqs = course.prerequisites if course else []
        prereq_str = f"  (needs: {', '.join(prereqs)})" if prereqs else "  (no prerequisites)"
        print(f"  {step}. {cid}: {name}{prereq_str}")
