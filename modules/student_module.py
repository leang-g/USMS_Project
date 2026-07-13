"""Student role functions."""

from database import students_db, courses_db

def student_menu(student_id):
    """Student Dashboard"""
    student = students_db.get(student_id)
    if not student:
        print("❌ Student not found!")
        return

    while True:
        print("\n" + "="*50)
        print(f"   🧑‍🎓 STUDENT DASHBOARD")
        print(f"   Welcome, {student.name}!")
        print("="*50)
        print("1. View My Profile")
        print("2. View Course Materials")
        print("3. Enroll in Course")
        print("4. Submit Assignment")
        print("5. View My Roadmap")
        print("6. Logout")

        choice = input("\nChoose (1-6): ").strip()  # <-- Added .strip() to remove spaces

        if choice == "1":
            view_profile(student_id)
        elif choice == "2":
            view_materials(student_id)
        elif choice == "3":
            enroll_course(student_id)
        elif choice == "4":
            submit_assignment(student_id)
        elif choice == "5":
            view_roadmap(student_id)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

# ---------- VIEW PROFILE ----------
def view_profile(student_id):
    student = students_db.get(student_id)
    if not student:
        print("❌ Student not found!")
        return
    
    print("\n" + "-"*40)
    print("📋 MY PROFILE")
    print("-"*40)
    print(f"  📛 ID          : {student.sid}")
    print(f"  👤 Name        : {student.name}")
    print(f"  🎓 Major       : {student.major}")
    print(f"  📊 GPA         : {student.gpa}")
    
    completed = ', '.join(student.completed_courses) if student.completed_courses else 'None'
    print(f"  ✅ Completed   : {completed}")
    
    enrolled = ', '.join(student.enrolled_courses) if student.enrolled_courses else 'None'
    print(f"  📖 Enrolled    : {enrolled}")
    print("-"*40)

# ---------- VIEW COURSE MATERIALS ----------
def view_materials(student_id):
    student = students_db.get(student_id)
    if not student:
        print("❌ Student not found!")
        return
    
    print("\n" + "-"*40)
    print("📄 COURSE MATERIALS")
    print("-"*40)
    
    if not student.enrolled_courses:
        print("📭 You are not enrolled in any courses.")
        print("   Use 'Enroll in Course' to add some!")
        return
    
    for cid in student.enrolled_courses:
        course = courses_db.get(cid)
        if course:
            print(f"\n📘 {course.name} ({cid})")
            print(f"   Semester: {course.semester}")
            print(f"   📄 Materials: Lecture Slides, Lab Notes, Assignments")
        else:
            print(f"\n⚠️ Course {cid} not found in database.")
    print("-"*40)

# ---------- ENROLL IN COURSE ----------
def enroll_course(student_id):
    student = students_db.get(student_id)
    if not student:
        print("❌ Student not found!")
        return
    
    print("\n" + "-"*40)
    print("📚 ENROLL IN COURSE")
    print("-"*40)
    
    available = []
    for cid, course in courses_db.items():
        if cid not in student.completed_courses and cid not in student.enrolled_courses:
            prereq_met = True
            for prereq in course.prerequisites:
                if prereq not in student.completed_courses:
                    prereq_met = False
                    break
            
            status = "✅ Prereqs met" if prereq_met else "🔒 Prereqs not met"
            available.append((cid, course, prereq_met))
            prereq_str = f" (Prereq: {', '.join(course.prerequisites)})" if course.prerequisites else ""
            print(f"  {cid}: {course.name}{prereq_str} - {status}")
    
    if not available:
        print("📭 No courses available for enrollment.")
        return
    
    choice = input("\nEnter Course ID to enroll (or 0 to cancel): ").upper().strip()
    if choice == "0":
        return
    
    selected = None
    for cid, course, prereq_met in available:
        if cid == choice:
            selected = (cid, course, prereq_met)
            break
    
    if not selected:
        print("❌ Invalid course ID.")
        return
    
    cid, course, prereq_met = selected
    if not prereq_met:
        print(f"❌ You don't meet the prerequisites for {course.name}!")
        return
    
    student.enrolled_courses.append(cid)
    print(f"✅ Successfully enrolled in {course.name}!")

