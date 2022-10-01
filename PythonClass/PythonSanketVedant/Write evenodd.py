file = open("evenOdd100.py","w")
file.write('num = int(input("enter a number = "))\n')
file.write('if(num==1):\n')
file.write('\tprint("Odd number")\n')
for i in range(2,1001):
    if(i%2==0):
        file.write(f'elif(num=={i}):\n')
        file.write('\tprint("Even number")\n')
    else:
        file.write(f'elif(num=={i}):\n')
        file.write('\tprint("Odd number")\n')
file.write('else:\n')
file.write('\tprint("Invalid Number")\n')
file.close()


