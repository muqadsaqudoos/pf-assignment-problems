
#Bubble sort
from random import *
from time import *
list1=[0]*5
list2=[0]*5
list3=[]
seconds1=time()
for i in range(5):
    list1[i]=randint(1,10)
for i in range(4):
    for j in range(4):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
for i in range(5):
    list2[i]=randint(1,10)
for i in range(4):
    for j in range(4):
        if list2[j]>list2[j+1]:
            list2[j],list2[j+1]=list2[j+1],list2[j]
print(list2)
for i in range(5):
    list3.append(list1[i])
for i in range(5):
    list3.append(list2[i])
for i in range(9):
    for j in range(9):
        if list3[j]>list3[j+1]:
            list3[j],list3[j+1]=list3[j+1],list3[j]
seconds2=time()
print(list3)
print(seconds2-seconds1)


#selection sort
from random import *
from time import *
def find_min_index(x,start,end):
    for i in range(start,end):
        if i==start:
            min_index=start
        elif x[min_index]>x[i]:
            min_index=i
    return min_index
list1=[0]*5
list2=[0]*5
list3=[]
seconds1=time()
for i in range(5):
    list1[i]=randint(1,10)
for i in range(4):
    min_index=find_min_index(list1,i,5)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
for i in range(5):
    list2[i]=randint(1,10)
for i in range(4):
    min_index=find_min_index(list2,i,5)
    list2[i],list2[min_index]=list2[min_index],list2[i]
print(list2)
for i in range(5):
    list3.append(list1[i])
for i in range(5):
    list3.append(list2[i])
for i in range(9):
    min_index=find_min_index(list3,i,10)
    list3[i],list3[min_index]=list3[min_index],list3[i]
print(list3)
seconds2=time()
print(seconds2-seconds1)
