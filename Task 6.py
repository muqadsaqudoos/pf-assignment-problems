from random import *
list=[0]*10
for i in range(10):
    flag=True
    while flag:
        a=randint(1,15)
        flag=False
        for j in range(i):
            if a==list[j]:
                flag=True
                break
    list[i]=a
print(list)
