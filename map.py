#map --> in-built function
#syntax-- map(fun_name, iteration collection)
l=["meera","ram","sita"]
print(list(map(lambda x:x.upper(),l)))
string="my name is priyanshu"
print(list(map(lambda x:x.upper(),string)))
string="my name is priyanshu"
print(list(map(lambda x:x.split(),string)))
list=[5,6,7,8]
show=dict(map(lambda x:(x,x**2),list))
print(show)
l=[3,5,7,9]
print(show)
list=[3,5,7,9]
#output {0:3,1:5,2:7,3:9}
sh=dict(map(lambda x:(x[0],x[1]),enumerate(list)))# enumerate function-- gives nested collection
print(sh)
print(ord("a"))
print(chr(97))
print(ord("A"))
print(chr(65))
# if-elseW#lambda arguments: expression_if_true if condition else expression_if_false

#find factorial of function using lambda function
f=1
for i in range(1,7):
    f=f*i
print(f)
fact=lambda n:1 if n==0 else n*fact(n-1)
print(fact(6))
#filter fuhnction examples
#print prime numbers from 1 to 30


prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print(list(filter(prime, range(1, 31))))



