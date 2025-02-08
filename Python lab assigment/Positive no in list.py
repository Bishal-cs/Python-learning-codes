'''Python program to print positive numbers in a list.'''

# Function to print positive numbers from a list
def print_positive_numbers(numbers):
    print("Positive numbers in the list are :: ")
    for number in numbers:
        if number > 0:
            print(number, end=" ")

# Example usage
numbers_list = [-10, 15, 0, -5, 20, 25, -30, 5]
print_positive_numbers(numbers_list)
