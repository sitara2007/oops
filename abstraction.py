#1. using abstract base class (ABC) 
#2. using abstractmethod decorator like @abstractmethod use pass inside the function in abs method 
from abc import ABC, abstractmethod

class Child(ABC):
    @abstractmethod
    def area(self, name, roll):
        pass  # Enforces that all children MUST implement 'area' with these parameters

class Child1(Child):
    def area(self, name, roll):
        self.name = name
        self.roll = roll  # Correctly saves the data to the object instance
        return f"name is {self.name} and roll is {self.roll}"

# Execution
obj = Child1()
print(obj.area("meena", 1234))

#program successfully executed
from abc import ABC, abstractmethod

class Child(ABC):
    @abstractmethod
    def area(self, name, roll):
        pass

class Child1(Child):
    def area(self, name, roll):
        self.name = name
        self.roll = roll  # Fixed from self.roll-roll
        return f"name is {self.name} and roll is {self.roll}"

# Execution
obj = Child1()
print(obj.area("meena", 1234))

#program successfully executed
 # example -- create a clas called payment and inheritate upi and car payment both are child classes using concrete method and abc 

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class Upi(Payment):
    def pay(self):
        return "upi payment"
class Card(Payment):
    def pay(self):
        return "card payment"
obj = Upi()
print(obj.pay())
obj1 = Card()
print(obj1.pay())

#program successfully executed
#even or odd
from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def even_odd(self):
        pass
class child1(parent):
    def even_odd(self, num):
        self.num=num
        if num%2==0:
            return "even"
        else:
            return "odd"
obj=child1()
print(obj.even_odd(4))
#program successfully executed)

# or using lambda --> it is a keyword which creates anonymous function a simple task mostly true false type of simple task
#syntax-->
#palindrome
#check_pal=lambda n:n==n[::-1]
#print(check_pal("madam"))
from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def even_odd(self):
        pass
class child1(parent):
    def even_odd(self, num):
        self.num=num
        num=str(num)
        check_palindrome=lambda n:n==n[::-1]
        return check_palindrome(num)
obj=child1()
print(obj.even_odd(4))



