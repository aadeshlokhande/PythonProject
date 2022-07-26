# ************keyword************
# import keyword
# for i in keyword.kwlist:
#     print(i)



# ************* Variable - cantainer *******
# a = 10
# rules:
# 1) we can't start variable name with numbers
# ex: 12aadesh, 90name, 99city this are not alowed
# 2) we can use underscore(_)
# ex: _name, first_name, lastname_
# 3)we can use numbers, letters and underscore only
# ex: new_city2, last_name23,
# 4) variable names are case sensative
# ex a = 10, A = 20
# age = 10
# Age = 20
# AGE = 30

# *************Data Type***********
# int = integer values = 123,345,342,-1312,-1235
# float = decimal number = 5.8, 40.7, 1.5
# string = "aadesh","90","a"
# a = 10
# print(type(a))
# b = 10.7
# print(type(b))
# c = "10.7"
# print(type(c))

# a = int("10")
# print(type(a))



# ************ tuple ***************
# immutable
# a = (12,12.5,"12",32,42,51,57,52,42,32)
# print(len(a))
# print(a[3])
# print(a[-3])
# print(a[2:6])
# print(a[-7:-2])
# print(a[:5])
# print(a[4:])
# print(a[::2])
# print(a[::-1])

# b = a.count(52)
# print(b)
# tuple = (12,3,54,53,434,5,(123,5,43,5,6,675))
# print(tuple[6][2])

# ****************list**********************
# mutable
# a = [12,43,65,75.5,'34',"Aadesh","vibhor",345]
# print(len(a))
# print(a[3])
# print(a[-3])
# print(a[2:6])
# print(a[2:6][::-1])
# print(a[-7:-2])
# print(a[:5])
# print(a[4:])
# print(a[::2])
# print(a[::-1])

# b = ["tamater", "aalu", "kande"]
# print(b)
# b.append("mirchi")
# print(b)
# b.insert(2,"wange")
# print(b)
# b.pop(0)
# print(b)
# b.remove("mirchi")
# print(b)
# b[2] = "bhendi"
# print(b)

# ****************dictionary******
# dic = {"mirchi":10, 15:"wange", "sambhar":5}
# print(dic[15])
# print(dic.keys())
# print(dic.values())
# dic.pop(15)
# print(dic)

# ******************string****************
# str = "My name is Doraemon "
# print(str[8])
# print(str[4:10])
# print(str.count("a"))
# print(str.find("is"))
# print(str.lower())
# print(str.upper())
# print(str.capitalize())
# print(str.join("FOR"))
# print(str.strip())
# print(str.split("a"))
# name = "vibhar"
# age = 28
# p = f"my name is {name} and my age is {age}"
# print(p)
# o = "my name is {1} and my age is {0}".format(age,name)
# print(o)

# a = "double quates"
# b = 'single quates'
# c = """double triple quates"""
# d = '''single triple quates'''

# a = 'chandra shekar azad said "tum mujhe khun do mai tumhe aazadi dunga"'
# b = "this is my mom's mobile"
# c = """[1:02 am, 16/10/2021] Vibhor Dada: Ok
# [1:03 am, 16/10/2021] Vibhor Dada: Aawaj nahi yet ahe
# [1:04 am, 16/10/2021] Vibhor Dada: 1min
# [1:04 am, 16/10/2021] Vibhor Dada: Aawaj speaker mdhun ahet ahe
# [1:04 am, 16/10/2021] Vibhor Dada: Headphone mdhun nahi"""

# d = '''single triple quates'''
# print(a)

# escape charecters
# a = "chandra shekar \\n azad \\said \"tum mujhe khun do mai tumhe aazadi dunga\""
# print(a)

# \n = new line
# \t = tab 


# # ********************set***************
# a = {45,687,98,89,89,98,6,76,36}
# print(a)

# *************operator***************
# a = 10
# b = 20 
# Arithmetic operator
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# Relational operator
# print(a < b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a <= b)
# print(a >= b)

# logical operator
# And - ziddi operator
# cake        icecream        feel 
# 0               0           0
# 0               1           0
# 1               0           0
# 1               1           1


# or - gareeb manacha manus
# cake            icecream        feel
# 0                   0           0
# 0                   1           1
# 1                   0           1
# 1                   1           1

# not - ultya khopdicha
# 1 ---> 0
# 0 ---> 1


# assignment operator
# a = 10
# a = a * 2
# a *= 2



# *************Conditional statements********
# 1) if
# syntax
# if (condition):
#     statements

# a = int(input("Enter a number = "))
# if(a%2==0):print(a)

# if 10>9 : print("true")


# if else 
# syntax 
# if (condition):
#     statements1
# else:
#     statements2

# age = int(input("Enter your age = "))
# if(age>18):
#     print("you can drive")
# else:
#     print("you can't drive")

