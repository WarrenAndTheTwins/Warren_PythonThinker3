
# Quiz Auto-Marker
# You are building an auto-marker system for a multiple-choice quiz.
# The program must compare a student’s answers with the answer key.
# It should calculate the score, identify which questions were wrong, and assign a grade.

# Given Sample Data
# answer_key = ["B","D","A","A","C","B","C","D","B","A"]
# student_ans = ["B","D","C","A","C","B","C","A","B","A"]
  
# Function Requirements
# 1) score_quiz(key, ans)
# Takes two lists of equal length.
# Compares each answer in the same position.
# Returns the total number of correct answers.
# Example:

# score_quiz(answer_key, student_ans)
# # returns 8
  
# 2) wrong_questions(key, ans)
# Returns a list of question numbers (starting from 1) that were answered incorrectly.
# If all answers are correct, return an empty list [ ].
# Example:

# wrong_questions(answer_key, student_ans)
# # returns [3, 8]
  
# 3) grade(score, total) -> str
# Takes the student’s score and total number of questions total.
# Calculates percentage internally: (score / total) * 100.
# Returns:
# "A" if percentage ≥ 80%
# "B" if percentage ≥ 70%
# "C" if percentage ≥ 60%
# "D" otherwise
# Example:

# grade(8, 10)
# # returns "A"
  
# Coding Instructions:

# Your code should ask for input in the same order as the Test Cases below.
# The expected output for Test Case 1 & Test Case 2 has been provided to you. You can use these to check the correctness of your code.
# You are required to get the correct output for all 3 Test Cases.
# Test Cases:

# Test Case 1

# Answer Key: ["B","D","A","A","C","B","C","D","B","A"]

# Student Answers: ["B","D","C","A","C","B","C","A","B","A"]

# Expected Output:

# Score: 8

# Wrong Questions: [3, 8]

# Grade: A

# Test Case 2

# Answer Key: ["A","B","C","D"]

# Student Answers: ["A","B","C","D"]

# Expected Output:

# Score: 4

# Wrong Questions: []

# Grade: A

# Test Case 3

answer_key = ["B","D","A","A","C","B","C","D","B","A"]

student_answers = ["B","D","C","A","C","B","C","A","B","A"]

# Copy the template into your file:

# """
# ============================================================
# Q1. Quiz Auto-Marker
# ============================================================
# You are building an auto-marker system for a multiple-choice quiz.
# The program must compare a student's answers with the answer key.
# It should calculate the score, identify which questions were wrong, and assign a grade.

# - Write 3 functions:
#     1) score_quiz(key, ans)
#     2) wrong_questions(key, ans)
#     3) grade(score, total)
# - Do not change the function names or parameters.
# - After writing your functions, uncomment the test code at the bottom to test.

# ============================================================
# """

# # ============================================================
# # Step 1: Write function score_quiz(key, ans)
# # ============================================================
# # - key and ans are lists of equal length
# # - Compare answers at the same position
# # - Return total number of correct answers
# # ============================================================

def score_quiz(answer_key, student_answers):
    score = 0 
    counter = -1
    for ans in answer_key:
        counter += 1
        if ans == student_answers[counter]:
            score += 1
    return score

# # ============================================================
# # Step 2: Write function wrong_questions(key, ans)
# # ============================================================
# # - Return a list of question numbers (starting from 1) that are wrong
# # - If all answers are correct, return an empty list
# # ============================================================

def wrong_questions(answer_key, student_answers):
    counter = -1
    wrong = []
    for i in answer_key:
        counter += 1
        if i != student_answers[counter]:
            wrong.append(str(counter + 1))
    return wrong

# # ============================================================
# # Step 3: Write function grade(score, total)
# # ============================================================
# # - Compute percentage = (score / total) * 100
# # - Return:
# #     "A" if percentage >= 80
# #     "B" if percentage >= 70
# #     "C" if percentage >= 60
# #     "D" otherwise
# # ============================================================
def grade(score, total):
    score = score_quiz(answer_key, student_answers)
    percent = (score/total) *100 
    if percent >= 80:
        return "a"
    elif percent >= 70:
        return "b"
    elif percent >= 60:
        return "c"
    else:
        return "d"


# # ============================================================
# # Step 4: Main Code Testing
# # ============================================================
# # Uncomment after writing your functions

score = score_quiz(answer_key, student_answers)
wrong = wrong_questions(answer_key, student_answers)
final_grade = grade(score, len(answer_key))

print("Score:", score)
print("Wrong Questions:", wrong)
print("Grade:", final_grade)