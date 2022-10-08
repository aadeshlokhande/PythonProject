# 1.what is python?
# 2. advantages disadvantages.
# 3.  how to setup python enviornment?
# 4. what is variable and write variable declaration rules ?
# 5. what is string?give example of string slicing
# 6. what is list and how to print list values?
# 7. What is dictonary?
# 8. Write logic operators with example and input output table.
# 9. Write a program to explain nested if else statement
# 10. write a atm program and store balance pin and balance
#
#
# ANSWERS:
# 1) Python is a programming language in which we can code in a single line.
#
# 2)Advantages:
#     In python we can code in single line.
#     python is simple and easy language than other languages.
#
# 3)1.Open google tab .
#   2.Write download pycharm.
#   3.Download the latest version of pycharm.
#   4.After completion of download install it.
#   5.read all the instructions and click on next and save it in your disk
#
# 4) Variables are the container in which we can store data.
# !!!!!RULES!!!!!
# a) We can not start variables with numbers.
#     ex: 1abc, 08h,etc.
# b) we can use underscore(_) in variables.
#     ex: a_b, x_, abc_,etc.
# c) Variables only contains alphabets, numbers and underscore(_).
#     ex: a1_, b_2, xyz, x1, etc.
# d) Variables are case sensitive.
#     ex: name = "shivani"
#         Name = "Shivani"
#         NAME = "SHIVANI"
#
#     print("name")
#     RESULT:
#     shivani
#
# 5) String: collection of characters. we can denote denote string as "".
# There are four types of string.
# a) ' abc'
# b) " abc "
# c) '''abc   '''
# d) """ abc  """
#
# STRING SLICING:
# ex :a= "Computer is an electronic device "
# print(a[5])   # It will print by index
# print(a[:8])  # it will starting point to end given point
# print(a[4:16])# It will print from start given point to end given point.
# print(a[4:]) # It will print from start given point upto end.
# print(a[::-1]) # For reverse
#
# 6) list : list are changeable . we can write or store list in square brackets[].
# list contains strings, numbers.
# PRINT LIST VALUE:
# list = [45,12,85,"shivani",66]
# print(list[3])
# it will print shivani
#
# 7)Dictonary: It contains key value pairs. we can write or store dictonary in curly brackets{}.
#  ex:a={"a":"stone","b":"paper","c":"scissors"}
#
# 8) logic operators: there are three logical operators AND , OR, NOT
# AND :(Ziddi operator)
# a       b           result
# 0       0           0
# 0       1           0
# 1       0           0
# 1       1           1
#
# OR:(Gareeb manacha)
# a       b           result
# 0       0           0
# 0       1           1
# 1       0           1
# 1       1           1
#
# NOT:(ultya khopdicha)
# 0 --> 1
# 1 --> 0
#
# 9) NESTED IF ELSE:
# if(conditions):
#     statements
#     if(conditions):
#         statements
#         if(conditions):
#             statements
#         else:
#             statements
#     else:
#         statements
# else:
#     statements
#
# pass12th =input("are you 12th pass=  ")
# if(pass12th=="yes"):
#     cs = input("do you have computer science sub in 12th=  ")
#     if(cs=="yes"):
#         per = input("your percentage are greater than 60=  ")
#         if(per=="yes"):
#             print("welcome to kamla nehru college")
#         else:
#             print("you are not eligible")
#     else:
#         print("computer science is must")
# else:
#     print("first complete your 12th")
def writepin():
    writepin =open("pin1.txt",'w')
    pin= writepin.write()
writepin()

def readpin(pin):
    readpin = open("pin1.txt",'r')

def writebalance():
    writebalance= open("balance1.txt",'w')
    balance= writebalance.write()
writebalance()

def readbalance(balance):
    readbalance = open("balance1.txt",'r')
    balance











