# if 
# if(condition):
#     statements

# age = int(input("Enter your age = ")) 
# if(age>18):
#     print("adult")
# print("boy")


# if else 
# if(condition):
#     statements
# else: 
#     statements

# age = int(input("Enter your age = "))
# if(age>18):
#     print("you can drive")
# else:
#     print("you cant drive")


# num = int(input("Enter a number = "))
# if(num%2==0):
#     print("number is even")
# else:
#     print("number is odd")


# num = int(input("Enter a year = "))
# if(num%4==0):
#     print("leap year")
# else:
#     print("not a leap year")


# print("Leap year") if(int(input("Enter a year = "))%4==0) else print("Not a leap year")

# *****home work******
# get value from user and check the positive or nagative
# get 3 angles from user and check the triangle or not




# *********if else ladder********** 
# if(condition):
#     statements
# elif(condition):
#     statements
# elif(condition):
#     statements
# . 
# . 
# . 
# else:
#     statements

# example
# a = int(input("Enter a number = "))
# if(a==1):
#     print("ONE")
# elif(a==2):
#     print("TWO")
# elif(a==3):
#     print("THREE")
# else:
#     print("wrong input")
# print("Hello")

# grades
# marks = 
# 0-35 = fail 
# 35 - 50 = c grade
# 50 - 75 = b grade 
# 75 - 90 = a grade 
# 90 - 100 = a+ grade





# nested if else 
# if(condition):
#     statements
#     if(condition):
#         statements
#         if(condition):
#               statements
#         else :
#             statements
#     else:
#         statements
# else:
#     statements       
        
# goa trip
# paise - 10000
# vehicle - available
# members - 6

# print("chalo goa jate hai")
# paise = int(input("tera kitna budget hai = "))
# if(paise>10000):
#     vehicle = input("gadi hai kya = ")
#     if vehicle=="yes":
#         members = int(input("tumhare sath kitne log hai = "))
#         if members>=6:
#             print("Goa me apka swagat hai...")
#         else:
#             print("sathme jane ke liye fds ko ready kro")
#     else:
#         print("arrange kro")
# else:
#     print("bhag ja bhikmange...")

# get three values from user and print greater value
# greater value
# a = int(input('enter the 1st value = '))
# b = int(input('enter the 2nd value = '))
# c = int(input('enter the 3rd value = '))
# if (a >= b) and (a >= c):
#     greater = a
# elif (b >= a) and (b >= c):
#     greater = b
# else:
#     greater = c
# print('The greater value is', greater)



# ---------------------------
# pin = 3336
# balance = 12000
# choice = 1 - withdraw 
#     enter a pin = 3336
#     enter amount = 1200
#     balance = 10800
# choice - 2 - check balance 
#     enter a pin = 3336
#     balance print 
# choice - 3 - change pin 
#     enter a pin = 3336
#     new pin = 9090
#     c pin = 9090
#     pin changed...!!
# choice 4 - exit 
#     print thank for using our service



# ATM
# pin = 4411
# balance = 15000
# print("1 : withdraw")
# print("2 : check balance")
# print("3 : change pin")
# print("4 : exit")
# choice = int(input('enter your choice = '))
# if choice == 1:
#     print('withdraw')
#     PIN = int(input('enter your pin = '))
#     if PIN == pin:
#         amount = int(input('enter your amount = '))
#         if amount <= balance:
#             print("balance =",balance-amount)
#         else:
#             print("insuficiant balance")
# elif choice == 2:
#     print('check balance')
#     code = int(input('enter your pin = '))
#     if code == pin:
#         print('balance =', balance)
#     else:
#         print('your pin is wrong')
# elif choice == 3:
#     print('change pin')
#     code = int(input('enter your pin = '))
#     if code == pin:
#         a = int(input('enter your new pin = '))
#         c = int(input('enter your confirm pin = '))
#         if c == a:
#             print('changed pin = ', a)
#             print('pin changed successfully...!!')
#         else:print("pin doesn't match")
#     else:
#         print("Wrong pin")
# elif choice == 4:
#     print('EXIT')
#     print('thank for using our service')




# ---------------ATM----------------
# print('WELCOME TO ATM ')
# pin = 1234
# balance = 10000
# print("1 : withdraw")
# print("2 : check balance")
# print("3 : change pin")
# print("4 : exit")
# service_code = int(input('ENTER SERVICE CODE = '))
# if(service_code==1):
#     print('WITHDRAW')
#     if(int(input("ENTER PIN = "))==1234):
#         amount = int(input('ENTER AMOUNT = '))
#         if(amount<balance):
#             print("WITHDRAW SUCCESSFUL")
#             print('CURRENT BALANCE : {a}'.format(a=balance-amount))
#         else:
#             print('INSUFFICIENT BALANCE')
#     else:
#         print('invaild pin')
# elif(service_code==2):
#     print('CHECK BALANCE')
#     if(int(input('ENTER PIN = '))==1234):
#         print(balance)
#     else:
#         print('INVAILD PIN')
# elif(service_code==3):
#     print('CHANGE PIN')
#     if(int(input('ENTER CURRENT PIN = '))==1234):
#         n_pin = int(input('ENTER NEW PIN = '))
#         c_pin = int(input('CONFIRM PIN = '))
#         if(n_pin==c_pin):
#             print('PIN CHANGED SUCCESSFULLY')
#         else:
#             print("CONFIRM PIN DOESN'T MATCH TO NEW PIN")
#     else:
#         print('INVAILD PIN')
# elif(service_code==4):
#     print("EXIT")
#     print("THANKS FOR USING OUR SERVICE")
# else:
#     print('INVAILD')

