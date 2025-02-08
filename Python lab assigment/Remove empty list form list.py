'''Python - Remove empty List from List.'''

# Function to remove empty lists from a list
def remove_empty_lists(input_list):
    return [sublist for sublist in input_list if sublist]

# Example usage
nested_list = [1, [], 2, [], 3, [], [4, 5], [], [6]]
result = remove_empty_lists(nested_list)
print("List after removing empty lists ::", result)