'''
For n= 3,
pattern:  3 3 3 2 2 2 1 1 1
          3 3 2 2 1 1 
          3 2 1
'''
n = int(input("Enter the number :: "))

for i in range(n, 0, -1):  
    for j in range(n, 0, -1):  
        print((str(j) + " ") * i, end="")  
    print()  