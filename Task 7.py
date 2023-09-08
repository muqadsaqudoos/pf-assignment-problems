from random import *
list=[0]*10
sen=-1
for i in range(10):
   list[i]=randint(1,5)
   print(list[i],end=' ')
print()
for i in range(10):
    if sen!=list[i]:
        print(f'{list[i]} is at index {i}',end=' ')
        for j in range(i+1,10):
            if list[i]==list[j]:
                print(f'{j}',end=' ')
                list[j]=sen
        print()
              
