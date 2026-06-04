#1. using abstract base class (abc) 
#2. using abstractmethod decorator like @abstractmethod use pass inside the function in abs method 
from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def area(self):
        pass #abstraction method, no implementation here