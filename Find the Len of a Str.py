# Write a Python program to find the length of a given string without using any built-in functions.

def check_input(usr_inpt):
    count = 0
    for check in usr_inpt:
            count += 1
    return count

print(check_input("I am vishal das welcome to kolkata"))