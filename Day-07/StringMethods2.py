Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Whitespace and Trimming Methods
s='     Monika Sai    Priyanka     '
s.strip()
'Monika Sai    Priyanka'
s.lstrip()
'Monika Sai    Priyanka     '
s.rstrip()
'     Monika Sai    Priyanka'
s.replace(' ','')
'MonikaSaiPriyanka'
#Splitting and Joining Methods
s='monika-sai-priyanka'
s.split('-')
['monika', 'sai', 'priyanka']
s.split('-',,2)
SyntaxError: invalid syntax
s.split('-',2)
['monika', 'sai', 'priyanka']
s.rsplit('-',2)
['monika', 'sai', 'priyanka']
l='''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
s=["python", "java", "mysql", "flask"]
s
['python', 'java', 'mysql', 'flask']
''.join(s)
'pythonjavamysqlflask'
' '.join(s)
'python java mysql flask'
', '.join(s)
'python, java, mysql, flask'
a='strings.py.java.sql'
a
'strings.py.java.sql'
a.partition('.')
('strings', '.', 'py.java.sql')
a.rpartition('.')
('strings.py.java', '.', 'sql')
#String Testing Methods
a='python.java'
a.startswith('python')
True
a.startswith('c')
False
a.endswith('python')
False
'acvgdh123'.isalpha()
False
'avbgg678'.isalnum()
True
'avbgg6@78'.isalnum()
False
'    '.isspace()
True
''.isspace()
False
'   avg'.isspace()
False
'Hlo World'.istitle()
True
'HLO World'.istitle()
False
'PYTHON'.isupper()
True
'pyTHon'.islower()
False
'my_var'.isidentifier()
True
'my_va@r'.isidentifier()
False
