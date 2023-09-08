from random import *
list1=[0]*10
list2=[]
for i in range(10):
    list1[i]=randint(1,10)
print(list1)
for i in range(-1,-11,-1):
    list2.append(list1[i])
print(list2)
