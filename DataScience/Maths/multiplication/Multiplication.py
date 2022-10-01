from random import randint
file = open("multiplication/multiSet1.txt","a")

a = randint(10,100)
b = randint(10,100)

file.write(f"{a} x {b} = {a*b}\n")
print(f"{a} x {b}")

file.close()