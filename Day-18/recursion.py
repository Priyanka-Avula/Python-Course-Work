#Recursion-A function calling itself is called recursion and if it reaches the base condition it has to stop the process.
#Syntax
'''def func(args):
    if base:
        return 
    fun(update args)
fun(para)'''
#Print 1 to 10 numbers
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)
#print 10 to 1 numbers
def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)
#Iterate the string
def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)
s=input("Enter the string:")
display(s,0)
