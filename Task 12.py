from random import *
list=[0]*10
for i in range(10):
    list[i]=randint(3,7)
print(list)
for i in range(1,11):
    sum=0
    for j in range(i):
        print(list[j],end=' ')
        sum=sum+list[j]
    print(f'={sum}')
