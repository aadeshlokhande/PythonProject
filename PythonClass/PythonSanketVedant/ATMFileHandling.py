# sanket ATM 
print("press 1 : withdraw")
print("press 2 : balance check")
print("press 3 : change pin")
print("press 4 : exit")
choice = int(input("Enter Your Choice ="))
if(choice==1):
    upin = int(input("Enter a pin ="))
    f = open("pin.txt","r")
    fpin = int(f.read())
    f.close()

    if(upin==fpin):
        amount= int(input("Enter a Amount ="))
        if(amount>0):
            d = open("bal.txt","r")
            bal = int(d.read())
            d.close()
    
            if(amount<bal):
                print("Transaction is Successful")
                print(f"current balance ={bal-amount}")
                d = open("bal.txt","w")
                bal = int(d.write(f"{bal-amount}"))
                d.close()
            else:
                print("low balance")
        else:
            print("amount can't be negetive value")
    else:
        print("you pin is wrong")
        
elif(choice==2):

    upin = int(input("Enter a pin ="))
    f = open("pin.txt", "r")
    fpin = int(f.read())
    f.close()

    if(upin==fpin):

        d = open("bal.txt", "r")
        bal = int(d.read())
        d.close()

        print("current balance =",bal)
    else:
        print("you enter a wrong pin ")
        
elif(choice==3):
    upin = int(input("Enter a pin ="))

    f = open("pin.txt", "r")
    fpin = int(f.read())
    f.close()

    if(upin==fpin):
        npin = int(input("Enter a New pin ="))
        lpin = int(input("Confirm a pin ="))
        if(npin==lpin):
            print("pin changed successful")
            f = open("pin.txt", "w")
            f.write(f"{npin}")
            f.close()
        else:
            print("pin does't match")
    else:
        print("your pin is wrong")
elif(choice==4):
    print("thanks for uing our service")
else:
    print("invalid number")