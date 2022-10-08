# recursion

# def functionName():
#     staetments;
#     functionName()
#
# functionName()


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input("Enter a number = "))
print("The factorial of", num, "is", factorial(num))




# 6! = 6x5x4x3x2x1
# 6! = 6x5!
# 7! = 7x6x5x4x3x2x1
# 7! = 7x6!
# 1! = 1
# 0! = 1


