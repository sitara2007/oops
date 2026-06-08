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


