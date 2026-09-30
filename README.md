# AttendTrack – Student Attendance Management System

## Overview
AttendTrack is a complete menu-driven Python application for managing student attendance.  
It allows teachers/admins to register students, mark daily attendance, and generate detailed reports.

Developed for **CSE1021 – Introduction to Problem Solving and Programming** under the VITyarthi Build Your Own Project guidelines.

## Features

### Module 1: Student Management
- Add, View, Update, Delete students
- View detailed attendance history of a student

### Module 2: Attendance Marking
- Mark attendance for all students or a single student
- Support for any date (default: today)
- View daily attendance sheet

### Module 3: Reports & Analytics
- Individual student attendance report
- Class-wise summary with percentage
- List of students with low attendance (< 75%)
- Search student by name

## Technologies Used
- Python 3
- Standard libraries only (`json`, `os`, `datetime`)
- No external packages required

## Project Structure
```
AttendTrack/
├── main.py
├── student_manager.py
├── attendance_module.py
├── reports.py
├── utils.py
├── data/
│   └── students.json
├── README.md
├── statement.md
└── requirements.txt
```

## How to Run
```bash
cd AttendTrack
python3 main.py
```

## Testing Steps
1. Add a few students
2. Mark attendance for today (or any date)
3. View daily attendance
4. Check Individual Report and Class Summary
5. Check Low Attendance list
6. Exit and re-run → data persists

## Author
CSE1021 Project – VITyarthi Build Your Own Project
