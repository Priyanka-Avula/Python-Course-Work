#While loop is used when we don't know how many times we have to iterate
#Print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i+=1


#Print numbers from 10 to 1
i=10
while i>0:
    print(i)
    i-=1

#Multiples of 5 to 50
i=5
while i<=50:
    print(i)
    i+=5


#Print the string
s="while loop"
i=0
while i<len(s):
    print(s[i])
    i+=1


#Print the reverse of a string
s="while loop"
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1


#Display the list of numbers
l=[5467,5678,6789,9876]
i=0
while i<len(l):
    print(l[i])
    i+=1


#Divide the digit into single digit
n=8765
while n>0:
    print(n%10)
    n//=10


#Divide the digit into single digit and add the sum of digit
n=8765
sumofdigits=0
while n>0:
    sumofdigits+=n%10
    n//=10
print("Sum of digits:",sumofdigits)


#Divide the digit into single digit and add the product of digit
n=8765
productofdigits=1
while n>0:
    productofdigits*=n%10
    n//=10
print("Product of digits:",productofdigits)


#Reverse of a number
n=8754
res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res)


#Sum of even digits in a number
n=32547698
res=0
while n>0:
    rem=n%10
    if rem%2==0:
        res+=rem
    n//=10
print(res)


#Remove the zeroes from the list
l=[7,9,23,0,0,0,12,0,13,0,1,0,4,0,0,6,13,0]
while 0 in l:
    l.remove(0)
print(l)


#To print sum of first and last number in the list
l=[2,4,6,9,23,45,78]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1


#bill generation using while loop
data={
    "Rice":65,
    "Grains":50,
    "Oil":90,
    "Salt":25,
    "Cake":45,
    "Sugar":36,
    "Dal":87,
    "Eggs":200,
    "Cheese":90
}
bill=0
while True:
    product=input("Enter the product name or [E]xit:")
    if product=="e" or product=="E":
        print("Thanks for shopping")
        print("Total bill",bill)
    else:
        quantity=int(input("Enter the quantity:"))
        bill+=data[product]*quantity
