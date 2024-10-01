# Write a program to idntify the char is digit,space,spacial-char, or alphabet and print this:

def identify_character(input_str):
    for char in input_str:
        if char.isdigit():
            print(f"The character '{char}' is a digit.")
        elif char.isalpha():
            print(f"The character '{char}' is an alphabet.")
        elif char.isspace():
            print(f"The character '{char}' is a space.")
        else:
            print(f"The character '{char}' is a special character.")

input_str = input("Enter a string: ")
identify_character(input_str)