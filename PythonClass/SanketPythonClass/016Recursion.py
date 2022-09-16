# Recursion 
# def abc():
#     print("Hello ")
#     abc()

# abc()

# ------------------
# def abc(a):
#     if(a>0):
#         a-=1
#         print("Hello ")
#         abc(a)

# abc(5)
# --------------------

# 5! = 5x4x3x2x1 
# 4! = 4x3x2x1 
# 5! = 5 X 4! 

# n! = n x (n-1)! 
# 1! = 1 
# 0! = 1 

# def fact(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#         return num * fact(num-1)

# ans = fact(785)
# print(ans)