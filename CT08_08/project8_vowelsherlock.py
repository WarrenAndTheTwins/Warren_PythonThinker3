FILE_NAME = "/workspaces/Warren_PythonThinker3/CT08_08/sherlock.txt"
import os
cwd = os.getcwd()
print(cwd)
vowel_count = 0
a = 0
e = 0
i = 0
o = 0
u = 0
with open(FILE_NAME, "r") as file:
    content = file.read()
content = content.lower()
print(content)
for character in content:
    if character in ["a", "e", "i", "o", "u"]:
        vowel_count += 1
        if character == "a":
            a += 1
        if character == "e":
            e += 1
        if character == "i":
            i += 1
        if character == "o":
            o += 1
        if character == "u":
            u += 1
print(vowel_count)

print("there are " + str(a) + " a's")
print("there are " + str(e) + " e's")
print("there are " + str(i) + " i's")
print("there are " + str(o) + " o's")
print("there are " + str(u) + " u's")
