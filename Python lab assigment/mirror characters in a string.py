'''Python Dictionary to find mirror characters in a string.'''

# Create a dictionary for mirror characters
mirror_chars = {
    'A': 'A', 'b': 'd', 'd': 'b', 'H': 'H',
    'I': 'I', 'M': 'M', 'O': 'O', 'p': 'q',
    'q': 'p', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y'
}

# Function to find mirror characters in a string
def mirror_char(input_str):
    mirror = []
    for char in input_str:
        if char in mirror_chars:
            mirror.append(mirror_chars[char])  # Append the mirrored character
    return mirror

# Get user input
input_string = input("Enter a string: ")
mirror_characters = mirror_char(input_string)

# Print the result
if mirror_characters:
    print(f"Mirror characters in '{input_string}': {''.join(mirror_characters)}")
else:
    print(f"No mirror characters found in '{input_string}'.")
