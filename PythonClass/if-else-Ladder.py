# if-else-ladder
# syntax
# if(condition):
#     statements
# elif(condition):
#     statements
# elif(condition):
#     statements
#     .
#     . 
#     . 
# else:
#     statements


# example 1:
# marks = int(input("Enter your marks = "))
# if((marks>=0) and (marks<35)):
#     print("your are fail")
# elif((marks>=35) and (marks<50)):
#     print("C Grade")
# elif((marks>=50) and (marks<75)):
#     print("B Grade")
# elif((marks>=75) and (marks<90)):
#     print("A Grade")
# elif((marks>=90) and (marks<=100)):
#     print("A+ Grade")
# else:
#     print("Invalid Input")


# exmple 2:
# a =int(input("Enter a number = "))
# if(a==1):
#     print("one")
# elif(a==2):
#     print("TWO")
# elif(a==3):
#     print("Three")
# else:
#     print("Invalid input")



# ========================================================

# homework
# calender,

# a=float(input("Enter the first number = "))
# b=float(input("Enter the second number = "))
# remainder=a%b
# if remainder==0:
#     print(a,"is divisible by number",b)
# else:
#     print(a, "is not divisible by number",b)


# num=int(input("Enter a day = "))
# day = num % 7
# if(day==1):
#      print("friday")
# elif(day==2):
#      print("saturday")
# elif(day==3):
#      print("sunday")
# elif(day==4):
#      print("monday")
# elif(day==5):
#      print("tuesday")
# elif(day==6):
#      print("wednesday")
# elif(day==0):
#     print("thusday")
# else:
#     print("Invalid input")



# num = int(input("Enter a number = "))

# if(num%2==0):
#     print("divisible by 2")
#     if(num%3==0):
#         print("divisibe by 3")
#     else:
#         print("not divisible by 3")
# else:
#     print("not divisible by 2")