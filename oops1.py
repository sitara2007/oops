#creating a class name student , create a clas members clg_name , course , 
# student name and age are requirements of class and 
# object members are student name and age
class Student:
    #class members
    clg_name = "ABC College"
    course = "Python"
    #object members
    student_name = "reena"
    age = 25    
#creating an object of the class student
student1 = Student()
print(student1.student_name)#accessing object members using object name
print(student1.course)#accessing class members using object name
print(student1.age) #accessing object members using object name
#creating a class called employee with class members company name and salary 
# and object members employee name and age and id and  accessing the 
# members using object name , use diff employee name and age and id for the 
# object members of employee class
class Employee:
    #class members
    company_name = input("Enter the company name: ")
    salary = input("Enter the salary: ")
    #object members
    employee_name = input("Enter the employee name: ")
    age = int(input("Enter the age: "))
    id = int(input("Enter the ID: "))
employee1 = Employee()
print(employee1.employee_name)
print(employee1.age)
print(employee1.id)
print(employee1.company_name)
print(employee1.salary)
employee2 = Employee()
employee2.employee_name = "Jane Smith"
employee2.age = 25
employee2.id = 54321
print(employee2.employee_name)   
print(employee2.age)
print(employee2.id)
print(employee2.company_name)
print(employee2.salary)
#methosds in class
class employee:
    #class members
    company_name = "CivicOs"
    salary = 30000
    #object members
    employee_name = "John Doe"
    age = 30
    id = 12345
    def details(self,company_name,salary,employee_name,age,id ):
        self.comp_name = company_name
        self.s = salary 
        self.emp_name = employee_name
        self.age = age
        self.id = id
employee1 = employee()
employee1.details('Toyota',30000,"John Doe",30,12345)
print(employee1.comp_name)   
print(employee1.s)
print(employee1.emp_name)
print(employee1.age)    
print(employee1.id)
# initialize method in class
class Employee:
    def __init__(self, company_name, salary, employee_name, age, id):
        self.company_name = company_name
        self.salary = salary
        self.employee_name = employee_name
        self.age = age
        self.id = id
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
print(employee1.company_name)           
print(employee1.salary)
print(employee1.employee_name)
print(employee1.age)
print(employee1.id)

#types of parameters in class using init method
#first is default constructor
class Employee:
    def __init__(self):
        self.company_name = "CivicOs"#class members
        self.salary = 30000
        self.employee_name = "John Doe"
        self.age = 30#object members
        self.id = 12345
        
employee1 = Employee()
print(employee1.company_name)   
print(employee1.salary)
print(employee1.employee_name)
print(employee1.age)
print(employee1.id)
#second is parameterized constructor
class Employee:
    def __init__(self, company_name, salary, employee_name, age, id):
        self.comp_name = company_name
        self.s= salary
        self.name= employee_name
        self.age = age
        self.id = id
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 1234)
employee2= Employee("Toyota", 40000, "Jane Smith", 25, 54321)
print(employee1.comp_name)
print(employee1.s)
print(employee1.name)
print(employee1.age)
print(employee1.id)
print(employee2.comp_name)
print(employee2.s)
print(employee2.name)
print(employee2.age)
print(employee2.id)
#assign and access class members using class name using init method using return statement
class Employee:
    def __init__(self, company_name, salary, employee_name, age, id):#parameterized constructor
        self.comp_name = company_name #class members
        self.s= salary
        self.name= employee_name #object members
        self.age = age
        self.id = id
    def get_details(self): # method to return the details of the employee
        return f"Company Name: {self.comp_name}, Salary: {self.s}, Employee Name: {self.name}, Age: {self.age}, ID: {self.id}"
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
print(employee1.get_details())
#modify the class members and object members using object name
class Employee:
    def __init__(self, company_name, salary, employee_name, age, id):
        self.comp_name = company_name
        self.s= salary
        self.name= employee_name
        self.age = age
        self.id = id
    def get_details(self):
        return f"Company Name: {self.comp_name}, Salary: {self.s}, Employee Name: {self.name}, Age: {self.age}, ID: {self.id}"
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
employee1.comp_name = "Toyota" #modifying class member using object name
employee1.s = 40000 #modifying class member using object name
employee1.name = "Jane Smith" #modifying object member using object name
employee1.age = 25 #modifying object member using object name
employee1.id = 54321 #modifying object member using object name
print(employee1.get_details())
#modify the class members and object members using class name
class Employee:
    def __init__(self, company_name, salary, employee_name, age, id):
        self.comp_name = company_name
        self.s= salary
        self.name= employee_name
        self.age = age
        self.id = id
    def get_details(self):
        return f"Company Name: {self.comp_name}, Salary: {self.s}, Employee Name: {self.name}, Age: {self.age}, ID: {self.id}"
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
Employee.comp_name = "Toyota" #modifying class member using class name
Employee.s = 40000 #modifying class member using class name
employee1.name = "Jane Smith" #modifying object member using object name
employee1.age = 25 #modifying object member using object name
employee1.id = 54321 #modifying object member using object name
print(employee1.get_details())
#delete the class members and object members
class Employee:
        def __init__(self, company_name, salary, employee_name, age, id):
            self.comp_name = company_name
            self.s= salary
            self.name= employee_name
            self.age = age
            self.id = id
        def get_details(self):
            return f"Company Name: {self.comp_name}, Salary: {self.s}, Employee Name: {self.name}, Age: {self.age}, ID: {self.id}"
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
del employee1.comp_name #deleting class member using object name
del employee1.s #deleting class member using object name
del employee1.name #deleting object member using object name
del employee1.age #deleting object member using object name
del employee1.id #deleting object member using object name
print(employee1.get_details())
#delete the class members and object members
class Employee:
        def __init__(self, company_name, salary, employee_name, age, id):
            self.comp_name = company_name
            self.s= salary
            self.name= employee_name
            self.age = age
            self.id = id
        def get_details(self):
            return f"Company Name: {self.comp_name}, Salary: {self.s}, Employee Name: {self.name}, Age: {self.age}, ID: {self.id}"
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
del Employee.comp_name #deleting class member using class name
del Employee.s #deleting class member using class name
del employee1.name #deleting object member using object name
del employee1.age #deleting object member using object name
del employee1.id #deleting object member using object name
print(employee1.get_details())
#delete the class
class Employee:
        def __init__(self, company_name, salary, employee_name, age, id):
            self.comp_name = company_name
            self.s= salary
            self.name= employee_name
            self.age = age
            self.id = id
        def get_details(self):
            return f"Company Name: {self.comp_name}, Salary: {self.s}, Employee Name: {self.name}, Age: {self.age}, ID: {self.id}"
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
del Employee #deleting the class
print(employee1.get_details())
#decorators in class
class Employee:
    def __init__(self, company_name, salary, employee_name, age, id):
        self.comp_name = company_name
        self.s= salary
        self.name= employee_name
        self.age = age
        self.id = id
    @property #decorator to get the details of the employee
    def get_details(self):
        return f"Company Name: {self.comp_name}, Salary: {self.s}, Employee Name: {self.name}, Age: {self.age}, ID: {self.id}"
employee1 = Employee("CivicOs", 30000, "John Doe", 30, 12345)
print(employee1.get_details)
#static method in class
class Employee:
    def __init__(self, company_name, salary, employee_name, age, id):
        self.comp_name = company_name
        self.s= salary
        self.name= employee_name
        self.age = age
        self.id = id
    @staticmethod #decorator to define a static method
    def get_company_name():
        return "CivicOs"
print(Employee.get_company_name())

