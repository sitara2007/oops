#using enumereate 
my_list=[3,5,7,9]
dis=map(lambda x:x,enumerate(my_list))
print(list(dis))

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
show=dict(map(lambda x,y:(x,y),(l1),(l2)))
print(show)
dict={"ram":2,"sita":3,"meera":4}
li=dict.keys()
lis=dict.values()
display=list(map(lambda x,y:(x,y),dict.keys(),dict.values()))
print(display)
#filter --> in built function
lis=[21,9,13,80]
print(list(filter(lambda x:x>18,lis)))