#Pass by Value - when we pass immutable datatypes inside a function they are not going to affect outside(int,float,complex,str,tuple,bool)
#Pass by Reference - when we pass mutable datatypes inside a function they are going to affect outside also(list,dict,set) 
#Int
def display(n):
    n+=10
    print("Inside the Function:",n)
n=20
display(n)
print("Outside the Function:",n)
#Float
def display(n):
    n+=10.6
    print("Inside the Function:",n)
n=20.3
display(n)
print("Outside the Function:",n)
#String
def display(n):
    n+="python"
    print("Inside the Function:",n)
n="java"
display(n)
print("Outside the Function:",n)
#Boolean
def display(n):
    n=True
    print("Inside the Function:",n)
n=False
display(n)
print("Outside the Function:",n)
#Complex
def display(n):
    n+=10+3j
    print("Inside the Function:",n)
n=16+5j
display(n)
print("Outside the Function:",n)
#Tuple
def display(n):
    n+=(2,3,4,5)
    print("Inside the Function:",n)
n=(1,2,3)
display(n)
print("Outside the Function:",n)
#List
def display(n):
    n+=[1,2,3,4]
    print("Inside the Function:",n)
n=[5,6,7]
display(n)
print("Outside the Function:",n)
#Set
def display(n):
    n.add(8)
    print("Inside the Function:",n)
n={5,6,7}
display(n)
print("Outside the Function:",n)
#Dictionary
def display(n):
    n[9]=0
    print("Inside the Function:",n)
n={5:6,7:8}
display(n)
print("Outside the Function:",n)
