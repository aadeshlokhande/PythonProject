from random import randint
import os 
file = open("multiplication/multiSet1.txt","a")

a = randint(11,99)
b = randint(11,99)

os.system("clear")

file.write(f"{a} x {b} = {a*b}\n")
print(f"\n{a} x {b}\n")

file.close()