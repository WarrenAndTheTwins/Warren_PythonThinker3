import os
cwd = os.getcwd()

with open("example.txt", "w") as file:
    file.write("potati")
lines = ["\npneumonoultramicroscopicsilicovolcanoconiosis", "\nchargoggagoggmanchauggagoggchaubunagungamaugg"]
with open("example.txt", "a") as file:
    file.write("\nbdkjjkdas")

    file.writelines(lines)

with open("example.txt", "r") as file:
    read_lines = file.readlines()
    for i in read_lines:
        print(i)