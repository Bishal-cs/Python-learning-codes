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


arr1 = [1, 2, 2, 1]  
arr2 = [5, 4, 3, 2]  
arr3 = [1, 3, 2]     

# Test the function with example arrays
print(is_monotonic(arr1))  
print(is_monotonic(arr2))  
