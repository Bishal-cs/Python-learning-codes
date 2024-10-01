# Write a program to print the multipleacation Table using user input:

def print_multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

print_multiplication_table()