# ---------- SUBMIT ASSIGNMENT ----------

def submit_assignment(student_id):
    """Submit Assignment - Hash Table"""
    student = students_db.get(student_id)
    if not student:
        print("❌ Student not found!")
        return
    
    print("\n" + "-"*40)
    print("📤 SUBMIT ASSIGNMENT")
    print("-"*40)
    
    if not student.enrolled_courses:
        print("📭 You are not enrolled in any courses.")
        return
    
    print("Your enrolled courses:")
    for i, cid in enumerate(student.enrolled_courses, 1):
        course = courses_db.get(cid)
        name = course.name if course else cid
        print(f"  {i}. {name} (ID: {cid})")  # <-- SHOW THE ID TOO!
    
    choice = input("Enter course number (e.g., 1) or Course ID (e.g., CS201) to submit (or 0 to cancel): ").strip()
    if choice == "0":
        return
    
    # Try to find the course
    selected_cid = None
    
    # Check if it's a number (list index)
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(student.enrolled_courses):
            selected_cid = student.enrolled_courses[idx]
    
    # If not a number, check if it's a Course ID
    if selected_cid is None:
        # Check if the input matches any enrolled course ID
        for cid in student.enrolled_courses:
            if cid.upper() == choice.upper():
                selected_cid = cid
                break
    
    if selected_cid is None:
        print("❌ Invalid selection. Please enter a number from the list or a valid Course ID.")
        return
    
    course = courses_db.get(selected_cid)
    print(f"✅ Assignment submitted for {course.name if course else selected_cid}!")
    print("-"*40)
    
# ---------- VIEW ROADMAP ----------
def view_roadmap(student_id):
    student = students_db.get(student_id)
    if not student:
        print("❌ Student not found!")
        return
    
    print("\n" + "="*50)
    print("   🗺️ MY ACADEMIC ROADMAP")
    print("="*50)
    
    # 1. Completed Courses
    print("\n✅ COMPLETED COURSES:")
    if student.completed_courses:
        for cid in student.completed_courses:
            course = courses_db.get(cid)
            name = course.name if course else cid
            print(f"  ✅ {cid}: {name}")
    else:
        print("  (No courses completed yet)")
    
    # 2. Enrolled Courses
    print("\n📖 ENROLLED COURSES:")
    if student.enrolled_courses:
        for cid in student.enrolled_courses:
            course = courses_db.get(cid)
            name = course.name if course else cid
            print(f"  📖 {cid}: {name} (In Progress)")
    else:
        print("  (Not enrolled in any courses)")
    
    # 3. Locked Courses
    print("\n🔒 LOCKED COURSES (Need prerequisites):")
    locked_count = 0
    for cid, course in courses_db.items():
        if cid not in student.completed_courses and cid not in student.enrolled_courses:
            prereq_met = True
            missing = []
            for prereq in course.prerequisites:
                if prereq not in student.completed_courses:
                    prereq_met = False
                    missing.append(prereq)
            if not prereq_met:
                locked_count += 1
                print(f"  🔒 {cid}: {course.name} (Need: {', '.join(missing)})")
    if locked_count == 0:
        print("  (No locked courses found)")

    # 4. Available Courses
    print("\n📋 AVAILABLE COURSES (Prerequisites met):")
    available_count = 0
    for cid, course in courses_db.items():
        if cid not in student.completed_courses and cid not in student.enrolled_courses:
            prereq_met = True
            for prereq in course.prerequisites:
                if prereq not in student.completed_courses:
                    prereq_met = False
                    break
            if prereq_met:
                available_count += 1
                print(f"  📋 {cid}: {course.name}")
    if available_count == 0:
        print("  (No available courses right now)")
    
    print("\n" + "="*50)