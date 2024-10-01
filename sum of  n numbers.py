# WAP To find the sum of first n natural numbers using for While Loop and find factorial 

n = int(input("Enter a number: "))
s = 0
f = 1
i = 1
while i <= n:
    s += i
    f *= i
    i += 1
print("The sum of first", n, "natural numbers is", s)
print("The factorial of", n, "is", f)