#Username and Password Login
username=input("Username:")
password=input("Password:")
if username=="admin" and password=="admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")


#Product Search
products=["laptop","mouse","bag"]
search=input("Enter the product:")
if search in products:
    print(f"{search} found")
else:
    print(f"{search} not found")

#Delivery Charge Calculation
bill=int(input("Enter the bill:"))
if bill>99:
    print("Final Bill",bill)
else:
    print("Final bill + delivery charge",bill+30)