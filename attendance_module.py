"""
attendance_module.py
Module 2: Attendance Marking
"""

from utils import is_valid_roll, is_valid_date, get_today, search_student_by_roll
from student_manager import save_students


def mark_attendance(students):
    """Mark attendance for a specific date (for all or one student)."""
    print("\n--- Mark Attendance ---")
    date = input(f"Enter date (YYYY-MM-DD) [Press Enter for today ({get_today()})]: ").strip()
    if not date:
        date = get_today()
    if not is_valid_date(date):
        print("Invalid date format. Use YYYY-MM-DD.")
        return students

    print("\n1. Mark for ALL students")
    print("2. Mark for ONE student")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        print(f"\nMarking attendance for {date}")
        print("Enter P for Present, A for Absent")
        for student in students:
            while True:
                status = input(f"{student['name']} (Roll {student['roll']}): ").strip().upper()
                if status in ("P", "A"):
                    student.setdefault("attendance", {})[date] = status
                    break
                print("Invalid! Enter P or A only.")
        save_students(students)
        print("Attendance marked for all students.")

    elif choice == "2":
        roll = input("Enter Roll Number: ").strip()
        if not is_valid_roll(roll):
            print("Invalid roll number.")
            return students
        student = search_student_by_roll(students, int(roll))
        if not student:
            print("Student not found.")
            return students

        while True:
            status = input(f"Status for {student['name']} (P/A): ").strip().upper()
            if status in ("P", "A"):
                student.setdefault("attendance", {})[date] = status
                save_students(students)
                print(f"Marked as {'Present' if status == 'P' else 'Absent'}.")
                break
            print("Invalid! Enter P or A only.")
    else:
        print("Invalid choice.")
    return students


def view_daily_attendance(students):
    """View attendance of all students for a particular date."""
    date = input(f"Enter date (YYYY-MM-DD) [Enter for today]: ").strip()
    if not date:
        date = get_today()
    if not is_valid_date(date):
        print("Invalid date.")
        return

    print(f"\n--- Attendance on {date} ---")
    print(f"{'Roll':<10}{'Name':<25}{'Status':<10}")
    print("-" * 45)
    found = False
    for s in students:
        status = s.get("attendance", {}).get(date)
        if status:
            found = True
            display = "Present" if status == "P" else "Absent"
            print(f"{s['roll']:<10}{s['name']:<25}{display:<10}")
    if not found:
        print("No attendance records found for this date.")


def attendance_menu(students):
    while True:
        print("\n===== Attendance Marking =====")
        print("1. Mark Attendance")
        print("2. View Daily Attendance")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            students = mark_attendance(students)
        elif choice == "2":
            view_daily_attendance(students)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
    return students
