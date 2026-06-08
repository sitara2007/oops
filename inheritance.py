#create a parent class and intialize employee name and salary and
#  constructor and create a child class developer and construct the requirements are programming language and inherit the parent class and assign values to
#  the child class objects and display
#  the details of employee using method overriding
class Employee:#creating a parent class called employee #base class
    def __init__(self,emp_name, salary):#defining a constructor
        self.name=emp_name
        self.s=salary
class developer(Employee):#creating a child class called developer which inherits from employee class
    def __init__(self,emp_name, salary, lang):#defining a constructor
        super().__init__(emp_name , salary)#inheriting the parent class constructor
        self.lang=lang
    def display_details(self):#method to display details
        return f"Employee Name: {self.name}, Salary: {self.s}, Programming Language: {self.lang}"#displaying details
dev1=developer("John Doe", 50000, "Python")# type: ignore #creating an object of the developer class
print(dev1.display_details())#displaying details using the method of the developer class
#multilevel inheritance in python
#10th or 12th details as parent class and clg details as child class and employee details as grand child class
class tenth_details:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
class twelth_details(tenth_details):
    def __init__(self,name ,marks, grade):
        super().__init__(name, marks)#inheriting the parent class constructor
        self.grade = grade
        tenth_details.__init__(self, name, marks)
class clg_details(twelth_details):
    def __init__(self, name, marks, grade, clg_name, location):
        super().__init__(name, marks, grade)#inheriting the parent class constructor
        self.clg_name = clg_name
        self.location = location
    def display_details(self):
        return f"Name: {self.name}, Marks: {self.marks}, Grade: {self.grade}, \
            College Name: {self.clg_name}, Location: {self.location}"
student1=clg_details("Priyanshu", 85, "A", "A.i.w.c a.o.e", "jamshedpur")
print(student1.display_details())   
student2=clg_details("kashak", 92, "A+", "st joseph high school", "jamshedpur")
print(student2.display_details())

