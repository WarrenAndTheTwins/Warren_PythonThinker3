# Lesson 5 - School Attendance System (SAS)

## Task 1: Create Student Database
# **Create the Initial Attendance Database​**

# - Create a dictionary to store the names of students and their attendance records.​
# - Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
# - (True for present, False for absent).​
# - This dictionary will serve as the database for all subsequent tasks.

attendance_dict = {
    "john": [True, False, True],
    "jane": [True, True, True],
    "bob": [False, False, True],
    "alice": [True, True, False],
    "sam": [True, True, True],
    "eve": [False, True, False],
    "tom": [True, False, False],
    "daisy": [True, True, True],
    "mike": [False, False, False],
    "lily": [True, False, True]
}


def take_attendance(attendance_dict):
    for student in attendance_dict:
        ans = input(f"Is {student} present? (y/n): ")
        while ans != "y" and ans != "n":
            ans = input("Invalid input. Please enter 'y' or 'n': ")
        if ans == 'y':
            attendance_dict[student].append(True)
        if ans == 'n':
            attendance_dict[student].append(False)

    return attendance_dict
def calculate_attendance_percentage(student_name, attendance_dict):
    student_attendance = attendance_dict[student_name]
    total_days = len(student_attendance)
    present_days = sum(student_attendance)
    percentage = (present_days / total_days * 100) if total_days > 0 else 0
    return percentage

take_attendance(attendance_dict)
