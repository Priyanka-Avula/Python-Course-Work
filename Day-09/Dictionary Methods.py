Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Dictionary
d={}
type(d)
<class 'dict'>
d={1:4,2:8}
d
{1: 4, 2: 8}
d={}
d[1]=1
d[12.3]=1
d["str"]=1
d[(1,2,4)]=1
d[(2+3j)]=1
d[True]=1
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: unhashable type: 'list'
d[{1,2,4})=1
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
d[{1,2,4}]=1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[{1,2,4}]=1
TypeError: unhashable type: 'set'
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
d[1]=1
d[2]=12.3
d[3]="str"
d[4]=2+9j
d[5]=True
d[6]=[1,2,3]
d[7]=(1,2,3)
d[8]={1,2,3}
d[9]=frozenset({1,2,3})
d[10]={1:2,2:4}
d[11]=None
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.3, 3: 'str', 4: (2+9j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 2, 2: 4}, 11: None}
d={}
d[1]=2
d
{1: 2}
d[1]=3
d
{1: 3}
data={"name":"priyanka", "course":"pfs", "batch":65}
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65}
name in data
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    name in data
NameError: name 'name' is not defined
"course" in data
True
"batch" not in data
False
data["age"]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    data["age"]
KeyError: 'age'
data.get("age","key not found")
'key not found'
data.get("name")
'priyanka'
data.get("course")
'pfs'
data.get("name","key not found")
'priyanka'
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65}
data["age"]=21
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 21}
data["phnno"]=987654321
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 987654321}
data.update({"email":"monika@gmail.com","py":2026})
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 987654321, 'email': 'monika@gmail.com', 'py': 2026}
data["py"]
2026
data["py"]=2027
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 987654321, 'email': 'monika@gmail.com', 'py': 2027}
data["age"]=22
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com', 'py': 2027}
data.popitem()
('py', 2027)
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com'}
data.pop("course")
'pfs'
data
{'name': 'priyanka', 'batch': 65, 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com'}
del data["batch"]
data
{'name': 'priyanka', 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com'}
data.clear()
data
{}
len(data)
0
00
0
data={'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com', 'py': 2027}
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com', 'py': 2027}
len(data)
7
data.keys()
dict_keys(['name', 'course', 'batch', 'age', 'phnno', 'email', 'py'])
data.values()
dict_values(['priyanka', 'pfs', 65, 22, 987654321, 'monika@gmail.com', 2027])
data.items()
dict_items([('name', 'priyanka'), ('course', 'pfs'), ('batch', 65), ('age', 22), ('phnno', 987654321), ('email', 'monika@gmail.com'), ('py', 2027)])
max(data)
'py'
min(data)
'age'
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phnno', 'py']
d={1:1,2:2}
m=d
m[3]=3
m
{1: 1, 2: 2, 3: 3}
d
{1: 1, 2: 2, 3: 3}
n=d.copy()
n[5]=5
n
{1: 1, 2: 2, 3: 3, 5: 5}
d
{1: 1, 2: 2, 3: 3}
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com', 'py': 2027}
data.get("py")
2027
data.setdefault("py",2027)
2027
data
{'name': 'priyanka', 'course': 'pfs', 'batch': 65, 'age': 22, 'phnno': 987654321, 'email': 'monika@gmail.com', 'py': 2027}
data.setdefault("name",2026)
'priyanka'
dict.fromkeys(["python","mysql","java"],0)
{'python': 0, 'mysql': 0, 'java': 0}
