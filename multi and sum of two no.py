# Write a Python program to calculate the multiplication and sum of two numbers. If the product is less than or equal to 1000, return the product; otherwise, return their sum.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def calculate():
    multiplication = num1 * num2
    if multiplication <= 1000:
        return multiplication
    else: 
        sum = num1 + num2
        return sum

print("the two numbers multiplication is:",calculate())