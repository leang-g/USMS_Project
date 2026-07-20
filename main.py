"""Entry point for the University Student Management System."""

from database import students_db, teachers_db, build_prereq_graph, build_attendance_graph
from modules.student_module import student_menu
from modules.teacher_module import teacher_menu
from modules.admin_module import admin_menu
from utils.data_generator import seed_database
from database import build_curriculum_tree


def login():
    """Main login and role router"""
    while True:
        print("\n" + "="*50)
        print("   🎓 ITE STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Student")
        print("2. Teacher")
        print("3. Admin")
        print("4. Exit")

        choice = input("\nChoose your role (1-4): ").strip()

        if choice == "1":
            student_id = input("Enter your Student ID (e.g., ITE-001): ").strip()
            if student_id in students_db:
                student_menu(student_id)
            else:
                print(f"❌ Student {student_id} not found!")
                print("Available students:")
                for sid in sorted(students_db.keys()):
                    print(f"  {sid}: {students_db[sid].name}")

        elif choice == "2":
            teacher_id = input("Enter your Teacher ID (e.g., T001): ").strip()
            if teacher_id in teachers_db:
                teacher_menu(teacher_id)
            else:
                print(f"❌ Teacher {teacher_id} not found!")
                print("Available teachers:")
                for tid in sorted(teachers_db.keys()):
                    print(f"  {tid}: {teachers_db[tid].name}")

        elif choice == "3":
            print("\n🔒 ADMIN AUTHENTICATION REQUIRED")
            username = input("Enter Admin Username: ").strip()
            password = input("Enter Admin Password: ").strip()
            if username == "admin" and password == "admin123":
                print("✅ Access Granted!")
                admin_menu()
            else:
                print("❌ Access Denied! Invalid credentials.")

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    print("🚀 Starting University Student Management System...")
    
    # Seed fresh data every time (no persistence)
    seed_database()
    
    # Build the prerequisite graph from the course data
    build_prereq_graph()
    
    # Build the attendance graph from the student data
    build_attendance_graph()
    
    #Build the currimlum tree from courses_db
    build_curriculum_tree()
    
    # Optional: Check for cycles and warn
    from database import prereq_graph
    if prereq_graph.has_cycle():
        print("⚠️ WARNING: Course prerequisites contain a cycle!")
    else:
        print("✅ No cycles detected in prerequisite graph.")
    
    # Start the system
    login()