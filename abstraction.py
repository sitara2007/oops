#1. using abstract base class (ABC) 
#2. using abstractmethod decorator like @abstractmethod use pass inside the function in abs method 
from abc import ABC, abstractmethod
class child(ABC):
    @abstractmethod
    def area(self, name,roll):
        pass #abstraction method, no implementation here
class child1(child):
    def area(self,name, roll):
        self.name=name
        self.roll-roll
        return f" name is {self.name} and roll is {self.roll}"
        #implementation of the abstract method
        
obj=child1()
print(obj.area("meena",1234))
#program successfully executed