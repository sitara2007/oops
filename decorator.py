#property decorator
# third method for private specifier to display property
class bank_account:
    def __init__(self,balance):
        self.__balance = balance#private property
    def getter(self):# anything but in case of property decorator
        return self.__balance
    def setter(self,value):
        self.__balance = value
obj=bank_account(1000)
print(obj.getter())
obj.setter(2000)
print(obj.getter())
#rules for decorator -->
#1. @property
#2. def same_property(self) and then return self
#3. same_propertyname.setter
#4. def sameproperty_name(self, new_value) and 
#5. then self.__property name=newvalue
class bank_account:
    def __init__(self,balance):
        self.__balance = balance
    @property
    def getter(self):
        return self.__balance
    @getter.setter
    def setter(self,value):
        self.__balance = value
obj=bank_account(1000)
print(obj.getter)
obj.setter=2000
print(obj.setter)
