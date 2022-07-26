# a = int(input("enter a 1st number "))
# b = int(input("enter a 2nd number "))
# if(a<b):
#    print("larger number is", b)
# else:
#    print("larger number is", a)


# a = int(input("enter a 1st number = "))
# b = int(input("enter a 2nd number = "))
# c = int(input("enter a 3rd number = "))

# if(a>b):
#     if(a>c):
#         print("Largest =",a)
#     else:
#         print("Largest =",c)
# else:
#     if(b>c):
#         print("Largest =",b)
#     else:
#         print("Largest =",c)


# 1)
# 1 = sunday
# 2 = monday
# .
# .
# 7 = saturday


# 2)
# marks < 35 = fail
# marks > 35 and marks < 50 = C grade
# marks > 50 and marks < 74 = b grade
# marks > 75 and marks < 90 = a grade
# marks > 90 and marks < 100 = a+ grade




# number = int(input("Enter a number = "))
# num = number%7
# if (num==1):
#     print("Sunday")
# elif(num==2):
#     print("monday")
# elif (num == 3):
#     print("Tuesday")
# elif(num==4):
#     print("Wednesday")
# elif(num==5):
#     print("thursday")
# elif(num==6):
#     print("friday")
# else:
#     print("saturday")

# String
# Collection of Characters
# str1  = "what is your name "
# str2 = """what is your name"""
# str3 = 'what is your name'
# str4 = '''what is your name''

# Slicing
# str1 = "my name is chaitra i study in class 9th"
# print(str1[4:15])
# print(str1[4])
# print(str1[::1])
# print(str1[-4:])
# print(str1[4:25])
# print(str1[0:])

# functions
# str = "Which Is Your Favorite Colour "
# print(str.upper())
# print(str.lower())
# print(str.replace("o","v"))
# print(str.split(" "))
# print(str.capitalize())
# print(len(str))


import random
a = int(input("guess a number between 1 to 10 = "))
b = print(random.randrange(1,10))
if(a==b):
     print("you win")
else:
     print("you entered a smaller number")
c = int(input("guess a number between 1 to 10 = "))
print(random.randrange(1,10))
if(a==b):
     print("you entered a samller  number ")
else:
     print("you entered a greater number ")
