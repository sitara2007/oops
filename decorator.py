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

#example-->
#create a class nme bank account inside that acc num and balance will be the property and define getter and setter method to access those paticular values and set a new value

class bank_account:
    def __init__(self,balance, acc_num):
        self.__balance = balance
        self.__acc_num=acc_num
    @property
    def getter(self):
        return self.__balance,self.__acc_num
    @getter.setter
    def setter(self,value1,value2):
        self.__balance = value1
        self.__acc_num=value2
obj=bank_account(1000,123456)
print(obj.getter)
obj.setter(200,400)
print(obj.setter)
print(obj.getter)
print("program successfully executed")
#program successfully executed
