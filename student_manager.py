"""
student_manager.py
Module 1: Student Management (CRUD)
"""

import json
import os
from utils import is_valid_roll, search_student_by_roll

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "students.json")


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def save_students(students):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


def add_student(students):
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ").strip()
    if not is_valid_roll(roll):
        print("Invalid roll number.")
        return students

    roll = int(roll)
    if search_student_by_roll(students, roll):
        print(f"Student with roll {roll} already exists!")
        return students

    name = input("Enter Student Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return students

    student = {
        "roll": roll,
        "name": name,
        "attendance": {}      # date: "P" or "A"
    }
    students.append(student)
    save_students(students)
    print(f"Student {name} (Roll: {roll}) added successfully!")
    return students


def view_all_students(students):
    if not students:
        print("\nNo students found.")
        return

    print("\n--- All Students ---")
    print(f"{'Roll':<10}{'Name':<25}{'Total Days':<12}{'Present':<10}{'%':<8}")
    print("-" * 65)
    for s in students:
        present, absent = 0, 0
        records = s.get("attendance", {})
        for status in records.values():
            if status == "P":
                present += 1
            else:
                absent += 1
        total = present + absent
        perc = round((present / total) * 100, 2) if total > 0 else 0.0
        print(f"{s['roll']:<10}{s['name']:<25}{total:<12}{present:<10}{perc:<8.2f}")


def view_student(students):
    roll = input("Enter Roll Number: ").strip()
    if not is_valid_roll(roll):
        print("Invalid roll number.")
        return
    student = search_student_by_roll(students, int(roll))
    if not student:
        print("Student not found.")
        return

    print("\n--- Student Details ---")
    print(f"Roll : {student['roll']}")
    print(f"Name : {student['name']}")
    records = student.get("attendance", {})
    if not records:
        print("No attendance records yet.")
    else:
        print("\nAttendance Records:")
        print(f"{'Date':<15}{'Status':<10}")
        print("-" * 25)
        for date in sorted(records.keys()):
            status = "Present" if records[date] == "P" else "Absent"
            print(f"{date:<15}{status:<10}")


def update_student(students):
    roll = input("Enter Roll Number to update: ").strip()
    if not is_valid_roll(roll):
        print("Invalid roll number.")
        return students
    student = search_student_by_roll(students, int(roll))
    if not student:
        print("Student not found.")
        return students

    new_name = input(f"Enter new name (current: {student['name']}): ").strip()
    if new_name:
        student["name"] = new_name
        save_students(students)
        print("Student updated successfully!")
    return students


def delete_student(students):
    roll = input("Enter Roll Number to delete: ").strip()
    if not is_valid_roll(roll):
        print("Invalid roll number.")
        return students
    student = search_student_by_roll(students, int(roll))
    if not student:
        print("Student not found.")
        return students

    confirm = input(f"Delete {student['name']}? (y/n): ").lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted.")
    return students


def student_menu(students):
    while True:
        print("\n===== Student Management =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Details")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            students = add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            view_student(students)
        elif choice == "4":
            students = update_student(students)
        elif choice == "5":
            students = delete_student(students)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
    return students
