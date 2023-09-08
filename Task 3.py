from random import *
len=int(input())
list1=[0]*len
for i in range(len):
    list1[i]=randint(1,10)
print(list1)
list2=[list1[i] for i in range(len)]
print(list2)
