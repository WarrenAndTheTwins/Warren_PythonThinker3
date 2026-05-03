import random
user_list = {

}
def menu():
    print("Welcome to the Chargoggagoggmanchauggagoggchaubunagungamaugg Service! \n 1: New User \n 2: Change Password \n 3: Sign in \n 4: View Data \n 5: Exit")
    choice = input("")
    return choice

def gen_password():
    temp_password = ""
    for i in range(12):
        temp_password += chr(random.randint(33, 122))
    return temp_password

def create_user(user_list):
    username = input("username?")
    print(username + ", your password is:")
    password = gen_password()
    print(password)
    user_list[username] = password

def login(user_list):
    authorization = False
    username1 = input("username?")
    password1 = input("password?")
    if user_list[username1] == password1:
        authorization = True
    return authorization

def view_user_data(user_list):
    asterisked_password = ""
    for user in user_list:
        for character in user_list[user]:
            asterisked_password += "*"
        print(user + ": " + asterisked_password)

def change_password():
    username1 = input("username?")
    password1 = input("password?")
    if user_list[username1] == password1:
        newpassword = gen_password()
        print("your new password is " + newpassword)
        user_list[username1] = newpassword

while True:
    choice = menu()
    if choice == "1":
        create_user(user_list)
    elif choice == "2":
        change_password(user_list)
    elif choice == "3":
        if login(user_list):
            print("You're in!")
    elif choice == "4":
        view_user_data(user_list)
    elif choice == "5":
        print("bye!")
        break
    else:
        print("not right! try again")