import logic as lg

if lg.login():
    while True:
        lg.menu()
        ch=input("Enter the choice:").upper()
        if ch=="C":
            lg.checkbalance()
        elif ch=="D":
            lg.deposit()
        elif ch=="W":
            lg.withdraw()
        elif ch=="V":
            lg.viewtransactions()
        elif ch=="E":
            print("--------------ThankYou, Visit Again---------------")
            break
        else:
            print("Enter the valid choice")

