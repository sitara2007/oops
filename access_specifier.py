#public specifier-->
#it does not provide any security to the data members of the class
#in public accesss specifier we can easily access the data inside the class or outside the class and more precisely known
#as public member or variable

#protected specifier --> 
# used to give securiyt , does not provide and used that paticualr property inside the parent class or a child class

#private access specifier -->
# which gives security to the property for this we have to use __
#class bank_account:
 #   def __init__(self, balance, account_num ):#CONSTRUCTOR
  #      self.__balance = balance #private property

      #  self.__account_num=account_num
#obj=bank_account(400,123456)
#print(obj.balance)
#print(obj.account_num)
#program successfully executed
#3 ways -->
# 1.name mangling method-- it is a syntactical way to access private way data members ( synatax --- > obj._classnme__property name)
#
class bank_account:
    def __init__(self, balance, account_num ):#CONSTRUCTOR
        self.__balance = balance #private property
        self.__account_num=account_num
obj=bank_account(400,123456)
print(obj._bank_account__balance)
print(obj._bank_account__account_num)
#program successfully executed
#gettr and setter method to set values or property--> 
# syntax(def getter(self))
#return self.__property name
#setter
#syntax--
#def setter(self, new_val)
#self__property_name=new value
class bank_account:
    def __init__(self, balance, account_num ):
        self.bal=balance
        self.acc=account_num
    def getter(self):
        return self.bal
    def setter(self, new_val):
        self.bal=new_val
obj=bank_account(400,123456)
print(obj.getter())
obj.setter(500)
print(obj.getter())
#program successfully executed  
