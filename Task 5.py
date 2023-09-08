from random import *
list=[0]*10
list_even=[]
list_odd=[]
for i in range(10):
    list[i]=randint(1,10)
print(list)
for i in range(10):
    if list[i]%2==0:
        print(list[i],end=' ')
        list_even.append(list[i])
print()
for i in range(10):
    if list[i]%2==1:
        print(list[i],end=' ')
        list_odd.append(list[i])
print()
if len(list_even)>len(list_odd):
    for i in range(len(list_odd)):
        list_even.append(list_odd[i]+1)
    for i in range(10):
        print(list_even[i],end=' ')
elif len(list_even)<len(list_odd):
    for i in range(len(list_even)):
        list_odd.append(list_even[i]+1)
    for i in range(10):
        print(list_odd[i],end=' ')
else:
    for i in range(10):
        print(list[i],end=' ')
