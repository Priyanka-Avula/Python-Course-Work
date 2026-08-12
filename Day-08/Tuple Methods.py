Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=()
t=tuple()
t-(1,2,3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t-(1,2,3)
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
t=(1,2,3)
t=(1,1,1,)
t
(1, 1, 1)
t=(1,2.3,"str",[2,5,9],{9,0,8},{1:1,9:0},True)
t
(1, 2.3, 'str', [2, 5, 9], {0, 9, 8}, {1: 1, 9: 0}, True)
type(t)
<class 'tuple'>
#Tuple Operations
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 2.3, 'str', [2, 5, 9], {0, 9, 8}, {1: 1, 9: 0}, True)
t[1]
2.3
t[-1]
True
t[3:7]
([2, 5, 9], {0, 9, 8}, {1: 1, 9: 0}, True)
t[::-1]
(True, {1: 1, 9: 0}, {0, 9, 8}, [2, 5, 9], 'str', 2.3, 1)
t[-1:-3:-1]
(True, {1: 1, 9: 0})
True in t
True
"str" not in t
False
#Tuple Methods
t=(12,34,56,12,789,1256)
t
(12, 34, 56, 12, 789, 1256)
sorted(t)
[12, 12, 34, 56, 789, 1256]
min(t)
12
max(t)
1256
1256
1256
len(t)
6
t
(12, 34, 56, 12, 789, 1256)
t.index(56)
2
t.count(12)
2
t=(1,2,4,87,65)
sum(t)
159
t=(1,2,0,0,0)
any(t)
True
all(t)
False
