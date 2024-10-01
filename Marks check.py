# Write a Python program that takes the marks of a student as input and assigns a grade based on the following criteria:

marks = int(input("Enter your marks: "))
m = marks # assign marks to m 
if  (m>=90):
    print("Your grade is E")
elif (m>=80 and m<=90):
    print("Your grade is O")
elif (m>=70 and m<=80):
    print("Your grade is A")
elif (m>=60 and m<=50):
    print("Your grade is B")
elif (m>=50 and m<=40):
    print("Your grade is C")
elif (m>=40 and m<=35):
    print("Your grade is F")
else:
    print("Fail,Try Next Year")