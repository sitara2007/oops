#single inheritance in python
#explaining the concept of inheritance and method overriding in python using the below code snippet
class father:#creating a class called father
    def __init__(self, name, age):#defining a constructor
        self.name = name#object member
        self.age = age#object member    
    def display_details(self):#method to display details
        return f"Name: {self.name}, Age: {self.age}"#displaying details
class son(father):#creating a class called son which inherits from father class 
    def display_details(self):#method to display details
        return f"Name: {self.name}, Age: {self.age}"#displaying details
son1 = son("John", 30)#creating an object of the son class
print(son1.display_details())#displaying details using the method of the father class
print(son1.display_details())#displaying details using the method of the son class
son2=son("Mike", 25)#creating another object of the son class
print(son2.display_details())#displaying details using the method of the father class
 