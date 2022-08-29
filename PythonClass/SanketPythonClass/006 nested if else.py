# nested if else

# if(condition):
#     statements
#     if(condition):
#         statements
#     else:
#         statements
# else:
#     statements
#     if(condition):
#         statements
#     else:
#         statements


# age = int(input("Enter your age = "))

# if(age>0 and age<75):
#     if(age>18):
#         print("you can drive")
#     else:
#         print("you can't drive")
# else:
#     print("invalid age")



# engineer addmission form 

# income = 75000+
# neet = 80+
# 12th = 65+

# income = int(input("enter your income = "))
# if(income>75000):
#     neet = int(input("Neet marks = "))
#     if(neet>80):
#         marks12th = int(input("enter your 12th marks = "))
#         if(marks12th>65):
#             print("you are able to engineering")
#         else:
#             print("you are not able to engineering")
#     else:
#         print("try next year")
# else:
#     print("bhag ja bhikmange")



# income = int(input("enter your income = "))
# if(income>75000):
#     neet = int(input("Neet marks = "))
#     if(neet>80):
#         marks12th = int(input("enter your 12th marks = "))
#         if(marks12th>65):
#             print("you are able to engineering")
#         else:
#             print("you are not able to engineering")
#     else:
#         a = input("do you want to try next year = ")
#         if(a=="yes"):
#             print("All the best")
#         else:
#             print("try in another college")
# else:
#     print("bhag ja bhikmange")

# ************************************

num = int(input("Enter a number = "))

if(num%2==0):
    print("Its divisible by 2")
    if(num%3==0):
        print("Its divisible by 3")
    else:
        print("its not divisible by 3")
else:
    print("its not divisible by 2")