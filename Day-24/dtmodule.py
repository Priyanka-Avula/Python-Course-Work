#DateTime Module
from datetime import date
t=date.today()
print(t)
print(t.day)
print(t.month)
print(t.year) 
print(t.weekday())

#Validate the dob
year,month,day=list(map(int,input("[YYYY-MM-DD]").split("-")))
print(date(year,month,day))

#Time
from datetime import time
tm=time(21,6,19,25)
print(tm)
print(tm.hour)
print(tm.minute)
print(tm.second)
print(tm.microsecond)

#DateTime
from datetime import datetime
dt=datetime.now()
print(dt)
print(dt.strftime("%d-%m-%y"))  #%y gives 2 digits of an year
print(dt.strftime("%d-%m-%Y"))  #%Y gives 4 digits of an year
print(dt.strftime("%d-%m-%Y %H:%M:%S"))
print(dt.strftime("%d-%m-%Y %H:%M:%S %p"))   #%p gives whether it is AM or PM
print(dt.strftime("%d-%m-%Y %I:%M:%S %p"))   #%I gives 12 hours time
print(dt.strftime("%d-%b-%Y %I:%M:%S %p"))   #%b gives three letters of the month name
print(dt.strftime("%d-%B-%Y %I:%M:%S %p"))   #%B gives the full month name
print(dt.strftime("%a,%d-%B-%Y %I:%M:%S %p")) #%a gives three letters of a day
print(dt.strftime("%A,%d-%B-%Y %I:%M:%S %p")) #%A gives the full name of the day

#Timedelta
from datetime import timedelta,datetime,date
dt=datetime.now()
t=date.today()
t7=t+timedelta(days=7)
m15=dt+timedelta(minutes=15)
print(t7,m15)

#Itertools
from itertools import permutations,combinations
s="abcd"
res1=list(permutations(s,2))
res2=list(combinations(s,2))
print(["".join(i) for i in res1])
print(["".join(i) for i in res2])