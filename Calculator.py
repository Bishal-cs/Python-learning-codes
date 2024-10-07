# Calculator Program in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    calculator()