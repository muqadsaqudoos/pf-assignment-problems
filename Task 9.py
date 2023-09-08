from random import *
list=[0]*20
list1=[]
for i in range(20):
    list[i]=randint(0,9)
print(list)
for i in range(0,2):
    list1.append(list[i])
for i in range(2,18):
        a=list[i-2]+list[i-1]+list[i+1]+list[i+2]
        b=a//4
        list1.append(b)
for i in range(18,20):
    list1.append(list[i])
print(list1)
