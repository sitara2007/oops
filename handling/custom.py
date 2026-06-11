
class Dobexception(Exception):#user define exception
    pass
year=int(input())
age=2026-year
try:
    if age<18 & age>14:
        print("yummmy")
    else:
        raise Dobexception
except Dobexception:
    print("^__^")