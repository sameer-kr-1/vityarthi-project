"""
reports.py
Module 3: Attendance Reports & Analytics
"""

from utils import (
    calculate_attendance_percentage,
    count_present_absent,
    search_student_by_name,
    search_student_by_roll,
    is_valid_roll
)


def show_individual_report(students):
    roll = input("Enter Roll Number: ").strip()
    if not is_valid_roll(roll):
        print("Invalid roll number.")
        return
    student = search_student_by_roll(students, int(roll))
    if not student:
        print("Student not found.")
        return

    present, absent = count_present_absent(student)
    total = present + absent
    perc = calculate_attendance_percentage(student)

    print("\n--- Individual Attendance Report ---")
    print(f"Name           : {student['name']}")
    print(f"Roll           : {student['roll']}")
    print(f"Total Days     : {total}")
    print(f"Present        : {present}")
    print(f"Absent         : {absent}")
    print(f"Percentage     : {perc}%")

    if total > 0:
        print("\nDetailed Records:")
        print(f"{'Date':<15}{'Status':<10}")
        print("-" * 25)
        for date in sorted(student.get("attendance", {}).keys()):
            status = "Present" if student["attendance"][date] == "P" else "Absent"
            print(f"{date:<15}{status:<10}")


def show_class_summary(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Class Attendance Summary ---")
    print(f"{'Roll':<10}{'Name':<22}{'Present':<10}{'Absent':<10}{'%':<8}")
    print("-" * 60)

    low_attendance = []
    for s in sorted(students, key=lambda x: x["roll"]):
        present, absent = count_present_absent(s)
        perc = calculate_attendance_percentage(s)
        print(f"{s['roll']:<10}{s['name']:<22}{present:<10}{absent:<10}{perc:<8.2f}")
        if perc < 75 and (present + absent) > 0:
            low_attendance.append((s["name"], s["roll"], perc))

    if low_attendance:
        print("\n*** Students with Attendance below 75% ***")
        for name, roll, perc in low_attendance:
            print(f"  {name} (Roll {roll}) - {perc}%")


def show_low_attendance(students, threshold=75):
    print(f"\n--- Students with Attendance < {threshold}% ---")
    found = False
    for s in students:
        perc = calculate_attendance_percentage(s)
        present, absent = count_present_absent(s)
        if (present + absent) > 0 and perc < threshold:
            found = True
            print(f"Roll: {s['roll']} | {s['name']} | {perc}%")
    if not found:
        print("No students found below the threshold.")


def search_by_name(students):
    name = input("Enter name to search: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    results = search_student_by_name(students, name)
    if not results:
        print("No matching students.")
        return
    print(f"\n--- Search Results ---")
    for s in results:
        perc = calculate_attendance_percentage(s)
        print(f"Roll: {s['roll']} | {s['name']} | Attendance: {perc}%")


def reports_menu(students):
    while True:
        print("\n===== Attendance Reports =====")
        print("1. Individual Student Report")
        print("2. Class Summary")
        print("3. Low Attendance Students (<75%)")
        print("4. Search Student by Name")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_individual_report(students)
        elif choice == "2":
            show_class_summary(students)
        elif choice == "3":
            show_low_attendance(students)
        elif choice == "4":
            search_by_name(students)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
