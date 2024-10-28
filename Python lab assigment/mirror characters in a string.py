'''Python Dictionary to find mirror characters in a string.'''

# Create a dictionary for mirror characters
mirror_chars = {
    'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H',
    'I': 'I', 'M': 'M', 'O': 'O', 'p': 'q',
    'q': 'p', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y'
}

def mirror_char(input_str):
    mirror = []
    for char in input_str:
        if char == mirror_char:
            mirror.append(char)
    return

input_string = input("Enter a string: ")
mirror_characters = mirror_char(input_string)

if mirror_characters:
    print(f"Mirror characters in '{input_string}': {mirror_characters}")
else:
    print(f"No mirror characters found in '{input_string}'.")
