Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Input Formatting
a=input()
name
a
'name'
a=input("Enter a Value:")
Enter a Value:123
a
'123'
marks=int(input("Enter the marks:"))
Enter the marks:89
marks
89
price=float(input("Enter the price:"))
Enter the price:90.8
price
90.8
names=input("Enter the names:")
Enter the names:Priyanka Kalyani Iswarya
names
'Priyanka Kalyani Iswarya'
list(names)
['P', 'r', 'i', 'y', 'a', 'n', 'k', 'a', ' ', 'K', 'a', 'l', 'y', 'a', 'n', 'i', ' ', 'I', 's', 'w', 'a', 'r', 'y', 'a']
names.split()
['Priyanka', 'Kalyani', 'Iswarya']
names.split(',')
['Priyanka Kalyani Iswarya']
courses="pfs-java-flask"
course.split(-)
SyntaxError: invalid syntax
courses.split(-)
SyntaxError: invalid syntax
courses.split('-')
['pfs', 'java', 'flask']
names=tuple(input("Enter the names:")).split()
Enter the names:Priyanka Kalyani Iswarya
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names=tuple(input("Enter the names:")).split()
AttributeError: 'tuple' object has no attribute 'split'
names=tuple(input("Enter the names:").split())
Enter the names:Priyanka Kalyani Iswarya
names
('Priyanka', 'Kalyani', 'Iswarya')
courses=set(input("Enter the courses:").split('-'))
Enter the courses:pfs-java-flask
courses
{'pfs', 'flask', 'java'}
names=input("enter the names:")
enter the names:Monika Sai Priyanka
names
'Monika Sai Priyanka'
names.split(',')
['Monika Sai Priyanka']
names=input("enter the names:")
enter the names:Monika, Sai, Priyanka
names
'Monika, Sai, Priyanka'
names.split(',')
['Monika', ' Sai', ' Priyanka']
marks="enter the marks"
marks=input("enter the marks")
enter the marks2 45 78 09
marks
'2 45 78 09'
marks.split()
['2', '45', '78', '09']
map(int,marks)
<map object at 0x0000016F3416B370>
list(map(int,marks))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(map(int,marks))
ValueError: invalid literal for int() with base 10: ' '
marks=list(map(int,marks))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    marks=list(map(int,marks))
ValueError: invalid literal for int() with base 10: ' '
marks=list(map(int,marks.split()))
marks
[2, 45, 78, 9]
marks=tuple(map(int,marks.split()))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    marks=tuple(map(int,marks.split()))
AttributeError: 'list' object has no attribute 'split'
marks=tuple(map(int,marks.split()))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    marks=tuple(map(int,marks.split()))
AttributeError: 'list' object has no attribute 'split'
marks=tuple(map(int,input("Enter the marks").split()))
Enter the marks34 56 78
marks
(34, 56, 78)
marks=set(map(int,input("Enter marks").split()))
Enter marks89 76 54
marks
{89, 76, 54}
marks=tuple(map(int,marks.))
SyntaxError: invalid syntax
marks=tuple(map(int,marks))
marks
(89, 76, 54)
price=input("enter the price")
enter the price78.9 87.0 76.5
price
'78.9 87.0 76.5'
price.split(',')
['78.9 87.0 76.5']
map(float,price)
<map object at 0x0000016F3416AA40>
price=list(map(float,price).split()))
SyntaxError: unmatched ')'
price=list(map(float,price).split())))
SyntaxError: unmatched ')'
price=list(map(float,price.split()))
price
[78.9, 87.0, 76.5]
price=tuple(map(float,input("enter price").split()))
enter price67.9 78.0 8.9
price
(67.9, 78.0, 8.9)
price=set(map(float,input("enter price").split()))
enter price8.9 78.9 67.6
price
{8.9, 67.6, 78.9}
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"name")
c
'name'
email,password=input("Enter the email, password:").split()
Enter the email, password:monika@gmail.com 8765
email,password
('monika@gmail.com', '8765')
int(password)
8765
a,b,c=list(map(int,input().split()))
4 5 8
a
4
c
8
a,b,c=tuple(map(int,input().split()))
12 34 56
c
56
a,b,c=set(map(int,input().split()))
2 5 47
b
5
status=eval(input())
True
status
True
type(status)
<class 'bool'>
status=eval(input())
status=eval(input())
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    status=eval(input())
          ^
SyntaxError: invalid syntax
status=eval(input())
2+5j
status
(2+5j)
type(status)
<class 'complex'>
status=eval(input())
[1,2,3]
status
[1, 2, 3]
status=eval(input())
(1,2,3)
type(status)
<class 'tuple'>
