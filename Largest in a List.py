# Write a Python program to find the largest number in a list.

numbers = [10, 20, 30, 40, 50]

max_value = numbers[0]

for i in range(1,len(numbers)):
    if numbers[i] > max_value:
        max_value = numbers[i]
print(max_value)

# -------------------------or--------------------------

def largest(num):
    return max(num)

print(largest(numbers))