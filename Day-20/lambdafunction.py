#A lambda function is a small, anonymous function (a function without a name) that can take any number of arguments but contains only one expression.
'''Syntax 
variable_name = lambda arguments : expression'''

#Print name 
wish=lambda name:f"Welcome to course {name}"
print(wish("Monika"))
print(wish("Priyanka"))

#Calculate GST
gst=lambda price:price+price*0.18
print(gst(800))
print(gst(1921))

#Calculate average
avg=lambda a,b,c:(a+b+c)/3
print(avg(2,5,8))
print(avg(9,8,6))

#Calculate even or not
iseven=lambda a:"Even" if a%2==0 else "Odd"
print(iseven(8))
print(iseven(5))

#Largest of 3 numbers
largest=lambda a,b,c:a if a>b and b>c else (b if b>c else c)
print(largest(89,65,43))
print(largest(34,12,4))

#Vowel or not
isvowel=lambda a:"Vowel" if a in "aeiouAEIOU" else "Consonant"
print(isvowel('m'))
print(isvowel('a'))

#Add 10 to each value in a list
l=[1,2,3,4,5,7,8]
update=list(map(lambda i:i+10,l))
print(update)

#Giving discount to every element
t=(789,234,765,126)
discount=list(map(lambda i:i-i*0.3,t))
print(discount)

#Printing odd numbers
l=[1,2,3,4,5,7,8]
update=list(filter(lambda i:i%2!=0,l))
print(update)

#Printng numbers greater than 1000
t=(789,5674,9876,1234,743)
greater=list(filter(lambda i:i>1000,t))
print(greater)

#Extract domains
l=["monika@gmai.com","monika@outlook.com","monika@yahoo.com"]
res=list(map(lambda i:i.split('@')[-1],l))
print(res)

#Reduce is used to compress long units into one unit
#Add list of elements into a single unit
from functools import reduce
l=[4,2,4,6,86,543,12]
res=reduce(lambda sum,i:sum+i,l)
print(res)

#Product of elements
from functools import reduce
l=[42,2,678,23]
res1=reduce(lambda product,i:product*i,l)
print(res1)

#Checking seat availabilty
seats={"s1":True,
       "s2":False,
       "s3":False,
       "s4":False,
       "s5":True,
       "s6":True}
ava=list(filter(lambda i:seats[i]!=True,seats))
print(ava)

#Printing products price greater than 50
products={
    "eggs":80,
    "sugar":60,
    "salt":20,
    "butter":70
}
res=list(filter(lambda i:products[i]>50,products))
print(res)

#Printing prices in ascending or descending order
products={
    "eggs":80,
    "sugar":60,
    "salt":20,
    "butter":70
}
print(dict(sorted(products.items(),key=lambda i:i[1])))
#If we want in reverse order
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))

