#Print 10 to 1 numbers using base conditions we are using for 1 to 10 numbers.
#If we write print() after recursion it is going to give the output in reverse order.
def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)

#Reverse the string
def display(s,n):
    if n==len(s):
        return
    display(s,n+1)
    print(s[n],end="")
s=input("Enter the string:")
display(s,0)

#Break the string based on the given width
def display(s,ind,w):
    if len(s)-w+1==ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)
s=input("Enter a string:")
w=int(input("Enter the width:"))
display(s,0,w) 

#Take a list of elements and return their sum
def display(l,ind):
    if ind==len(l):
        return 0
    return l[ind]+display(l,ind+1)
l=list(map(int,input("Enter the elements:").split(',')))
print(display(l,0))

#Sum of digits
def display(n):
    if n==0:
        return 0
    return n%10 + display(n//10)
n=int(input("Enter the digit:"))
print(display(n))

#Product of digits
def display(n):
    if n==0:
        return 1
    return n%10 * display(n//10)
n=int(input("Enter the digit:"))
print(display(n))

#Factorial of a number
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input("Enter a number:"))
print(factorial(n))

#Fibonacci Series using conditional statements and loops
n=int(input("Enter a number:"))
if n==1:
    print(0)
elif n==2:
    print(1)
else:
    a,b=0,1
    print(a,b)
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=" ")
    
 #Fibonacci Series using Recursion
def fibanocci(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    return fibanocci(a-1)+fibanocci(a-2)
a=int(input("Enter the number:"))
for i in range(a):
    print(fibanocci(i))



