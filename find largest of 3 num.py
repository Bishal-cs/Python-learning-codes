# Write a program to find the largest number in 3 numbers:

N1 = int(input("Enter one number: "))
N2 = int(input("Enter second number: "))
N3 = int(input("Enter third number: "))
if (N1>N2 and N1>N3):
    print("The greatest number is: ",N1)
elif (N2>N1 and N2>N3):
    print("The greatest number is: ",N2)
else:
    print("The greatest number is: ",N3)    