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


