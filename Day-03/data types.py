Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#data types
#int float complex
a=12
type(a)
<class 'int'>
b=13.4
type(b)
<class 'float'>
c=12+4j
type(c)
<class 'complex'>
#sequence data types
#string list tuple
s='Codegnan'
id(s)
2788345870448
s='Python'
id(s)
2788309420016
s += 'Python'
id(s)
2788315672688
s='aaaa'
type(s)
<class 'str'>
list=[1,2,3]
type(list)
<class 'list'>
id(list)
2788315672512
list.append(6)
id(list)
2788315672512
list
[1, 2, 3, 6]
list=[1, 12.6, 'string', [1,5]]
list
[1, 12.6, 'string', [1, 5]]
t=(1,2,3)
type(t)
<class 'tuple'>
t=(1,1,2)
t
(1, 1, 2)
tuple=(1, 12.9, 'abc')
tuple
(1, 12.9, 'abc')
s={80,70,24,78,78}
s
{80, 24, 70, 78}
s.add(5)
s
{5, 70, 78, 80, 24}
s={1, 12.3, 'xyz'}
s
{1, 12.3, 'xyz'}
type(S)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
type(s)
<class 'set'>
dict={'name':'abc','age':20,'grade':5}
dict
{'name': 'abc', 'age': 20, 'grade': 5}
s={1,2,3}
s
{1, 2, 3}
s=frozenset({1,2,1,4,5})
s
frozenset({1, 2, 4, 5})
a=True
type(a)
<class 'bool'>
s=None
s
type(s)
<class 'NoneType'>
