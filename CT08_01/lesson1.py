# ## Recap 2: Variables & Mind map
# Use mindmap to think about the number of variables you need for
# the following. Then, create a program that does the following:

# You just had lunch at a sushi restaurant and have to calculate
# the total amount you have spent. Different coloured plates
# costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates,
# and 4 green plates. Calculate and print the total amount you
# have spent:

# red = input("red?")
# blue = input("blue?")
# green = input("green?")
# rcost = int(red) * 1
# bcost = int(blue) * 2
# gcost = int(green)* 3
# x = rcost + gcost + bcost
# print (x)

## Recap 3: Debugging Average Score Program
# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))

## Recap 4: If..elif..else & Flowchart
# Write a program that asks the user to input a score
# (as an integer) and then assigns a grade based on that score.
# Use the following grading scheme:

# If the score is 75 or higher, the grade is 'A'.
# If the score is between 60 and 74 (inclusive), the grade is 'B'.
# If the score is between 50 and 59 (inclusive), the grade is 'C'.
# Any score below 50 will be graded as 'Fail'.

# Use flowchart to draw out all decisions that are to be made
# before starting on your code.

# If..elif..else
grade = int(input("gimme ur number i hungy"))
if grade >= 75:
    print("A")
elif grade >= 60:
    print("B")
elif grade >= 50:
    print ("C")
else:
    print("YOU FAILURE YOU ABSOLUTE FAILURE NOONE ENJOYS YOUR PRESENCE UPON THIS EARTH YOU ANSWERED 15 THIS IS A HISTORY QUIZ YOU SAID THAT ABRAHAM LINCOLN STARTED THE BIG BANG YOU DIDNT EVEN SEE THE BACK SIDE IT HAD 99% OF THE QUESTIONS")