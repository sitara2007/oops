#employee salary system by static method and class
#  method and static method and
#  using decorators
class Employee:
    company_name ="CivicOS"#class member
    def __init__(self, name, salary):#defining a constructor
        self.name = name#object member
        self.salary = salary#object member
    @classmethod#class method to change company name
    def change_company_name(cls, new_company_name):#method to change company name
        cls.company_name = new_company_name
    @staticmethod#static method to display employee details
    def display_employee_details(employee):#method to display employee details
        return f"Employee Name: {employee.name}, Salary: {employee.salary}, Company Name: {Employee.company_name}"#displaying employee details
emp1=Employee("priyanshu",50000)#creating an object of the employee class
print(emp1.display_employee_details(emp1))#displaying employee details using the static method
Employee.change_company_name("TechCorp")#changing the company name using class method
print(emp1.display_employee_details(emp1))#displaying employee details using the static method after changing company name
#program successfully executed