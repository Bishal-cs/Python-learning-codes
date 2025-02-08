# Function to print full pyramid pattern
def Full_pyramid(n):
    for i in range(1, n+1):
        # for this print spaces
        for j in range(n - i):
            print(" ", end="")
        # this loop for print *
        for k in range(1, 2*i):
            print("*", end="")
        print()

# input the number 
n = int(input("Enter Number: "))

Full_pyramid(n)