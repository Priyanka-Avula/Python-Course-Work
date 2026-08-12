Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Set
s=set()
type(s)
<class 'set'>
s={1,2,3,4,5,6,1234,1234689,65478}
s
{1, 2, 3, 4, 5, 6, 1234689, 65478, 1234}
s={1,2,1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s.add(1)
s.add(8.9)
s.add("str")
s.add([1,2])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add([1,2])
TypeError: unhashable type: 'list'
s.add((4,5))
s.add({1,5,6})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add({1,5,6})
TypeError: unhashable type: 'set'
s.add({1:2,4:6})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add({1:2,4:6})
TypeError: unhashable type: 'dict'
s.add(True)
s
{8.9, 1, 'str', (4, 5)}
#set Operations
a={1,2,3,4,5}
b={3,5,7,8,9}
2 in a
True
10 not in a
True
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
{3, 5}
b-a
{8, 9, 7}
a^b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
{1}<=a
True
a>={1,2,3}
True
a.isdisjoint(b)
False
#Set Merhods
a={1,7,40,43,21,23,89}
a
{1, 23, 21, 7, 40, 89, 43}
sorted(a)
[1, 7, 21, 23, 40, 43, 89]
min(a)
1
max(a)
89
len(a)
7
a={1,2,"str",0}
any(a)
True
all(a)
False
a={1,2,4,5}
sum(a)
12
a={1,2,3}
b=a
b.add(4)
a
{1, 2, 3, 4}
b
{1, 2, 3, 4}
c=a.copy()
c
{1, 2, 3, 4}
c.add(5)
c
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4}
{1, 2, 3, 4}
{1, 2, 3, 4}
a.add(100)
a
{1, 2, 3, 100, 4}
a.update(12,5,78)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.update(12,5,78)
TypeError: 'int' object is not iterable
a.update{(12,5,78)}
SyntaxError: invalid syntax
SyntaxError: invalid syntaxa
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a.update({12,5,78})
a
{1, 2, 3, 100, 4, 5, 12, 78}
a.pop()
1
a
{2, 3, 100, 4, 5, 12, 78}
a.remove(100)
a
{2, 3, 4, 5, 12, 78}
a.discard(100)
a
{2, 3, 4, 5, 12, 78}
a.clear()
a
set()
