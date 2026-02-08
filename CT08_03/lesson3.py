# students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# students["John"]= 1
# students["Kok Seng"]= 1
# students["Timothy"]= 1
# print(f"Student Grades: {students}")

# # Try using an input() to ask which student you want to check the score for?
# # What happens if you try accessing a student that does not exist?

# grade = input("who?")
# if grade in students:
#     whograde = students [grade]
#     print(whograde)
# else:
#     print("poo")

# Lesson 3 - Restaurant Menu

## Task 1: Display the Menu
# **Display the Menu**

# Write a program that:​
# - Creates a dictionary with at least 5 menu items and their prices.​
# - Prints all the items in the menu with their prices, one item per line.

# ## Task 2: Check if item exists
# **Take the Customer’s Order and Check if it Exists**

# Asks the customer for the item they want to order.​

# Checks if the item exists in the menu.​
# - If it exists: Print the item and its price.​
# - If it does not exist: Display a message saying the item is unavailable.​

# Keep asking again and again until customer says “no more”

# ## Task 3: Add ordered item to another Dictionary
# **Add the Ordered Item to Another Dictionary**

# Extend your program so that it:​
# - If the item exists, asks the customer if they want to add it to their order.​
# If the customer says "yes," ​
# add the item and its price to a separate dictionary that stores the customer’s order.​
# If the customer says "no," ​
# display a message confirming the item was not added.

# ## Task 4: Display Order Summary and Total Cost
# **Display the Order Summary and Total Cost**

# After the customer finishes ordering:​
# - Display all the items in their order with the prices.​
# - Calculate and display the total cost of the order.

# ## Challenge 1: Wallet Feature
# Assign a wallet balance to the customer (e.g., $10).​

# Before confirming an order, check if the total cost will exceed the customer’s wallet balance.​
# - If the total exceeds the wallet balance, display a message and do not add the item.​
# - If the total is within the wallet balance, confirm the order as usual and reduce the balance.

# menu = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5
# }
# order_list = []
# cost = 0
# print("Hi and welcome to skibidi slicers!")
# for item, price in menu.items():
#     print(f"{item}:{price}")
# while True:
#     order = input("what'd u like")
#     if order in menu: 
#         order_list.append(order)
#         print("ok nice. your order is ")
#         for i in order_list:
#             print (i)

#     else: 
#         if order == "quit":
#             print("great! your order is:")
#             for i in order_list:
#                 print (i)
#             print("it adds up to:")
#             for i in order_list:
#                 x = menu[i]
#                 cost += x
#             print (cost)
#             money = int(input("how much monies do u have?"))
#             if money >= cost: 
#                 print("nice! you have " + str(money - cost) + " dollars left")
#                 break
#             else:
#                 print("sry man, card declined. try removing smth")
#         elif order == "remove":
#             removed = input("what would you like to remove?")
#             order_list.remove(removed)
#             for i in order_list:
#                 print (i)
#         else:
#             print("sorry we don't have that here")
    
menu = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}
order_list = {}
cost1 = 0
print("Hi and welcome to skibidi slicers!")
for item, price in menu.items():
    print(f"{item}:{price}")
while True:
    order = input("what'd u like")
    if order in menu: 
        print(f"the price of {order} is {menu[order]}")
        sureness =  input("u sure? y/n")
        if sureness == "n":
            print("alright, not added")
        else:
            order_list[order] = menu[order]
            print("ok nice. your order is ")
            for item, cost in order_list.items():
                print (f"{item} : {cost}")

    else: 
        if order == "quit":
            print("great! your order is:")
            for item, price in order_list.items():
                print (f"{item}: {price}")
            print("it adds up to:")
            for item, price in order_list.items():
                 cost1 += price
            print (cost1)
            money = int(input("how much monies do u have?"))
            if money >= cost1: 
                print("nice! you have " + str(money - cost1) + " dollars left")
                break
            else:
                print("sry man, card declined. try removing smth")
        elif order == "remove":
            removed = input("what would you like to remove?")
            if removed in order_list:
                del order_list [removed]
                for i, j in order_list.items():
                    print(f"{i}: {j}")
            else:
                print("sorry, that item isn't in your order")
        else:
            print("sorry we don't have that here")