# import random

# a = [12,43,54,43,2,123,432,1]
# b = random.choice(a)
# print(b)

# print(random.randrange(1, 4))           # random range
# print(random.random())          # random number from 0 to 1


# list = [123,34,345,65,7,854,23,12]
# print(list)
# random.shuffle(list)
# print(list)


# print(random.uniform(1, 4))
import random


b = int(input("enter a no between 1 to 10 = " ))
a = (random.randrange(1,10))
if (b==a):
    print("you win")
elif(b<=a):
    print("your number is smaller")
elif(b>=a):
    print("your number is greater")
elif(b!=a):
    print("you loss")




