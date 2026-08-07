Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Pyhon Operators
a=10
b=5
a+b
15
a-b
5
a*6
60
20/b
4.0
25//b
5
a**b
100000
a%2
0
a=6
b=10
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
#Assigment operators
a=10
b=4
a+=5
a
15
b-=2
b
2
a*=5
a
75
b/=2
b
1.0
a//=3
a
25
b*=6
b
6.0
b**=6
b
46656.0
a%=2
a
1
b *= 2
b
93312.0
c=8
c**=2
c
64
#Relational/Logical Operators
a=10
b=6
a>b and a<b
False
a<b or a>b
True
not a==b
True
#Membership Operators
str='Python Java'
'Python' in str
True
'c' in str
False
'Java' not in str
False
lst=[1,2,3]
3 in lst
True
4 not in lst
True
tup=(4,6,9)
6 in tup
True
4 not in tup
False
set={8,9,0}
8 in set
True
0 not in set
False
dict={'name':'priyanka', 'age':20, 'batch':'pfs'}
dict
{'name': 'priyanka', 'age': 20, 'batch': 'pfs'}
'name' in dict
True
20 in dict
False
'batch' not in dict
False
#Identity Operators
l=[1,2,3]
m=[1,2,3]
id(l)
3012780119296
id(m)
3012811226816
l is m
False
a=m
a is m
True
id(a)
3012811226816
id(m)
3012811226816
l is not m
True
a is not l
True
a is not m
False
#Bitwise Operator
11&12
8
11|15
15
12^8
4
2<<3
16
3<<2
12
~7
-8
