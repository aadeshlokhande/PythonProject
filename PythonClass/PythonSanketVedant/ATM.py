pin = 1234 
bal = 12000

print("press 1: withdraw")
print("press 2: Check balance")
print("press 3: Change pin")
print("press 4: Exit")
choice = int(input("Enter your choice = "))

if(choice==1):
    upin = int(input("enter your pin = "))
    if(upin==pin):
        amount= int(input("enter a amount = "))
        if(amount<bal):
            print("transaction sucessfull")
            print(f"current balance = {bal-amount}")
        else:
            print("low balance")
    else:
        print("wrong pin")

elif(choice==2):
    upin = int(input("enter your pin = "))
    if(upin==pin):
        print("Current balance =",bal)
    else:
        print("wrong pin")

elif(choice==3):
    upin = int(input("enter your pin = "))
    if(upin==pin):
        npin = int(input("Enter a new pin = "))
        cpin = int(input("Confirm your pin = "))
        if(npin==cpin):
            print("pin changed sucessfull")
        else:
            print("pin doesn't match")
    else:
        print("Wrong pin")
        
elif(choice==4):
    print("Thanks for using our service")
else:
    print("invalid input")

        
            