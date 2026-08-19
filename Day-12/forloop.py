#Syntax of for loop
'''for var in seq:
    stmts'''
#str
s="Python Programming"
for i in s:
    print(i)

#list
l=[1,2,3,4,5]
for num in l:
    print(num)

#tuple
prices=(987,6543,678,123567)
for price in prices:
    print(price)

#set
names={"priyanka","sai","monika"}
for name in names:
    print(name)

#dictionary
d={1:2,3:4,5:6,7:8}
for i in d:
    print(i,d[i])

#Range always gives us the numeric values
#Syntax for range
#range(start,end+1,step):
#Print 1 to 10 numbers
for i in range(1,11):
    print(i)

#print even numbers upto 20
for i in range(2,21,2):
    print(i)

#Print multiples of 5 upto 100
for i in range(5,101,5):
    print(i)

#Print 5 to 0 in 
for i in range(5,0,-1):
    print(i)

#print odd numbers from 19 to 1
for i in range(19,0,-2):
    print(i)

#to know the index of string
s="monika sai priyanka"
for i in range(len(s)):
    print(i,s[i])

#to know the index of list
s=[123,345,2479,247998]
for i in range(len(s)):
    print(i,s[i])

#to know the index of tuple
s=(234,765,1278,4086)
for i in range(len(s)):
    print(i,s[i])

#enumerate is used to get in a sequence and the output is going to be a tuple
#str(enumerate)
s="monika sai priyanka"
for i in enumerate(s):
    print(i[0],i[1])

s="monika sai priyanka"
for i in enumerate(s):
    print(i)

#list
s=[6789,235,8753,9631]
for i in enumerate(s):
    print(i[0],i[1])

s=[6789,235,8753,9631]
for i in enumerate(s):
    print(i)

#tuple
s=(6789,235,8753,9631)
for i in enumerate(s):
    print(i[0],i[1])

s=(6789,235,8753,9631)
for i in enumerate(s):
    print(i)

#set
s={12,643,8765,2345}
for i in enumerate(s):
    print(i[0],i[1])

s={12,643,8765,2345}
for i in enumerate(s):
    print(i)

#dictionary
d={1:2,3:4,5:6,7:8}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

d={1:2,3:4,5:6,7:8}
for i in enumerate(d):
    print(i)

#Break is used to terminate the loop whenever it reaches the condition
for i in range(1,11):
    if i==5:
        break
    print(i)

#Continue is used to skip the current iteration and continues the next process
for i in range(1,11):
    if i==5:
        continue
    print(i)

#for-else
#when there is no break statement encountered we use else block
for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print("End of Loop")


l=[12,14,16,18,20]
n=26
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")


#Unlocking phone
pin=1234
for i in range(5):
    epin=int(input("Enter the pin:"))
    if epin==pin:
        print("Unlock Phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds")

#whether a number is prime or not
n=int(input("Enter a number:"))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime")
        break
else:
    print("Prime")
