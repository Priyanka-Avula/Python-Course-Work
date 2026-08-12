Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#List
l=[]
l=list()
type(l)
<class 'list'>
l=[1,12.5,"str",False,[1,2,3],(4,5,6),{7,8,9},{1:1,2:3},3+9j]
l
[1, 12.5, 'str', False, [1, 2, 3], (4, 5, 6), {8, 9, 7}, {1: 1, 2: 3}, (3+9j)]
l=[2,3,3,2,4]
l
[2, 3, 3, 2, 4]
a=[1,2,3]
b=[4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*2
[1, 2, 3, 1, 2, 3]
a=[567,89,903,1234]
a[1]
89
a[3]
1234
a[-2]
903
a[::-1]
[1234, 903, 89, 567]
a[:3]
[567, 89, 903]
a[-1:-3:-1]
[1234, 903]
89 in a
True
12334 not in a
True
567 not in a
False
a=[890,78,234,12,67,5]
max(a)
890
min(a)
5
sorted(a)
[5, 12, 67, 78, 234, 890]
len(a)
6
a.append(76)
a
[890, 78, 234, 12, 67, 5, 76]
a.append(1921)
a
[890, 78, 234, 12, 67, 5, 76, 1921]
a.insert(2,123)
a
[890, 78, 123, 234, 12, 67, 5, 76, 1921]
a.extend(45,56)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.extend(45,56)
TypeError: list.extend() takes exactly one argument (2 given)
a.extend([45,56])
a
[890, 78, 123, 234, 12, 67, 5, 76, 1921, 45, 56]
a.pop()
56
a
[890, 78, 123, 234, 12, 67, 5, 76, 1921, 45]
a.pop(2)
123
a
[890, 78, 234, 12, 67, 5, 76, 1921, 45]
a.remove(67)
a
[890, 78, 234, 12, 5, 76, 1921, 45]
a.clear()
a
[]
a=[890,78,234,12,67,5]
a
[890, 78, 234, 12, 67, 5]
del a[2]
a=[890,78,234,12,67,5]
a.index(78)
1
a.count(5)
1
b=a.copy()
b
[890, 78, 234, 12, 67, 5]
a=[2,'',False,[],{}]
a
[2, '', False, [], {}]
a.any()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.any()
AttributeError: 'list' object has no attribute 'any'
any([2,'',False,[],{}])
True
all([2,'',False,[],{}])
False
any([0,'',False,[],{}])
False
any(a)
True
a.reverse()
a
[{}, [], False, '', 2]
a.sort()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'dict'
a=[890,78,234,12,67,5]
a.sort()
a
[5, 12, 67, 78, 234, 890]
a.sorted()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
