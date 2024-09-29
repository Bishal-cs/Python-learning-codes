# Write a Python program to accept a string from the user and display characters that are present at even index positions.

def even_index_chars(input_str):
    for i in range(0, len(input_str), 2):
        print(input_str[i],end='')

even_index_chars("Bishal") # enter your string sentence 