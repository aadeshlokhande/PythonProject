# recursion 
# def functionName():
#     statements
#     functionName()

# functionName()

# 5! = 5x4x3x2x1
# 4! = 4x3x2x1
# 5! = 5 x 4!
# num! =num x (num-1)!
# 1! = 1 
# 0! = 1

# REcursion 
# def fact(num):
#     if(num==1)or(num==0):
#         return 1
#     else:
#         return num * fact(num-1)

# a = fact(int(input("Enter a number = ")))
# print(a)


# itration 
a = int(input("Number dere = "))
b = 1 
for i in range(1,a+1):
    b = b * i 
print(b)
