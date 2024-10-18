'''Python program to print even length words in a string.'''

def print_even_len_word(input_str):

    words = input_str.split()

    # Iterate through the words
    for word in words:
            # Check if the length of the word is even
            if len(word) % 2 == 0:
                print(word)


x = "This is a simple test string"

print_even_len_word(x)