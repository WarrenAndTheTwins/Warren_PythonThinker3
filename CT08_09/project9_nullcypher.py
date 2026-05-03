FILE_NAME = "/workspaces/Warren_PythonThinker3/CT08_09/encrypted_note.txt"
import os
cwd = os.getcwd()
print(cwd)
with open(FILE_NAME, "r") as file:
    content = file.read()
content = content.lower()
content = content.replace(".","")
content = content.replace(",","")
new_variable = ""

# put into a list
wordlist = content.split(" ")
for word in wordlist:
    new_variable += word[0]
print(new_variable)
# retrieve first character, form into a new sentence