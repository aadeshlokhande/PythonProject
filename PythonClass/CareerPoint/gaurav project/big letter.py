import random
b = int(input("enter your number = "))
a = random.randrange(1,10)
if (a == b):
    print("you win")
else:
    print(input("enter your number = "))
    if(a != b):
        print(input("enter your number = "))
    else:
        print("you win")




