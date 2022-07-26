def readbalance():
    balanceFile= open("balance1.txt",'r')
    balance= balanceFile.read()
    balanceFile.close()
    return balance

def writebalance(balance):
    balanceFile= open("balance1.txt",'w')
    balanceFile.write(balance)
    balanceFile.close()

def readpin():
    pinFile= open("pin1.txt",'r')
    pin= pinFile.read()
    pinFile.close()
    return pin

def writepin(pin):
    pinFile= open("pin1.txt",'w')
    pinFile.write(pin)
    pinFile.close()

repeat = "yes"

while(repeat=="yes"):
    print("1--> Withdraw","\n2--> check balance","\n3--> change pin","\n4--> exit")

    choice= int(input("enter your choice= "))
    if(choice==1):
        pin = input("enter your pin= ")
        if(int(readpin())==int(pin)):
            amount = int(input("enter your amount=  "))
            if(amount<int(readbalance())):
                balance = int(readbalance()) - amount
                print(f"transcation successful\nyour balance is {balance}")
            else:
                print("insufficient amount")
        else:
            print("incorrect pin")

    if(choice==2):
        pin = input("enter your pin= ")
        if (int(readpin()) == int(pin)):
            print(f"your current balance is {readbalance()}")
        else:
            print("invalid pin")

    if(choice==3):
        pin = input("enter your pin=  ")
        if (int(readpin()) == int(pin)):
            newpin= input("enter new pin= ")
            conpin= input("confirm your pin=  ")
            if(newpin==conpin):
                writepin(str(newpin))
            else:
                print("pin doesn't match")
        else:
            print("invalid pin")

    if(choice==4):
        exit()
    else:
        print("invalid choice")

    repeat = input("do you want to continue=  ")


