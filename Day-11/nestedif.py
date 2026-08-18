#Instagram Story Visibilty
follow_account=eval(input("Follow Account:"))
if follow_account:
    close_friend=eval(input("Close Friend:"))
    if close_friend:
        print("Story Visibile")
    else:
        print("Not in Close friends List")
else:
    print("Follow the account first")

#BGMI Tournament Entry
registration=eval(input("Registered:"))
if registration:
    fee=eval(input("Fee Paid:"))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")

#Google Drive File Access
link=eval(input("Link Active:"))
if link:
    Permission=eval(input("Permission Granted:"))
    if Permission:
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")


#All conditional Statements
data={
    'priyanka':{'status':True,'python':98,"mysql":89,"flask":76},
    'monika':{'status':False,'python':65,"mysql":74,"flask":90},
    'prasanna':{'status':True,'python':88,"mysql":69,"flask":55},
    'gayathri':{'status':True,'python':78,"mysql":55,"flask":42}
}
name=input("Enter the name:")
if name in data:
    if data[name]["status"]:
        sum=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=sum/3
        print(f"Hello {name}!!!!")
        print(f"your average score is {avg}")
        if avg>=90:
            print("Outstanding Performance")
        elif avg>=70:
            print("Very Good")
        elif avg>=60:
            print("Better Luck next time,work hard")
        elif avg>=30:
            print("Average,do hard work")
        else:
            print("you have failed the exam")
    else:
        print(f"{name} you did not attend the exam, bring your parents!!")