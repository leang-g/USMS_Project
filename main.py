"""Entry point for the University Student Management System."""

from database import seed_database
from modules.admin_module import admin_menu
from modules.student_module import student_menu
from modules.teacher_module import teacher_menu
from utils.input_validator import get_menu_choice


def login():
    """Simple role selector for the first version of the system."""
    print("\nUniversity Student Management System")
    print("1. Student")
    print("2. Teacher")
    print("3. Admin")
    print("4. Exit")
    return get_menu_choice("Choose your role: ", 1, 4)


def main():
    seed_database()

    while True:
        choice = login()

        if choice == 1:
            student_menu()
        elif choice == 2:
            teacher_menu()
        elif choice == 3:
            admin_menu()
        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
