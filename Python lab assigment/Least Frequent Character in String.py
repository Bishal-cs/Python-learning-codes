'''Python - Least Frequent Character in String.'''

# Sample string
text = "sample string with repeated characters"

# Step 1: Initialize an empty dictionary to store character counts
frequency = {}

# Step 2: Count the frequency of each character
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Step 3: Find the least frequent character by iterating through the dictionary
least_frequent = None
min_count = float('inf')  # Start with an infinitely high value

for char, count in frequency.items():
    if count < min_count:
        min_count = count
        least_frequent = char

print(f"The least frequent character is: '{least_frequent}' with a count of {min_count}")
