answer_key = ["A", "B", "B", "D"]  
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}

def grade_all_students(student_answers, answer_key):
    quiz_scores = {}
    for name, answers in student_answers.items():
        temp_score = 0
        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                temp_score += 1
        quiz_scores[name] = temp_score/len(answer_key) * 100
    return quiz_scores
quiz_scores = grade_all_students(student_answers, answer_key)

def calculate_average_score(quiz_scores):
    sum = 0
    for _, score in quiz_scores.items():
        sum += score
    return sum/len(quiz_scores)
def find_highest_scorer(quiz_scores):
    highest_scorers = []
    max_score = 0
    for _, score in quiz_scores.items():
        if score > max_score:
            max_score = score
    for name, score in quiz_scores.items():
        if score == max_score:
           highest_scorers.append(name)
    return highest_scorers
def display_results(quiz_scores):
    for name, score in quiz_scores.items():
        print(f"{name} : {score}")

def menu_system():
    res = ""
    while True:
        print("Quiz Grading System Menu")
        print("1: Grade All Students")
        print("2: Calculate Class Average")
        print("3: Find Highest Scorer(s)")
        print("4: Print All Results")
        print("5: Exit")
        res = int(input("Please choose your option"))
        if res == 5:
            break
        elif res == 1:
            quiz_scores = grade_all_students(student_answers, answer_key)
        elif res == 2:
            if len(quiz_scores) == 0:
                print("Please first grade students")
            else:
                class_average = calculate_average_score(quiz_scores)
                print("The average is " + class_average)
        elif res == 3:
            if len(quiz_scores) == 0:
                print("Please first grade students")
            else:
                highest_scorer = find_highest_scorer(quiz_scores)
                print("The highest scorer(s) is: ")
                for scorer in highest_scorer:
                    print(scorer)
        elif res == 4:
            if len(quiz_scores) == 0:
                print("Please first grade students")
            else:
                display_results(quiz_scores)
        else: 
            break

menu_system()