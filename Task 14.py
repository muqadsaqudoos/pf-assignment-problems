from random import *
rows=10
col=10
a=[[randint(0,9)for j in range(col)]for i in range(rows)]
for i in range(rows):
    for j in range(col):
        print(a[i][j],end=' ')
    print()
for i in range(rows):
    for j in range(col):
        if i==j:
            print(a[i][j],end=' ')
        else:
            print(end='  ')
    print()
print()
b=9
for i in range(10):
    for j in range(10):
        if j==b:
            print(a[i][j],end=' ')
            b-=1
        else:
            print(end='  ')
    print()
