#method change--> the phenomena of calling two parent class method to inside child class method ,
#  with the super fuction only u can and inheritate the paticular parent method
class parent1:
    def __init__(self):
        pass
    def method1(self):
        return "Parent 1 method"

class parent2:
    def __init__(self):
        pass
    def method2(self):
        return "Parent 2 method"
class child(parent1, parent2):
    def __init__(self):
        super().__init__()
        parent1.__init__(self)
        parent2.__init__(self)
    def method3(self):
        return "Child method"
obj=child()
print(obj.method1())
print(obj.method2())
print(obj.method3())

