class bank_account:
    def __init__(self, balance ):#CONSTRUCTOR
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount      
    def __add__(self, other):
        return bank_account(self.balance + other.balance)
obj1=bank_account(1000)
obj2=bank_account(2000)
obj3=obj1+obj2
print(obj3.balance) 
#program successfully executed
#Create a class calculator requirements are  num1 and 2, define 3 parent classes naming add, sub, mult
class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# Each class now inherits from 'calculator'
class add(calculator):
    def add(self):
        return self.num1 + self.num2

class sub(calculator):
    def sub(self):
        return self.num1 - self.num2

class mult(calculator):
    def mult(self):
        return self.num1 * self.num2

# Now you pass the numbers to the operation objects directly
obj1 = add(10, 20)
obj2 = sub(10, 20)
obj3 = mult(10, 20)

print(obj1.add())
print(obj2.sub())
print(obj3.mult())
#program successfully executed
