import os
FILE_NAME = "/workspaces/Warren_PythonThinker3/CT08_12/results.txt"
cwd = os.getcwd()
scores = {

}
student_ranges = {
    "0-50": [],
    "51-70": [],
    "71-90": [],
    "91-100": []
}
with open(FILE_NAME, "r") as file:
    for line in file:
        stuff = line.split()
        name = stuff[0]
        grade = stuff[1]
        scores[name] = grade
    print(scores)

for key, value in scores.items():
    if value < 50:
        student_ranges["0-50"].append(key)
    elif value < 70:
        student_ranges["51-70"].append(key)
    elif value < 90:
        student_ranges["71-90"].append(key)
    else:
        student_ranges["91-100"].append(key)