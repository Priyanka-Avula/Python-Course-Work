#Sys Module
import sys
print(sys.argv)  #This used to pass the parameters at the runtime and it is going to provide the output in the form of list
print(sys.path)  #Returns the path of the py files
print(sys.version)  #Returns the py version
print("start")
sys.exit()     #Stops the program
print("end")

#Platform module
import platform
print(platform.system())    #Gives whether it is windows/linux etc..
print(platform.release())   #Gives the version
print(platform.processor()) #Gives about the processror 

#Math Module
import math
print(math.pi)   #Returns the pi value
print(math.e)    #Returns the euler's value 
print(math.log(2,2))   #Used to get log values
print(math.sin(30))    #Used for sin values
print(math.cos(60))    #Used for cos values
print(math.tan(45))    #used for tan values
print(math.degrees(30))   #Used to convert from degrees to radians
print(math.radians(60))   #Used to convert from radians to degrees
print(math.factorial(6))  #used to find factorial
print(math.gcd(8,12))     #Used to find greatest common divisor of two numbers
print(math.sqrt(49))      #To find square root of a number(returns decimal value)
print(math.pow(2,4))      #To find the power of two numbers(returns decimal value)
print(round(12.001))      #Rounds to before value when it is less than .5
print(round(12.9966))     #Rounds to after value when it is greater than .5
print(math.ceil(12.001))  #It always gives greater value when we use ceil()
print(math.ceil(12.9966))
print(math.floor(12.001)) #It always gives lower values when we use floor()
print(math.floor(12.9966))

#Random Module
import random
random.seed(8)    #When we don't want to change the output 
print(random.random())   #Generates a random value from 0.0 to 1.0
print(random.randint(2,6))  #Generates the int value in the given range
print(random.uniform(3,8))  #Generates the float value in the given range
l=["r","p","s"]
print(random.choice(l))     #Generates a choice from the list
lang=["python","java","sql","html"]  #Generates the choices based on our requirement
print(random.choices(lang,k=2))
random.shuffle(lang)       #Shuffle the order
print(lang)

#Collections Module
from collections import Counter   #Counter is used to find the frequency and it won't give in sequential order
s="python programming" 
res=Counter(s)
print(res)
from collections import defaultdict  #It is used when you want a default value to be automatically created for a key that does not exist, instead of getting a KeyError.
products=["sugar","salt","milk"]
res=defaultdict(list)
for i in products:
    res[i].append(['des','rev','com'])
print(res)

from collections import defaultdict
s="python programming"
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)

from collections import deque
l=deque([])   #in deque module we have 4 methods as pop(),popleft(), append(), appendleft()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.append(50)
l.append(60)
l.popleft()
print(l)

from collections import deque
l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)

