
def readBalance():
    balanceFile= open("balance.txt",'r')
    balance = balanceFile.read()
    balanceFile.close()
    return balance

def writeBalance(balance):
    balanceFile = open("balance.txt", 'w')
    balanceFile.write(balance)
    balanceFile.close()

def readPin():
    pinFile = open("pin.txt", 'r')
    pin = pinFile.read()
    pinFile.close()
    return pin

def writePin(pin):
    balanceFile = open("pin.txt", 'w')
    balanceFile.write(pin)
    balanceFile.close()

repeat = "yes"

while(repeat=="yes"):
    print("1 --> Withdraw","\n2 --> check balance","\n3 --> change pin","\n4 --> exit")
    choice = int(input("Enter your choice = "))
    if(choice==1):
        pin = input("enter your pin = ")
        if(int(readPin())==int(pin)):
            amount = int(input("Enter a amount = "))
            if(amount<int(readBalance())):
                balance = int(readBalance()) - amount
                print(f"your transaction succesful\nyour balance is {balance}")
                writeBalance(str(balance))
            else:
                print("insuficiant balance")
        else:
            print("invalid pin")

    elif(choice==2):
        pin = input("enter your pin = ")
        if (int(readPin()) == int(pin)):
            print(f"you current balance = {readBalance()}")
        else:
            print("invalid pin")

    elif(choice==3):
        pin = input("enter your pin = ")
        if (int(readPin()) == int(pin)):
            newpin = input("Enter a new pin = ")
            conPin = input("Confirm your pin = ")
            if(newpin==conPin):
                writePin(str(newpin))
                print("pin changed")
            else:
                print("pin doesn't match")
        else:
            print("invalid pin")
    elif(choice==4):
        exit()
    else:
        print("Invalid choice")

    repeat = input("do you want to continue = ")