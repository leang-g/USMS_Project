"""Student role functions."""


# modules/student_module.py

from database import students_db, courses_db, find_student_by_id

def student_menu(student_id):
    """Student Dashboard"""
    student = find_student_by_id(student_id)
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

        choice = input("\nChoose (1-6): ")

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
            print("❌ Invalid choice!")

def view_profile(student_id):
    """View Profile - Hash Table O(1)"""
    student = find_student_by_id(student_id)
    if not student:
        return
    
    print("\n--- My Profile ---")
    print(f"  📛 ID: {student.sid}")
    print(f"  👤 Name: {student.name}")
    print(f"  🎓 Major: {student.major}")
    print(f"  📊 GPA: {student.gpa}")
    print(f"  ✅ Completed Courses: {', '.join(student.completed_courses) if student.completed_courses else 'None'}")
    print(f"  📖 Enrolled Courses: {', '.join(student.enrolled_courses) if student.enrolled_courses else 'None'}")

def view_materials(student_id):
    """View Course Materials - Hash Table"""
    student = find_student_by_id(student_id)
    if not student:
        return
    
    print("\n--- My Course Materials ---")
    if not student.enrolled_courses:
        print("📭 You are not enrolled in any courses.")
        return
    
    for cid in student.enrolled_courses:
        course = courses_db.get(cid)
        if course:
            print(f"\n📘 {course.name} ({cid})")
            print(f"   Semester: {course.semester}")
            print(f"   📄 Materials: Lecture Slides, Notes, Assignments")
        else:
            print(f"\n⚠️ Course {cid} not found in database.")

def enroll_course(student_id):
    """Enroll in Course - Tree (browse) + Graph (prerequisite check)"""
    student = find_student_by_id(student_id)
    if not student:
        return
    
    print("\n--- Enroll in Course ---")
    print("📚 Available Courses:")
    
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
    
    choice = input("\nEnter Course ID to enroll (or 0 to cancel): ").upper()
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

def submit_assignment(student_id):
    """Submit Assignment - Hash Table"""
    student = find_student_by_id(student_id)
    if not student:
        return
    
    print("\n--- Submit Assignment ---")
    if not student.enrolled_courses:
        print("📭 You are not enrolled in any courses.")
        return
    
    print("Your enrolled courses:")
    for i, cid in enumerate(student.enrolled_courses, 1):
        course = courses_db.get(cid)
        name = course.name if course else cid
        print(f"  {i}. {name}")
    
    choice = input("Enter course number to submit assignment (or 0 to cancel): ")
    if choice == "0":
        return
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(student.enrolled_courses):
            cid = student.enrolled_courses[idx]
            course = courses_db.get(cid)
            print(f"✅ Assignment submitted for {course.name if course else cid}!")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Invalid input.")

def view_roadmap(student_id):
    """View Roadmap - Graph (shows completed vs locked)"""
    student = find_student_by_id(student_id)
    if not student:
        return
    
    print("\n--- My Academic Roadmap ---")
    
    print("\n✅ Completed Courses:")
    for cid in student.completed_courses:
        course = courses_db.get(cid)
        name = course.name if course else cid
        print(f"  ✅ {cid}: {name}")
    
    print("\n📖 Enrolled Courses:")
    for cid in student.enrolled_courses:
        course = courses_db.get(cid)
        name = course.name if course else cid
        print(f"  📖 {cid}: {name}")
    
    print("\n🔒 Locked Courses (Need prerequisites):")
    for cid, course in courses_db.items():
        if cid not in student.completed_courses and cid not in student.enrolled_courses:
            prereq_met = True
            for prereq in course.prerequisites:
                if prereq not in student.completed_courses:
                    prereq_met = False
                    break
            if not prereq_met:
                prereq_str = f" (Need: {', '.join(course.prerequisites)})"
                print(f"  🔒 {cid}: {course.name}{prereq_str}")
    
    print("\n📋 Available Courses:")
    for cid, course in courses_db.items():
        if cid not in student.completed_courses and cid not in student.enrolled_courses:
            prereq_met = True
            for prereq in course.prerequisites:
                if prereq not in student.completed_courses:
                    prereq_met = False
                    break
            if prereq_met:
                print(f"  📋 {cid}: {course.name}")