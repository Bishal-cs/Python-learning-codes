def check_vowel_or_consonant(char):
    # Convert the character to lowercase
    char = char.lower()

    # Check if the character is a vowel
    if char in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

# Take user input
char = input("Enter a character: ")

# Check if the input is a single character
if len(char) == 1:
    print(check_vowel_or_consonant(char))
else:
    print("Please enter a single character.")