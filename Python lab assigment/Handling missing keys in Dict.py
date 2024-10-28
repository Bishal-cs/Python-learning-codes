'''Handling missing keys in Python dictionaries'''

def get_value(dictionary, key, default_value=None):
    for k in dictionary.keys():
        if k == key:
            return dictionary[k]
    return default_value  

my_dict = {'a': 1, 'b': 2, 'c': 3}
value = get_value(my_dict, 'd', 'default_value')
print("Manual Key Existence Check:", value) 


# 2. Manual Exception Handling (Without KeyError)
def get_value_without_exception(dictionary, key, default_value=None):
    # Manually check and handle the missing key
    for k in dictionary:
        if k == key:
            return dictionary[k]
    print(f"Key '{key}' not found, returning default value.")
    return default_value

# Example usage
person = {'name': 'Alice', 'age': 30}
age = get_value_without_exception(person, 'address', 'No Address')
print("Manual Exception Handling:", age)  # Output: 'No Address'


# 3. Manual Dictionary Update for Missing Keys
def add_key_if_missing(dictionary, key, default_value):
    # Manually add the key with default value if missing
    key_exists = False
    for k in dictionary:
        if k == key:
            key_exists = True
            break
    if not key_exists:
        dictionary[key] = default_value
    return dictionary

# Example usage
my_dict = {'p': 5, 'q': 6}
add_key_if_missing(my_dict, 'r', 100)
print("Manual Dictionary Update:", my_dict)  # Output: {'p': 5, 'q': 6, 'r': 100}


# 4. Handling Nested Dictionaries (Recursive Search)
def find_key_in_nested_dict(d, key, default_value=None):
    # Recursively search for the key in a nested dictionary
    for k, v in d.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            result = find_key_in_nested_dict(v, key, default_value)
            if result is not None:
                return result
    return default_value

# Example usage
nested_dict = {'level1': {'level2': {'level3': 10}}}
value = find_key_in_nested_dict(nested_dict, 'level3', 'not found')
print("Handling Nested Dictionaries:", value)  # Output: 10


# 5. Custom Dictionary Class to Handle Missing Keys
class CustomDict(dict):
    def __init__(self, default_value=None):
        self.default_value = default_value
        super().__init__()

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        else:
            return self.default_value

my_custom_dict = CustomDict(default_value="Not Found")
my_custom_dict['a'] = 10
print("Custom Dictionary Class - Existing Key:", my_custom_dict['a']) 
print("Custom Dictionary Class - Missing Key:", my_custom_dict['b'])  
