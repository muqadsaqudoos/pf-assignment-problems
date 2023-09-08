from random import *
rows=10
col=10
a=[[randint(0,9)for j in range(col)]for i in range(col)]
for i in range(rows):
    for j in range(col):
        print(a[i][j],end=' ')
    print()

print()
for i in range(rows):
    for j in range(col):
        if a[i][j]==0:
            print(f'{i} {j}',end=' ')
            print()
