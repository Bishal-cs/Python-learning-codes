'''Python Program to check if given array is Monotonic.'''

# Function to check if an array is monotonic
def is_monotonic(arr):
    # Assume the array is both non-increasing and non-decreasing at the start
    is_increasing = True
    is_decreasing = True
    
    # Iterate through the array to check the conditions
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            is_decreasing = False  
        if arr[i] > arr[i + 1]:
            is_increasing = False  
    
    # If it's either non-increasing or non-decreasing, it's monotonic
    return is_increasing or is_decreasing

element = int(input("Enter the number of elements in the array :: "))
arr1 = []
for i in range(element):
    print("Enter", i+1, "element of the array :: ",end=" ")
    arr1.append(int(input()))
print("The elements are :: ",is_monotonic(arr1))  
