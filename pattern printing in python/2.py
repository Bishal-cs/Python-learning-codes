# print the number pyramid 
def Number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print(j+1, end="")
        print()

num_row = int(input("Enter The number: "))

Number_pyramid = (num_row)