#Weekend Planner based on Budget
budget=int(input("Enter the budget:"))
if budget>10000:
    print("Trip")
elif budget>5000:
    print("Resort Stay")
elif budget>3000:
    print("Movie and Dinner")
elif budget>1000:
    print("Cafe and Shopping")
elif budget>500:
    print("Street food and Park visit")
else:
    print("Stay Home")

#Greeting Based on Time
hour=int(input("Enter the Time:"))
if 5<=hour<=11:
    print("Good Morning")
elif 12<=hour<=16:
    print("Good Afternoon")
elif 17<=hour<=20:
    print("Good Evening")
elif 21<=hour<23:
    print("Good Night")
else:
    print("GoodNight Sleep Well")

#Hosting Plan
budget=int(input("Enter the budget:"))
if budget>10000:
    print("Cloud Hosting")
elif budget>5000:
    print("Business Hosting")
elif budget>2000:
    print("Premium Hosting")
else:
    print("Single Hosting")