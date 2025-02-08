"""Python Program for cube sum of first n natural numbers"""

num = int(input("Enter the number :: "))
sum_cube = 0

# Using for loop print the sum of cube  
for i in range(1, num+1):
    sum_cube += i ** 3
    
print("The sum of cubes of the first", num, "natural numbers is :: ", sum_cube)