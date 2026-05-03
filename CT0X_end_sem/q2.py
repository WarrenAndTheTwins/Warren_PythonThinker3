"""
============================================================
Q2. Review Text Analysis
============================================================
You are given a text file containing customer reviews.
The program must analyse the reviews and generate a rating.

Program Requirements:
- Read the contents of the file "reviews.txt"
- Count the total number of characters in the file
- Count how many reviews contain "good"
- Count how many reviews contain "bad"
- Calculate the percentage of good reviews
- Determine the overall rating:
    70% and above → Positive
    40% to 69% → Mixed
    Below 40% → Negative
- Save the results into "review_results.txt" and also print the results to the console

Note:
- The counting must be case-insensitive
- The percentage must be rounded to 2 decimal places
- If there are no valid reviews, the percentage should be 0

Print and save the result in this format:
    Review Text Analysis
    ------------------------------
    Total Characters: <number>
    Good Reviews: <number>
    Bad Reviews: <number>
    Percentage of Good Reviews: <value>%
    Overall Rating: <rating>

============================================================
"""

# ============================================================
# Step 1: Read file contents
# ============================================================
import os
cwd = os.getcwd()
character_count = 0
good_count = 0
bad_count = 0

FILE_NAME = "/workspaces/Warren_PythonThinker3/CT0X_end_sem/reviews.txt"
with open(FILE_NAME, "r") as file:
    for character in file.read():
        character_count += 1
with open(FILE_NAME, "r") as file:
    for line in file.readlines():
        line = line.lower()
        if "good" in line:
            good_count += 1
        elif "bad" in line:
            bad_count += 1
        else:
            continue
percentage = round(good_count * 100 / (bad_count + good_count) * 100)
percentage = percentage / 100
if percentage >= 70:
    general = "good"
elif percentage >= 40:
    general = "mixed"
else:
    general = "bad"
with open("/workspaces/Warren_PythonThinker3/CT0X_end_sem/review_results.txt", "w") as file:
    file.write("total num characters: " + str(character_count) + "\n good reviews: " + str(good_count) + "\n bad reviews: " + str(bad_count) +"\n percentage good: " + str(percentage) + "%" + "\n general review: " + general)
print("total num characters: " + str(character_count) + 
    "\n good reviews: " + str(good_count) + 
    "\n bad reviews: " + str(bad_count) +
    "\n percentage good: " + str(percentage) + "%" +
    "\n general review: " + general)
# ============================================================
# Step 3: Count characters and good or bad reviews
# ============================================================



# ============================================================
# Step 4: Calculate percentage and rating
# ============================================================



# ============================================================
# Step 5: Write results to file
# ============================================================



# ============================================================
# Step 6: Print results to console
# ============================================================