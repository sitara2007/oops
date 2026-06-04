#create a parent class employee with attribute starting name, email and create two child class starting developer
#  and tester for developer the specific attribute will be language and for a tester the specifical attributee will
#  be a tool and display all details in parent class and inheritate
class employee:
    def __init__(self,name, email):#contructor to initialize the method
        self.name=name#class attributes
        self.email=email#class atributes
    def display_details(self):# display parent class
        return f"Name: {self.name}, Email: {self.email}"
class developer(employee):
    def __init__(self, name, email, language):
        super().__init__(name, email)
        self.language = language
    def display_details(self):
        return f"{super().display_details()}, Language: {self.language}"#

class tester(employee):
    def __init__(self, name, email, tool):
        super().__init__(name, email)
        self.tool = tool
    def display_details(self):
        return f"{super().display_details()}, Tool: {self.tool}"

dev = developer("Priyanshu", "priyanshu@gmail.com", "Python")
test = tester("Anjali", "pishu@gmail.com", "Selenium")

print(dev.display_details())
print(test.display_details())

