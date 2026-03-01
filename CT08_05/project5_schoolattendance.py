# Lesson 5 - School Attendance System (SAS)

## Task 1: Create Student Database
# **Create the Initial Attendance Database​**

# - Create a dictionary to store the names of students and their attendance records.​
# - Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
# - (True for present, False for absent).​
# - This dictionary will serve as the database for all subsequent tasks.

# attendance_dict = {
#     "john": [True, False, True],
#     "jane": [True, True, True],
#     "bob": [False, False, True],
#     "alice": [True, True, False],
#     "sam": [True, True, True],
#     "eve": [False, True, False],
#     "tom": [True, False, False],
#     "daisy": [True, True, True],
#     "mike": [False, False, False],
#     "lily": [True, False, True]
# }

# def take_attendance(attendance_dict):
#     for student in attendance_dict:
#         ans = input(f"Is {student} present? (y/n): ")
#         while ans != "y" and ans != "n":
#             ans = input("Invalid input. Please enter 'y' or 'n': ")
#         if ans == 'y':
#             attendance_dict[student].append(True)
#         if ans == 'n':
#             attendance_dict[student].append(False)

#     return attendance_dict
# def calculate_attendance_percentage(student_name, attendance_dict):
#     student_attendance = attendance_dict[student_name]
#     total_days = len(student_attendance)
#     present_days = sum(student_attendance)
#     percentage = (present_days / total_days * 100) if total_days > 0 else 0
#     return percentage

# def notify_low_percentage(attendance_dict, threshold):
#     low_attendance = []
#     for name in attendance_dict:
#         student_percentage = calculate_attendance_percentage(name, attendance_dict)
#         if student_percentage < threshold:
#             low_attendance.append(name)
#     return low_attendance

# def menu():

#     while True:
#         print("School Attendance System")
#         print("1: view attendance")
#         print("2: take attendance")
#         print("3: Given a student 𝘯, find the attendance percentage of that student. Enter in lowest case.")
#         print("4: look at low attendance students")
#         selection = input("Enter selection :)")
#         if int(selection) == 1:
#             print(attendance_dict)
#         elif int(selection) == 2:
#             take_attendance(attendance_dict)
#         elif int(selection) == 3:
#             student_picked = input("Which student?")
#             if student_picked in attendance_dict:
#                 that_attendance = calculate_attendance_percentage(student_picked, attendance_dict)
#                 print(that_attendance)
#             else:
#                 print("nuh uh")
#         elif int(selection) == 4:
#             print(notify_low_percentage(attendance_dict, 50))
#         else:
#             break


# menu()

# jonny : [True, True, True]
# sally : [False, False, True]
# becky : [False, True, True]
# mark : [True, True, True]
# linda : [False, False, False]