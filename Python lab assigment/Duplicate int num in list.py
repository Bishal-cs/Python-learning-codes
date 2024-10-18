'''Python - Program to print duplicates from a list of integers.'''

# define a function for check the duplicate No.
def duplicate_No_list(input_list):
    check = []
    duplicates = []

# using loop assign the value in "i"
    for i in range(len(input_list)):

        if input_list[i] in check:
            
            if input_list[i] not in duplicates:
                duplicates.append(input_list[i])
        else:
            check.append(input_list[i])

    print("Duplicates list of integers is :",duplicates)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 7, 4, 5]

duplicate_No_list(my_list)
