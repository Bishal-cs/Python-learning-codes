'''Learning OOPS Concepts,
    Class and Objects. Class & Instance attributes '''
class Example:
    # Default Constructor
    # def __init__(self):
    #     pass

    # Parameterized Constructor
    def __init__(self, name, age):
        self.names = name
        self.ages = age
        print("Adding a new Student in database...")

    def Welcome(self):
        print("Welcome to the class", self.names)

    @staticmethod  # Decorator
    def Collage():
        print("Welcome to the Collage")

    def student_age(self):
        return self.ages

s1 = Example("Amit", 90)
s1.Welcome()
print("Your age is", s1.student_age())
s1.Collage
print("-------------------------------------------------------------------------------------------------------------------")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_average(self):
        sum = 0 
        for val in self.marks:
            sum += val
        avg = sum/len(self.marks)
        print("Hello", self.name, "your average is", avg)

s1 = Student("Stark", [90, 80, 70])
s1.get_average()

print("--------------------------------------------OOPS Abstraction and Encapsulatio-----------------------------------------------------")

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Your current balance is Rs.", self.balance)
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Your current balance is Rs.", self.balance)

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 1234)
acc1.debit(1000)
acc1.credit(50000)