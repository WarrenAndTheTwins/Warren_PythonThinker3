"""
============================================================
Q2. Scrabble Game
============================================================
Write a PYTHON function that calculates the points
of a given word using a dictionary.

Requirements:
- Use a Python Dictionary for the letter points
- Ask for 5 words
- For each word, calculate the total score
- Print the score for each word in this format:
  Word #1:
  Score #1:

============================================================
"""

# ============================================================
# Step 1: Create the dictionary
# ============================================================
dictionary = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10

}


# ============================================================
# Step 2: Create a function calculate_score
# ============================================================
# - Loop through each letter in the word
# - Use the dictionary to find its value
# - Add up the total
# - Return the total score
# ============================================================

def calculate_score(dict, word):
    score = 0
    for letter in word:
        score += dict[letter]
    return score
# ============================================================
# Step 3: Ask for 5 words
# ============================================================
for i in range(5):
    word = input("Word #1:")
    print("Score #1: " + str(calculate_score(dictionary, word)))

# ============================================================
# Step 4: Print the score for each word in this format:
#         Word #1:
#         Score #1: