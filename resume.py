#create a resume builder usiing multilevel inheritance in python
#requremnts are create a parent class of 10th details and initialize marks and name and constructor 
# and create a child class 12 th details and construct the requirements
#  are employee name  and grade  and inherit the parent class and assign 
# values to the child class clg details and display the details of employee using 
# method overriding
class tenth_details:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
class twelth_details(tenth_details):
    def __init__(self, name, marks, grade):
        super().__init__(name, marks)
        self.grade = grade
        def display_details(self):
            return f"Name: {self.name}, Marks: {self.marks}, Grade: {self.grade}"
class clg_details(twelth_details):
    def __init__(self, name, marks, grade, clg_name, location):
        super().__init__(name, marks, grade)
        self.clg_name = clg_name
        self.location = location
    def display_details(self):
        return f"Name: {self.name}, Marks: {self.marks}, Grade: {self.grade}, \
            College Name: {self.clg_name}, Location: {self.location}"
student1=clg_details("Priyanshu", 85, "A", "A.i.w.c a.o.e", "jamshedpur")
print(student1.display_details())
student2=clg_details("kashak", 92, "A+", "st joseph high school", "jamshedpur")
print(student2.display_details())
