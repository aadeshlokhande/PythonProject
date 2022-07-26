import random
for i in range(3):
    cnum = random.randrange(1,11)

    unum = int(input("Guess the number = "))
    if(unum>cnum):
        print("your number is greater")
    elif(unum<cnum):
        print("your number is smaller")
    else:
        print(f"you win in {i+1} chance")
        exit()
print("you loss")