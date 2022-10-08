# Nested for loop
# syntax
# for variable in list_pf_data:
#     for variable in list_of_data:
#         statements
#     statements

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end="\n")
#     print()
#
# for i in range(5):
#     for j in range(10):
#         print(i*j , end=" \t")
#     print()

# for n in range (1,5):
#     for m in range(5,10):
#         print(n*m, end="\n")
#     print()


# for x in range(1575,2700):
#     if(x%5==0 and x%7==0):
#         print(x)


# for i in range(5):
#     for j in range(3):
#         print("*",end=" " )
#     print(i*j)


# for i in range(5):
#     for j in range(12):
#         print ('* ', end="")
#     print('')
#
# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
    # print('')

# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')
# print("\n

# result_str="";
# for row in range(0,7):
#     for column in range(0,7):
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str);

# result="*"
# for row in range(0,10):
#     for column in range(0,1):
#         if ((column ==2 or row ==5 or row==1) and (column==7 or column==3 or row ==6 or row ==9)):
#             print("*")




# for i in range(1,6):
#     for j in range(i):
#         print("*\t",end="")
#     print()
#
# for i in range(6,0,-1):
#     for j in range(i):
#         print("*\t",end="")
#     print()


#      *
#    *   *
#    *****
#    *   *
#    *   *

# print("  *  ")
# for r in range(4):
#     if (r==1):
#         print("*****")
#     else:
#         print("*   *")

#  ****
# *    *
# *
# *
# *    *
#  ****

# for r in range(6):
#     if ((r==0)or(r==5)):
#         print(" ****")
#     elif ((r==1) or (r==4)):
#         print("*    *")
#     else:
#         print("*")


#  **     *
#  * *    *
#  *  *   *
#  *   *  *
#  *    * *
#  *     **


# for i in range(6):
#     if(i==0):
#         print("**     *")
#     elif(i==1):
#         print("* *    *")
#     elif(i==2):
#         print("*  *   *")
#     elif(i==3):
#         print("*   *  *")
#     elif(i==4):
#         print("*    * *")
#     elif(i==5):
#         print("*     **")




#     ***
#    *   *
#   *
#   *
#   *
#   *    ****
#    *   *  *
#     ***   *

# for i in range(8):
#     if (i==0):
#         print("  ***")
#     elif(i==1):
#         print(" *   *")
#     elif((i==2)or(i==3)or (i==4)):
#         print("*")
#     elif(i==5):
#         print("*    ****")
#     elif(i==6):
#         print(" *   *  *")
#     elif(i==7):
#         print("  ***   *")
