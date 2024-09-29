# Write a Python program to count the number of vowels in a given string.

def check_vowel(sring_sentnce):
    vowels = "aeiouAEIOU"   # define our vowels to check them 
    cont = 0
    for char in sring_sentnce:
        if char in vowels:
            print(char,end='')
            cont +=1 
    return cont

print(check_vowel("Birendra Nagar"))