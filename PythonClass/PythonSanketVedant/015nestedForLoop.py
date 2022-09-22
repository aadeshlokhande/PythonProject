# Nested For Loop 
# for variable in CollectionOfData:
#     statements
#     for variable in CollectionOfData:
#         statements
#     statements

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j,end="\t")
#     print()


# for i in (1,2,3,4,5):
#     for j in (1,2,3,4,5):
#         print(j,end="\t")
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# 1 1 1
# 0 0 0
# 0 0 0 


# 11 12 13 
# 21 22 23
# 31 32 33


# for i in range(1,4):
#     for j in range(1,4):
#         if(i==1):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# 1 0 0 
# 1 0 0 
# 1 0 0 

# 1 0 0 
# 0 1 0 
# 0 0 1

# 11 12 13 
# 21 22 23
# 31 32 33

# for i in range(1,4):
#     for j in range(1,4):
#         if(i==j):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# 1 0 0 
# 1 1 0 
# 1 1 1 

# 11 12 13 
# 21 22 23
# 31 32 33

# for i in range(1,4):
#     for j in range(1,4):
#         if(i>=j):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# 1 1 1 
# 0 1 1 
# 0 0 1 

# for i in range(1,4):
#     for j in range(1,4):
#         if(i<=j):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# 1 0 1 
# 0 1 0 
# 1 0 1

# 1 1 1 1 1 
# 1 0 0 0 1 
# 1 0 0 0 1 
# 1 0 0 0 1
# 1 1 1 1 1

# for i in range(1,6):
#     for j in range(1,6):
#         if(i==1 or i==5 or j==1 or j==5):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# 1 1 1 1 1 
# 1 1 0 1 1 
# 1 0 1 0 1 
# 1 1 0 1 1
# 1 1 1 1 1

# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55

# for i in range(1,6):
#     for j in range(1,6):
#         if(i==1 or i==5 or j==1 or j==5 or i==j or i+j==6):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# 1 - 100 counting print 
# 1 2 3 ....10
# 11 12 13...20
# 21 22 23...30
# .
# .
# .
# 91 92 93.....100


# 1 - 10 tables 

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# * 
# * * 
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()



# * * * * *
# * * * *
# * * *
# * *
# * 


#         *
#       * *
#     * * *
#   * * * * 
# * * * * *

# for i in range(1,6):
#     for j in range(1,6):
#         if(i+j>=6):
#             print("*",end=" ")
#         else:
#             print(" " ,end=" ")
#     print()


#      * 
#     * *
#    * * *
#   * * * * 
#  * * * * * 

# for i in range(1,6):
#     for j in range(1,6):
#         if(i+j>=6):
#             print("*",end=" ")
#         else:
#             print(" " ,end="")
#     print()