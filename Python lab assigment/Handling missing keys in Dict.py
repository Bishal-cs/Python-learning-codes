'''Handling missing keys in Python dictionaries'''

# Example dictionary
my_dict = {'name': 'Bishal', 'age': 18}

# Using .get() method to handle missing keys
name = my_dict.get('name', 'Key not found')   # Retrieves the value of 'name' if it exists
hobby = my_dict.get('hobby', 'Key not found') # Tries to retrieve 'hobby', returns default if missing

# Output results
print("Name:", name)
print("Hobby:", hobby)
