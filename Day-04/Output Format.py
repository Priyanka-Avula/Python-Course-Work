Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Comma-separation formatting
a=10
b=12.8
c='name'
print(a,b,c)
10 12.8 name
print('a='a,'b='b,'c='c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a='a,'b='b,'c=',c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a=',a,'b=',b,'c=',c)
a= 10 b= 12.8 c= name
print('a=',a,'b=',b,'c=',c,sep='')
a=10b=12.8c=name
print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
12.8
c=
name
print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	12.8	c=	name
print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n')
a=	10	b=	12.8	c=	name

print('a=',a,'b=',b,'c=',c,sep='\t',end='#')
a=	10	b=	12.8	c=	name#
#f-strings
print(f'a={a} b={b} c={c}')
a=10 b=12.8 c=name
#Modulus
print('a=%d b=%f c=%s')
a=%d b=%f c=%s
print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.800000 c=name
#Formatting
print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.8 c=name
print('a={} b={} c={}'.format(c,b,a))
a=name b=12.8 c=10
print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=12.8 c=name
print('a={2} b={1} c={0}'.format(a,b,c))
a=name b=12.8 c=10
