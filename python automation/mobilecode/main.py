from DataCodes import Data
from time import sleep
lll = open('number.txt','w')
for i in range(len(Data)):
    if('MH' in Data[i]):
        for j in range(100000,1000000):
            pp = Data[i][0:4]+str(j)+'\n'
            lll.write(pp)
            print(pp)
            # sleep(0.04)



