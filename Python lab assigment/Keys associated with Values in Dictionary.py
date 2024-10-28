'''Python - Keys associated with Values in Dictionary'''

my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
}
x = int(input("Enter the value :: "))
keys_with_value = [
    key for key,
        value in my_dict.items()
        if value == x
]
print(keys_with_value)
