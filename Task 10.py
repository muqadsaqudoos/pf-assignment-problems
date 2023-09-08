from random import *
list=[0]*10
for i in range(10):
    list[i]=randint(3,7)
print(list)
for i in range(10):
    j=0
    while j<list[i]:
        print('*',end=' ')
        j+=1
    print()
