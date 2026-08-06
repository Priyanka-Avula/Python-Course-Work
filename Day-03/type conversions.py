Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
bool(a)
True
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
b=12.5
int(b)
12
str(b)
'12.5'
bool(b)
True
list(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
c='abc'
int(c)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'abc'
float(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    float(c)
ValueError: could not convert string to float: 'abc'
bool(c)
True
list(c)
['a', 'b', 'c']
tuple(c)
('a', 'b', 'c')
set(c)
{'a', 'b', 'c'}
dict(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
d=[1,2,4]
int(d)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
complex(d)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'list'
tuple(d)
(1, 2, 4)
set(d)
{1, 2, 4}
dict(d)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(d)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
e=(1,2,3,4)
float(e)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(e)
'(1, 2, 3, 4)'
list(e)
[1, 2, 3, 4]
set(e)
{1, 2, 3, 4}
dict(e)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(e)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
f={1,3,'a'}
float(f)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float(f)
TypeError: float() argument must be a string or a real number, not 'set'
int(f)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(f)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
str(f)
"{1, 'a', 3}"
list(f)
[1, 'a', 3]
dict(f)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(f)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
tuple(f)
(1, 'a', 3)
x={'name':'abc','age':20}
str(x)
"{'name': 'abc', 'age': 20}"
list(x)
['name', 'age']
bool(x)
True
y=True
complex(y)
(1+0j)
float(y)
1.0
