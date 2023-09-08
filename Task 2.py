from random import *
len=int(input())
list=[0]*len
sum=0
for i in range(len):
    list[i]=randint(1,10)
print(list)
for i in range(len):
    sum=sum+list[i]
print(sum)
