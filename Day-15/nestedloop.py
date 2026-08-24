#Patterns
for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(5):
        print(j%2,end=' ')
    print()

for i in range(5):
    for j in range(5):
        print(i%2,end=' ')
    print()

for i in range(5):
    for j in range(5):
        print((i+j)%2,end=' ')
    print()

for i in range(5):
    for j in range(5):
        print(i+j,end=' ')
    print()

c=1
for i in range(5):
    for j in range(5):
        print(c,end=' ')
        c+=1
    print()

for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()

for i in range(5):
    for j in range(5-i-1):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()

n=int(input("Enter the size:"))
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print()

n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for k in range(n-i):
            print('*',end=' ')
    print()

n=int(input("Enter the Size:"))
m=n//2
for i in range(n):
    if i<=m:
        print('* '*(i+1),end=' ')
    else:
        print('* '*(n-i),end=' ')
    print()

n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),'*'*(i+1),end=' ')
    else:
        print(' '*(i-m),'*'*(n-i),end=' ')
    print()

n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),'* '*(i+1),end=' ')
    else:
        print(' '*(i-m),'* '*(n-i),end=' ')
    print()