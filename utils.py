"""
utils.py
Helper functions for AttendTrack - Student Attendance System
"""

from datetime import datetime


def is_valid_roll(roll):
    try:
        return int(roll) > 0
    except ValueError:
        return False


def is_valid_date(date_str):
    """Validate date in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_today():
    """Return today's date as YYYY-MM-DD string."""
    return datetime.now().strftime("%Y-%m-%d")


def search_student_by_roll(students, roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def search_student_by_name(students, name):
    name = name.lower()
    return [s for s in students if name in s["name"].lower()]


def calculate_attendance_percentage(student):
    """Calculate attendance percentage for a student."""
    records = student.get("attendance", {})
    if not records:
        return 0.0
    total_days = len(records)
    present_days = sum(1 for status in records.values() if status == "P")
    return round((present_days / total_days) * 100, 2) if total_days > 0 else 0.0


def count_present_absent(student):
    """Count present and absent days."""
    records = student.get("attendance", {})
    present = sum(1 for status in records.values() if status == "P")
    absent = sum(1 for status in records.values() if status == "A")
    return present, absent
