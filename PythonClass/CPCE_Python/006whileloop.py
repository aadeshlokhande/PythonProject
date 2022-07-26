# while
# while(condition):
#     statements

# while(True):
#     print("happy new year 2022 ")


# a = 1
# while(a<=10):
#     print("Hello",end=" ")
#     a+=1


# ans = 2
# while(ans!=0):
#     a = int(input("Enter a number = "))
#     b = int(input("Enter a number = "))
#     ans = a + b 
#     print(f"{a} + {b} =  {ans}\n")




# print('WELCOME TO ATM ')
# pin = 1234
# balance = 10000
# a = 1
# while(a==1):
#     print("1 : withdraw")
#     print("2 : check balance")
#     print("3 : change pin")
#     print("4 : exit")
#     service_code = int(input('ENTER SERVICE CODE = '))
#     if(service_code==1):
#         print('WITHDRAW')
#         if(int(input("ENTER PIN = "))==1234):
#             amount = int(input('ENTER AMOUNT = '))
#             if(amount<balance):
#                 print("WITHDRAW SUCCESSFUL")
#                 print('CURRENT BALANCE : {a}'.format(a=balance-amount))
#             else:
#                 print('INSUFFICIENT BALANCE')
#         else:
#             print('invaild pin')
#     elif(service_code==2):
#         print('CHECK BALANCE')
#         if(int(input('ENTER PIN = '))==1234):
#             print(balance)
#         else:
#             print('INVAILD PIN')
#     elif(service_code==3):
#         print('CHANGE PIN')
#         if(int(input('ENTER CURRENT PIN = '))==1234):
#             n_pin = int(input('ENTER NEW PIN = '))
#             c_pin = int(input('CONFIRM PIN = '))
#             if(n_pin==c_pin):
#                 print('PIN CHANGED SUCCESSFULLY')
#             else:
#                 print("CONFIRM PIN DOESN'T MATCH TO NEW PIN")
#         else:
#             print('INVAILD PIN')
#     elif(service_code==4):
#         print("EXIT")
#         print("THANKS FOR USING OUR SERVICE")
#         a = 0
#     else:
#         print('INVAILD')

# **********total sum******** 
# Enter a number = 12
# Enter a number = 345
# Enter a number = 436
# Enter a number = 5345
# Enter a number = 0
# total sum = ??

# sum = 0
# num = 2
# while(num<1000):
#     num = int(input("Enter a number = "))
#     sum = sum + num 
# print("sum = ",sum-num)


# faulty calculator
# 10 + 20 = 124
# 23 - 43 = 34
# exit = "yes"
# while(exit=="yes"):
#     a = int(input("Enter a number = "))
#     b = int(input("Enter a number = "))
#     op = input("Enter a operator = ")
#     if(a==10 and b==20 and op=="+"):
#         print("10 + 20 = 124")
#     elif(a==23 and b==43 and op=="-"):
#         print("23 - 43 = 34")
#     else:
#         if(op=="+"):
#             print(a,"+",b,"=",a+b)
#         elif(op=="-"):
#             print(a,"-",b,"=",a-b)
#         elif(op=="*"):
#             print(a,"*",b,"=",a*b)
#         elif(op=="/"):
#             print(a,"/",b,"=",a/b)
#     exit = input("Do you want to continue = ")







# print("Calculator")
# print("1.Add")
# print("2.Substract")
# print("3.Multiply")
# print("4.Divide")
# print("5.Exit")
# x = 1
# while(x == 1):

#     choose = int(input("Enter Choice(1-5): "))

#     if choose == 1 :
#         a = int(input("Enter A:"))
#         b = int(input("Enter B:"))
#         c = a+b
#         print("Sum = ",c)
#     elif choose == 2:
#         a = int(input("Enter A:"))
#         b = int(input("Enter B:"))
#         c = a-b
#         print("Difference = ",c)
#     elif  choose == 3:
#         a = int(input("Enter A:"))
#         b = int(input("Enter B:"))
#         c = a*b
#         print("Product = ",c)
#     elif choose == 4:
#         a = int(input("Enter A:"))
#         b = int(input("Enter B:"))
#         c = a/b
#         print("Quotient = ",c)
#     elif choose == 5:
#         print("thanks for using")
#         x = 0
#     else:
#         print("invaild input")
