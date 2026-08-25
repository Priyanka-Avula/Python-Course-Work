#NamePatterns
#Letter D
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter B
n = int(input("Enter the size:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter E
n = int(input("Enter the size:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter F
n = int(input("Enter the size:"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter C
n = int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter G
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter H
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter I
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter J
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or (i==n-1 and j<=m) or j==m or (j==0 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter Z
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter X
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter Y
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter K
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i==j and i>=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter M
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Letter W
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=m) or (i+j==n-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter V
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or i-j==m or i+j==n+m-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter A
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i>=m) or (j==n-1 and i>=m) or i+j==m or (j-i==m and j>=m) or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter Q
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or (i==j and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter S
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==m or (j==n-1 and i>=m) or (j==0 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter B
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter C
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter L
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter N
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter O
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter P
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==m or (j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter R
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==m or (j==n-1 and i<=m) or (i==j and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter T
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Letter U
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


