#monkey patching in python
class monkey:
    def display(self):
        print("employeee works")
    def display(self):
        return ("not works")
    def display(self):
        return f"EMPLOYEE WORKS"
    #outside the class creating new method and overriding to display first value or details
monkey1=monkey()
print(monkey1.display())
#program successfully executed
#the address of new function otside the class will be overwitten will override the old class method address
class bank_account:
    def __init__(self, balance, account_num ):#CONSTRUCTOR
        self.__balance = balance #private property
        self.acc_num=account_num
    @property
    def getter(self):
        return self.__balance
    def setter(self, new_val):
        self.__balance=new_val
obj=bank_account(400,123456)
print(obj.getter)
obj.setter(500)
print(obj.getter)
#program successfully executed

