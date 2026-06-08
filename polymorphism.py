#polymorphism in python overloading / overriding
#s the OOPS concept that allows different classes to share the same method name but behave 
# completely differently based on the object calling them.
class rohit:
    def __init__(self, name):#constructor to initialize the name of the player
        self.name = name
    def display(self):#method to display the name of the player
        return f"Player is a batsman: {self.name}"  
class virat:
    def __init__(self, name):#constructor to initialize the name of the player
        self.name = name
    def display(self):#method to display the name of the player
        return f"Player is a bowler: {self.name}"
player1 = rohit("Rohit Sharma")#creating an object of the rohit class
player2 = virat("Virat Kohli")#creating an object of the virat class
print(player1.display())#displaying the name of the player using the method of the rohit class
print(player2.display())#displaying the name of the player using the method of the virat class
#polymorphism in python overriding
class animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        return f"{self.name} makes a sound"
class dog(animal):
    def sound(self):
        return f"{self.name} barks"
class cat(animal):
    def sound(self):
        return f"{self.name} meows"
animal1 = animal("Animal")#creating an object of the animal class
dog1 = dog("Dog")#creating an object of the dog class
cat1 = cat("Cat")#creating an object of the cat class
print(animal1.sound())#displaying the sound of the animal using the method of the  animal class
print(dog1.sound())#displaying the sound of the dog using the method of the dog class
print(cat1.sound())#displaying the sound of the cat using the method of the cat class
#differ in both the overloading and overriding is that in overloading we have multiple methods with the same name but different parameters 
#and in overriding we have a method in the child class with the same name as the method in the parent class and it overrides 
#the method of the parent class.
#overloading is a compile time polymorphism thereis no constructor in python but we can achieve overloading by using
#  default arguments and variable length arguments and overriding is a runtime polymorphism where the method of the 
# child class is called at runtime instead of the method of the parent class.
class calcarea:
    def area(self, x,y=None):#default argument y is set to None to achieve overloading
        if y is None:#memory optimization to check if the second parameter is None or not
            return f"Area of square: {x*x}"
        elif x is None:
            return f"Area of square: {y*y}"
        elif x is not None and y is not None:
            return f"Area of rectangle: {x*y}"
        elif x is None and y is None:
            return "Please provide the dimensions to calculate the area"
        else:
            return "Invalid input"
area1 = calcarea()#creating an object of the calcarea class
print("area is ",area1.area(4))#calculating the area of a square using the area method
print("area is ",area1.area(5, 10))#calculating the area of a rectangle using the area method
print("area is ",area1.area(None, -5))#calculating the area of a square using the area method
area2 = calcarea()#creating another object of the calcarea class
print("area is ",area2.area(7))#calculating the area of a square using the area method
print("area is ",area2.area(7, 14))#calculating the area of a rectangle using the area method
print("Program successfully executed")
class sumation:
    def summ(self, *args):#variable length arguments to achieve overloading , #kwrgs can also be used to achieve overloading
    #def sum(self, **kwargs):
        return f"Sum of the numbers: {sum(args)}"
    def max(self, *args):
        return f"maximum of the numbers: {max(args)}"
    def min(self, *args):
        return f"minimum of the numbers: {min(args)}"
    def average(self, *args):
        return f"average of the numbers: {sum(args)/len(args)}"


object= sumation()#creating an object of the sumation class
print("sum is ",object.summ(1, 2, 3))#calculating the sum of numbers using the summ method
print("max is ",object.max(4, 5, 6, 7))#calculating the maximum of numbers using the max method
print("min is ",object.min(8, 9, 10))#calculating the minimum of numbers using the min method
print("average is ",object.average(11, 12, 13, 14))#calculating the average of numbers using the average method
print("Program successfully executed")
#method overriding in python
class demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display1(self):
        return f"Name: {self.name}"
    def display2(self):
        return f"Age: {self.age} name: {self.name}"
    #overriding the display1 method to display the age instead of the name
    def display1(self):
        return f"Age: {self.age}"
demo1 = demo("John", 30)#creating an object of the demo class
print(demo1.display1())#displaying the age of the person using the display1 recently overridden method# Age: 30
print(demo1.display2())#displaying the age and name of the person using the display2 method#Age: 30 name: John
print("Program successfully executed")

    
    

