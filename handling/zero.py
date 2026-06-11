try:
    a=int (input())
    b=0
    c=a/b
except ZeroDivisionError:
    print("not divisible")

else:
    print(c)
finally:
    print("finally")