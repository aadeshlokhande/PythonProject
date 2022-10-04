file = open("squares1000.py","w")
file.write('num = int(input("enter a number = "))\n')
file.write('if(num==1):\n')
file.write('\tprint(1)\n')

for i in range(2,1001):
    file.write(f'elif(num=={i}):\n')
    file.write(f'\tprint({i*i})\n')

file.write('else:\n')
file.write('\tprint("Invalid Number")\n')
file.close()