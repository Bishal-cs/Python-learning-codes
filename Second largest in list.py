# Write a Python program to find the second largest number in a list without using any built-in functions.

def find_second_largest(numbers):
    first = float('-inf')
    second = float('-inf')
    
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif number > second and number != first:
            second = number
    return second

numbers = [10, 20, 30, 40, 50]
second_largest = find_second_largest(numbers)
print("The second largest number is:", second_largest)
