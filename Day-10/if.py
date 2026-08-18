#Display best seller if sales are greater than 1000
sales=int(input("Enter the sales:"))
if sales>1000:
    print("Best Seller")

#If the eligibility and verfied subscription are true then we have to print verified badge granted
eligibility_account=eval(input("Eligible account:"))
verified_subscription=eval(input("Meta verified subscription:"))
if eligibility_account and verified_subscription:
    print("Verified Badge Granted")

#zepto rain delivery charges
rain_status=eval(input("Enter the rain status:"))
if rain_status:
    print("Extra charges applied")

