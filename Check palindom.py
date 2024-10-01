# WAP to check if a list contains a palindom of elements.(Hint: use copy() method).

list = []
list.append(input("Enter a palindome : "))
n1 = list

n1.reverse()
if list == n1:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")