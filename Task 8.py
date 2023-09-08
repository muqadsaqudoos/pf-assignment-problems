from random import *
list=[0]*20
list[0]=randint(1,45)
list1=[]
for i in range(1,20):
    flag=True
    while flag:
        a=randint(1,45)
        flag=False
        for j in range(i):
            if a==list[j]:
                flag=True
                break
    list[i]=a
    for j in range(i):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
for i in range(19):
    a=list[i]
    b=list[i+1]
    c=a
    while a<b:
        if c<a:
            list1.append(a)
        a+=1
    
print(list1)
