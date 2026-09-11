#To solve the problem statement
    # 1 - Input of users
    # 2 - Rough logic
    # 3 - Test the code

#Problem Statement - Create a table of 2

user_input = int(input("Enter a number: "))
print("printing the table")

print(f"{user_input}*1 = {user_input*1}")
print(f"{user_input}*2 = {user_input*2}")
print(f"{user_input}*3 = {user_input*3}")
print(f"{user_input}*4 = {user_input*4}")
print(f"{user_input}*5 = {user_input*5}")
print(f"{user_input}*6= {user_input*6}")
print(f"{user_input}*7 = {user_input*7}")
print(f"{user_input}*8 = {user_input*8}")
print(f"{user_input}*9 = {user_input*9}")
print(f"{user_input}*10 = {user_input*10}")

# What does "f" means : - ----- :
# The "formatting" tells python that "I want to put variables inside this text"
#
# Example :-------:
# name = "Akshay"
# print(f"Hello {name}")
# Output will be:
# Hello Akshay
#
# Difference between {user_input} and {user_input*1} : ----------- :
#
# user_input means - give me the value stored in user_input
# User_input*1 means - Take the value stored in user_input and multiply it by 1
#
# Example - {user_input} = 8 , it will print 8
# Example - {user_input*1} = 8 * 1 = 8
#
# Anything inside { } is processed by Python.
# Anything outside { } is generally printed as normal text.