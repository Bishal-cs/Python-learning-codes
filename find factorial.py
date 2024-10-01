# WAF to Find the factorial of n numbers

def fact(n):
    i = 1
    f = 1
    while i <= n:
        f *= i 
        i += 1
    return f

i = int(input("Enter a number: "))
f = fact(i)
print(f)