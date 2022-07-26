# recursion 
# def funnctionName():
#     statemets 
#     functionName()
# functionName() 

# 5! = 5x4x3x2x1
# 4! = 4x3x2x1

# 5! = 5 x 4!
# formula: num! = num x (num-1)!
# 1! = 1
# 0! = 1


# def factorial(num):
#     if((num==1) or (num==0)):
#         return 1
#     else:
#         return num + factorial(num-1)

# print(factorial(10))

# def abc():
#     print("hello",end=" ")
#     abc()

# abc()



# Program to print the fibonacci series upto n_terms

# # Recursive function
# def recursive_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

# n_terms = 10

# # check if the number of terms is valid
# if n_terms <= 0:
#     print("Invalid input ! Please input a positive value")
# else:
#     print("Fibonacci series:")
# for i in range(n_terms):
# 	print(recursive_fibonacci(i))

# # 0 1 1 2 3 5 8 13