# num = int(input("Enter a number = "))
# if(num%2==0):
#     print("Even")
# else:
#     print("odd")

# trueStatement if (condition) else falseStatement
# print("EVEN") if int(input("number = "))%2==0 else print("ODD")
# one liner code

# ____________Pratice______________

# positive nagative
# take 3 angles from user and check this is tringle or not
# leap year



# nested if else 
# syntax 
# if(condition):
#     statements
#     if(condtion):
#         statements
#         if (condition):
#             statements
#         else:
#             statements
#     else:
#         statements
# else:
#     statements        


# gender, age, education
# gender = input("Enter your gender M/F = ").lower()
# if(gender=='m'):
#     age = int(input("Enter your age = "))
#     if(age>21):
#         education = input("Enter your education = ").lower()
#         if(education=='be'):
#             print("you are eligible for marrage")
#         else:
#             print("you need to complete BE to get marry")
#     else:
#         print("You need to complete 21 years to get marry")
# else:
#     print("Sorry at this time this survey is for Men only")





# if else ladder
# syntax 
# if(condition):
#     statements
# elif (condition):
#     statements
# elif (condition):
#     statements
# elif (condition):
#     statements
# elif (condition):
#     statements
# else:
#     statements


# a = int(input("Enter a number = "))
# if(a==1):
#     print("ONE")
# elif(a==2):
#     print("TWO")
# elif(a==3):
#     print("THREE")
# else:
#     print("Wrong input")

# ___________practice__________
# get date and print day




# loop 
# for 
# syntax:
# for variable in Collection_of_data:
    # statement
# a = int(input('number ='))
# for i in range(1,11):
#     print(i*a) 

# a = [12,45,48,79,16]
# for i in a:
#     print(i)

# a = "Hello buddy"
# for i in a:
#     print(i.upper())


# nested for 
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=' ')
#     print()
    
# ____________practice___________
# print 1 to 10 tables

# * * * * *
# * * * *
# * * *
# * * 
# *



# while 
# syntax 
# while (condition):
#     statement

# a = 1
# b = 1
# while (a!=0)and(b!=0):
#     a = int(input("enter a number = "))
#     b = int(input("enter a number = "))
#     print(f"{a} + {b} = {a+b}")


# ex = "yes"
# while ex=="yes":
#     a = int(input("enter a number = "))
#     b = int(input("enter a number = "))
#     print(f"{a} + {b} = {a+b}")
#     ex = input('do you want to continue = ')

# ____________practice___________
# get numbers from user and print sum of numbers


# **************************function********************
# def function_name(arguments):
#     statements
#     return value

# function_name(arguments)



# _______with argument with return__________
# def add(a,b):
#     c = a+b 
#     return c

# print(add(10,15))


# with argument without return
# def add(a,b):
#     c = a + b 
#     print(c)

# add(12,45)


# without argument with return 
# def add():
#     a = 10
#     b = 20
#     c = a+b 
#     return c 

# print(add())

# without argument without return 
# def add():
#     a = 10
#     b = 20
#     c = a+b 
#     print(c)

# add()



# # function overloading
# def calc(op,a,b):
#     if(op=="+"):
#         print(f"{a} + {b} = {a+b}")
#     if(op=="-"):
#         print(f"{a} - {b} = {a-b}")

# calc("+",12,14)
# calc("-",20,10)



# import family

# family.dada()
# family.tai()
# print(family.b) 

# from family import dada 
# dada()


# recursion 

# def Fname():
#     statements
#     Fname()
# fname()



# 5! = 5x4x3x2x1
# 4! = 4x3x2x1
# 5! = 5x4!
# n = n x (n-1)!
# 0! = 1
# 1! = 1


# def fact(num):
#     if((num==1) or (num==0)):
#         return 1
#     else:
#         return num * fact(num-1)

# a = fact(5)
# print(a)




# try - except
# try: 
#     a = int(input("enter a number = "))
#     b = int(input("enter a number = ")) 
#     print(a+b)
# except:
#     print("letters and special charecters not allowed")



# ************* file operation *************

# file = open("demo.txt","w")
# file.write("hello bhai")
# file.close()

# file = open("demo.txt",'r')
# print(file)
# a = file.readline()
# # a = file.read()
# print(a)
# file.close()


# file = open("demo.txt","a")
# file.write("\ngood afternoon")
# file.close()


# **************ATM*****************
# 1 withdraw
# enter your pin =
#     enter a amount =
#         withdraw done 
#         balance = balance - amount
#     :-no balance available
#     :- wrong pin
# 2 check balance
# enter your pin =

# 3 change pin 
# enter your pin =
# enter a new pin = 
# confirm your new pin = 

# 4 deposit
# enter your account number = 
# how many money you want to deposit = 

# 5 exit 