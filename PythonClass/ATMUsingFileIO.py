# def readPin():
#     file = open("pin.txt",'r')
#     a = file.read()
#     file.close()
#     return int(a)

# def readBalance():
#     file = open("balance.txt",'r')
#     a = file.read()
#     file.close()
#     return int(a)

# def writePin(a):
#     file = open("pin.txt",'w')
#     file.write(str(a))
#     file.close()

# def writeBalance(a):
#     file = open("balance.txt",'w')
#     file.write(str(a))
#     file.close()


# print("***********************ATM*****************************")
# print("\npress 1: Withdraw")
# print("press 2: check balance")
# print("press 3: Change pin")
# print("press 4: EXIT")

# choice = int(input("Enter your choice = "))

# if(choice==1):
#     upin = int(input("Enter your pin = "))
#     pin = readPin()
#     if(upin==pin):
#         amount = int(input("Enter a amount = "))
#         balance = readBalance()
#         if(amount<balance):
#             print(f"Transaction successful\nyour balance = {balance-amount}")
#             writeBalance(balance-amount)
#         else:
#             print("insufficient balance")
#     else:
#         print("wrong pin")

# elif(choice==2):
#     upin = int(input("Enter your pin = "))
#     pin = readPin()
#     if(upin==pin):
#         balance = readBalance()
#         print(f"your balance = {balance}")
#     else:
#         print("wrong pin")

# elif(choice==3):
#     upin = int(input("Enter your pin = "))
#     pin = readPin()
#     if(upin==pin):
#         npin = int(input("Enter a new pin = "))
#         cpin = int(input("confirm your pin = "))
#         if(cpin==npin):
#             print("Pin changed successfully")
#             writePin(npin)
#         else:
#             print("Pin dosen't match")
#     else:
#         print("wrong pin")

# elif(choice==4):
#     print("Thanks for using our service... :-)")
# else:
#     print("Wrong choice")




# number = 89
# if (number==1):
#     print("Odd")
# elif(number==2):
#     print("even")
# elif(number==3):
#     print("odd")
    


