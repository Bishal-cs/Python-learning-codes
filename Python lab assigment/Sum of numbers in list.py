'''Python - Sum of number digits in List.'''

# Function to find the sum of digits of each number in a list without built-in functions
def sum_of_digits_in_list(num_list):
    # List to store the sum of digits for each number
    sum_digits_list = []
    
    # Loop through each number in the list
    for num in num_list:
        sum_digits = 0
        original_num = num
        
        # Extract each digit manually using mathematical operations
        while num > 0:
            digit = num % 10  
            sum_digits += digit
            num = num // 10  
        
        sum_digits_list.append(sum_digits)
    
    return sum_digits_list

# Example list of numbers
num_list = [2, 4, 5, 9]

result = sum_of_digits_in_list(num_list)

print("Sum of digits for each number ::", result)

# Calculate and print the total sum of all digits manually
total_sum = 0
for digit_sum in result:
    total_sum += digit_sum

print("Total sum of digits:", total_sum)
