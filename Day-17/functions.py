#Syntax for function
#Function defining
'''def functionname(args):
    #stmts
    return (optional)
#function Calling
functionname(parameters)'''

#Printing Final bill after adding GST
def gst(price):
    print("Original Price:",price)
    print("Final Price:",price+price*0.18)
gst(1000)
gst(700)
gst(660)
gst(2000)
gst(7500)

#Printing tables from 1 to 10
def table(n):
    print(f"{n}-Table")
    print("--------------------------")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
for i in range(1,21):
    table(i)

#Checking leap year or not
#When we write return we need to print outside the function mandatorily if we write print inside the function there is no need of printing outside the function
def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
print(isleap(2006))
print(isleap(2012))
print(isleap(1997))

#Checking whether a number is prime or not
def isprime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return "Not a Prime"
    return "Prime"
print(isprime(16))
print(isprime(7))
print(isprime(9))

#Positional Arguments
def display(name,email,password):
    print("name:",name)
    print("email:",email)
    print("password:",password)
display("monika","monika@gmail.com","monika@456")
display("monika@456","monika","monika@gmail.com")
display("monika@gmail.com","monika@456","monika")

#Keyword Arguments
def display(name,email,password):
    print("name:",name)
    print("email:",email)
    print("password:",password)
display(name="monika",email="monika@gmail.com",password="monika@456")
display(password="monika@456",name="monika",email="monika@gmail.com")
display(email="monika@gmail.com",password="monika@456",name="monika")

#Default Arguments
def display(name,email,password=None):
    print("name:",name)
    print("email:",email)
    print("password:",password)
display("monika","monika@gmail.com")
display("monika","monika@gmail.com","monika@456")

#Variable Length Arguments
def display(*names):
    print(names)
display("monika")
display("monika","sai")
display("monika","sai","priyanka")

def display(**names):
    print(names)
display(n1="monika")
display(n1="monika",n2="sai")
display(n1="monika",n2="sai",n3="priyanka")
