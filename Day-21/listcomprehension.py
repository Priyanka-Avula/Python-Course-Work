#Printing numbers in between a range
l=[i for i in range(1,11)]
print(l)

#Printing even numbers in a range
m=[i for i in range(2,11,2)]
print(m)

#Printing factors
n=12
f=[i for i in range(1,n+1) if n%i==0]
print(f)

#Add even number in place of even add 0 in place of add
#when we have multiple conditions we have to write them in the right side only
x=[1,2,3,4,5,6,7,8,9]
y=[i if i%2==0 else 0 for i in x]
print(y)

#print the nested list
l=[[j for j in range(1,4)] for i in range(3)]
print(l)

#General method to print nested list
l=[]
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)

#Print the set
s={i for i in range(1,11)}
print(s)

#Print the dictionary
p={i:i*i for i in range(1,11)}
print(p)

