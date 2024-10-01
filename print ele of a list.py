# WAP to print the elements of a list using for loop[1,4,9,16,25,36,49,64,81,100] && sarch number "X"

l = [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number : "))
index = 0
for i in l:
    if (i == x):
        print("The number is present in the list", i, "at index", index)
    else:
        pass
    index += 1 