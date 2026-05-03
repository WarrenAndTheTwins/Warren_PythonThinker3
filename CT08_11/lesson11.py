FILE_NAME = "/workspaces/Warren_PythonThinker3/CT08_11/encrypted.txt"
import random
import os
cwd = os.getcwd()
def caesar_decode(letter_gap, deen):
    with open(FILE_NAME, "r") as file:
        content = file.read()
        for character in content:
            if deen == "decrypt":
                print(caesar_decode_singlechar(character, letter_gap, "decrypt"), end = "")
            elif deen == "encrypt":
                print(caesar_decode_singlechar(character, letter_gap, "encrypt"), end = "")
    print("\n")
def caesar_decode_singlechar(char, letter_gap, deen):
    ascii = ord(char)
    ascii -= 32
    if deen == "decrypt":
        ascii -= letter_gap
        ascii = ascii % 95
        ascii += 32
        return(chr(ascii))
    elif deen == "encrypt":
        ascii += letter_gap
        ascii = ascii % 95
        ascii += 32
        return(chr(ascii))

for i in range(-95, 96):
    caesar_decode(i, "decrypt")
    
## Task 2: Encrypt/ Decrypt a single sentence

### Encrypts or decrypts a full sentence by shifting each character.

# `caesar_shift_sentence()`
# - **Arguments**: 
#   - **sentence (str)**: The sentence to shift.
#   - **key (int)**: The encryption/decryption key.
#   - **mode (str)**: "encrypt" or "decrypt".

# - **Return Value**:
#   - **str**: The shifted sentence.



