data={
    123456:{"name":"Monika","pin":1234,"balance":5000,"history":[]},
    234567:{"name":"Sai","pin":1234,"balance":11000,"history":[]},
    345678:{"name":"Priyanka","pin":1234,"balance":3000,"history":[]}
}

def login():
    global acc_num
    acc_num=int(input("Enter the account number:"))
    pin=int(input("Enter the pin:"))
    if acc_num in data and data[acc_num]["pin"]==pin:
        print("Login Successful")
        return True
    else:
        print("Invalid Login")

def menu():
    print(f"Welcome to the ATM,{data[acc_num]['name']}")
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transactions")
    print("[E]xit")

def checkbalance():
    print(f"Hello {data[acc_num]['name']}")
    print("Current Balance:",data[acc_num]["balance"],end="\n\n")

def deposit():
    amount=int(input("Enter the amount to deposit:"))
    data[acc_num]["balance"]+=amount
    data[acc_num]["history"].append(f"{amount} is deposited")
    print(f"{amount} is deposited successfully")
    checkbalance()

def withdraw():
    amount=int(input("Enter the amount to withdraw:"))
    if data[acc_num]["balance"]>=amount:
        data[acc_num]["balance"]-=amount
        data[acc_num]["history"].append(f"{amount} is withdraw")
        print(f"{amount} is withdraw successfully")
        checkbalance()

def viewtransactions():
    if data[acc_num]["history"]:
        print("========Transaction History=======")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print("========End of the History===========")
    else:
        print("No Transaction History")


    