'''Python - Remove Tuples of Length K'''

# Function to remove tuples of a specific length from a list
def remove_tuples_of_length_k(input_list, k):
    # Create and return a new list with tuples whose length is not equal to k
    return [tup for tup in input_list if len(tup) != k]

# Example usage
nested_tuples = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10), (11, 12)]

# Get user input for the length to remove
k = int(input("Enter the length :: "))

# Call the function and store the result
result = remove_tuples_of_length_k(nested_tuples, k)

# Print the resulting list
print("List after removing tuples of length", k, ":", result)
