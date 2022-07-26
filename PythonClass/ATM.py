pin = 1122
balance = 10000

print("***********************ATM*****************************")
print("\npress 1: Withdraw")
print("press 2: check balance")
print("press 3: Change pin")
print("press 4: EXIT")

choice = int(input("Enter your choice = "))

if(choice==1):
    upin = int(input("Enter your pin = "))
    if(upin==pin):
        amount = int(input("Enter a amount = "))
        if(amount<balance):
            print(f"Transaction successful\nyour balance = {balance-amount}")
        else:
            print("insufficient balance")
    else:
        print("wrong pin")

elif(choice==2):
    upin = int(input("Enter your pin = "))
    if(upin==pin):
        print(f"your balance = {balance}")
    else:
        print("wrong pin")

elif(choice==3):
    upin = int(input("Enter your pin = "))
    if(upin==pin):
        npin = int(input("Enter a new pin = "))
        cpin = int(input("confirm your pin = "))
        if(cpin==npin):
            print("Pin changed successfully")
        else:
            print("Pin dosen't match")
    else:
        print("wrong pin")

elif(choice==4):
    print("Thanks for using our service... :-)")
else:
    print("Wrong choice")




# a = "nobita"
# b = "shizuka"
# sen = f'{b} likes {a}'

# print(sen)