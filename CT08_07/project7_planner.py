# first create the text file
# then make the append fuinction using text.write  append way
# then make the delete via a list that is in the write lines so you can change it around
# to mark a task as done, add a [DONE] after the append thing also to add tasks, just add to the list, which is ez
#that's basically it tbh

## Task 1: Display a Menu
import os
cwd = os.getcwd()
print(cwd)
FILE_NAME = "/workspaces/Warren_PythonThinker3/CT08_07/tasks.txt"
menu = """
Menu:
1: create new tasks file
2: add new task
3: look at tasks
4: delete task
5: toggle doneness
6: exit
enter your choice:
"""
def write_new_task_file():
    with open(FILE_NAME, "w") as file:
        file.write("Task list:")

def create_new_file():
    if os.path.exists(FILE_NAME):
        while True:
            print("file already exists")
            option_y_n = input("overwrite? (y/n): ").lower().strip()
            if option_y_n in ["y", "n"]:
                if option_y_n == "y":
                    write_new_task_file()
                break
            else:
                print("uhh thats not right try again")
    else:
        write_new_task_file()

def view_all_tasks():
    with open(FILE_NAME, "r") as file:
        content = file.readlines()
        if len(content) == 1:
            print("no tasks sorry")
        else:
            for i in range(len(content)):
                if i < 1:
                    print(content[i])
                else:
                    print(str(i) +": "+ content[i])

def add_tasks():
    task = input("gimme gimme taskkkkk:\n")
    with open(FILE_NAME, "a") as file:
        file.write("\n" + task)
        print("task added successfully!!!!")

def print_menu():
    choice = input(menu) # return a string
    return choice

def delete_task():
    with open(FILE_NAME, "r") as file:
        task_list = file.readlines()
        for i in range(len(task_list)):
            if i == 0:
                continue
            else:
                print(str(i) + ":" + task_list[i], end = "")
        print("\n" + "-" * 30)
        del_num = input("which task do u want to delete\n")
        if not del_num.isdigit():
            print("needs to be digit")
        else:
            del_num = int(del_num)
            if del_num < 0 or del_num > len(task_list) - 1:
                print("number must be between one and" + len(task_list) - 1)
            else:
                del task_list[del_num]
                with open(FILE_NAME, "w") as file:
                    file.writelines(task_list)
                print("deleted successfully")

def toggle_doneness():
    with open(FILE_NAME, "r") as file:
        task_list = file.readlines()
        for i in range(len(task_list)):
            if i == 0:
                continue
            else:   
                print(str(i) + ":" + task_list[i], end = "")
        print("\n" + "-" * 30)
        done_num = int(input("which task do u want to toggle if done or not\n"))
        task = task_list[done_num]
        if "[DONE]" in task: 
            task = task.replace("[DONE]", "")
        else:
            task = task.strip() + "" + "[DONE]"
        task_list[done_num] = task
        with open(FILE_NAME, "w") as file:
            file.writelines(task_list)
while True:
    choice = print_menu()
    # if it is not digit, you will get them to input a digit
    # the digit is between 1 to 6
    if not choice.isdigit():
        print("The input should be a digit between 1 - 6")
        continue
    elif int(choice) > 6 or int(choice) < 1:
        print("The input should be between 1 - 6")
        continue
    else:
        choice = int(choice)
        if choice == 1:
            create_new_file()
        elif choice == 2:
            add_tasks()
        elif choice == 3:
            view_all_tasks()
        elif choice == 4: 
            delete_task()
        elif choice == 5:
            toggle_doneness()
        elif choice == 6:
            print("Goodbye. Thank you for using this task service. Please rate 5 stars!")
            break
# function for delete_task >>ask for the task number, delete that task
# >>> retrieve all the task from the file >> put into a list.
# delete the specific item from the list >> del() # index
# save the entire list back into the file

# mark a task as done
# function mark_task_done()
# read the file, put into a list
# ask user to select the task to set as done
# check if already done. ask again
# else, we will set as done (append the word done)
# save it back into the file