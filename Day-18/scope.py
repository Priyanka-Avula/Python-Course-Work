#Scope is divided into 2 types
#1.Local Scope- when we declare a variable inside a function it will be accessed within the function only.
#2.Global Scope- when we declare a variable outside of a function we can access it inside and outside of a function.
#Local Scope
def display():
    n=10
    print("Inside Function:",n)
display()
print("Outside Function:",n)
#Global Scope
def display():
    print("Inside Function:",n)
n=10
display()
print("Outside Function:",n)
#Global Variable-If we have a local variable we want to access it globally we can use global
def display():
    global n
    n=10
    print("Inside Function:",n)
display()
print("Outside Function:",n)
#When we declare a variable as global we should not pass that variable as a parameter 
#When we write global inside a function it will affect outside automatically.
def display():
    global n
    n+=10
    print("Inside Function:",n)
n=10
display()
print("Outside Function:",n)
#NonLocal Variable-Inside a function we can access when we have nested functions and it will not affect the outside function.
def display():
    course="PFS"
    def update():
        nonlocal course
        course="JFS"
        print("Inner Function:",course)
    update()
    print("Outer Function:",course)
display()
#When we declare any built in function as a variable it looses its functionality and starts working as a variable.
l=[1,2,3,4,5]
print(max(l))

max=20
print(max(l))  #In this case we get error because we used built in function as a variable

l=[1,2,3,4,5]
print(sum(l))
sum=20
print(sum)

