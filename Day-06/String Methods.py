Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Concatenation
s='codegnan'
s
'codegnan'
type(s)
<class 'str'>
s=''
s
''
s='codegnan'
s
'codegnan'
a='python'
b='programming'
a+b
'pythonprogramming'
fname='monika'
lname='avula'
fname+lname
'monikaavula'
#repetition
b*12
'programmingprogrammingprogrammingprogrammingprogrammingprogrammingprogrammingprogrammingprogrammingprogrammingprogrammingprogramming'
'#'*6
'######'
'-sai-'*10
'-sai--sai--sai--sai--sai--sai--sai--sai--sai--sai-'
#Indexing
names='monika sai priyanka avula'
names
'monika sai priyanka avula'
names[0]
'm'
names[9]
'i'
names[20]
'a'
names[7:16]
'sai priya'
names[16:22]
'nka av'
names[-16:-8]
'i priyan'
names[-22:-1]
'ika sai priyanka avul'
#Slicing
names[::-1]
'aluva aknayirp ias akinom'
names[-8:]
'ka avula'
names[-13:-6]
'riyanka'
names[-14:-6]
'priyanka'
names[-1:-5]
''
names[:-1:-5]
''
names[-5:-1]
'avul'
names[-5:-1:-1]
''
names[-1:-5:-1]
'aluv'
#Membership
'avula' in names
True
'z' not in names
True
'sai' not in names
False
#String methods
s='codegnan'
s
'codegnan'
len(s)
8
ord(s)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    ord(s)
TypeError: ord() expected a character, but string of length 8 found
ord('s')
115
ord('M')
77
chr(89)
'Y'
chr(19)
'\x13'
che(21)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    che(21)
NameError: name 'che' is not defined. Did you mean: 'chr'?
chr(21)
'\x15'
sorted(s)
['a', 'c', 'd', 'e', 'g', 'n', 'n', 'o']
max(s)
'o'
min(s)
'a'
#Case Conversion methods
s="Monika Sai Priyanka"
s.upper()
'MONIKA SAI PRIYANKA'
s.lower()
'monika sai priyanka'
s.swapcase()
'mONIKA sAI pRIYANKA'
s.capitalize()
'Monika sai priyanka'
s.title()
'Monika Sai Priyanka'
#Alignment methods
s="Monika Sai Priyanka"
s.center(45,'#')
'#############Monika Sai Priyanka#############'
s.center(50,'.')
'...............Monika Sai Priyanka................'
s.ljust(50,'-')
'Monika Sai Priyanka-------------------------------'
s.rjust(50,'$')
'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Monika Sai Priyanka'
'123'.zfill(7)
'0000123'
'12345'.zfill(5)
'12345'
'1234'.zfill(2)
'1234'
#search and find methods
s="Monika Sai Priyanka"
s.find('a')
5
s.rfind('a')
18
s.index('a')
5
s.rindex('y')
14
s.count('a')
4
#Replace and Modify Methods
s="Monika Sai Priyanka"
s.replace('a','2')
'Monik2 S2i Priy2nk2'
s.replace('sai','chinni')
'Monika Sai Priyanka'
s.replace('Sai','chinni')
'Monika chinni Priyanka'
s.maketrans('aeiou','!@#$%')
{97: 33, 101: 64, 105: 35, 111: 36, 117: 37}
s.translate(s.maketrans('aeiou','!@#$%'))
'M$n#k! S!# Pr#y!nk!'
