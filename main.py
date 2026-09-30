"""
main.py
AttendTrack - Student Attendance Management System
CSE1021 Project
"""

from student_manager import load_students, student_menu
from attendance_module import attendance_menu
from reports import reports_menu


def display_banner():
    print("=" * 60)
    print("       AttendTrack - Student Attendance System")
    print("     CSE1021 | Problem Solving & Programming")
    print("=" * 60)


def main():
    display_banner()
    students = load_students()
    print(f"Loaded {len(students)} student(s) from storage.\n")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Student Management")
        print("2. Mark / View Attendance")
        print("3. Attendance Reports")
        print("4. Exit")
        print("===============================")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            students = student_menu(students)
        elif choice == "2":
            students = attendance_menu(students)
        elif choice == "3":
            reports_menu(students)
        elif choice == "4":
            print("\nThank you for using AttendTrack!")
            print("All data has been saved.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
