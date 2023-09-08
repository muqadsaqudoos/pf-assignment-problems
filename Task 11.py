from random import *
list=[0]*10
for i in range(10):
    list[i]=randint(3,7)
print(list)
for i in range(1,11):
    for j in range(i):
        print(list[j],end=' ')
    print()
