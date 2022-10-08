from FinelData import Data,Network,State
mob = input("Enter Mobile number OR first 4 digit of your mobile number = ")
mob = mob[:4]
count = 0
for i in range(len(Data)):
    if(mob in Data[i]):
        pop = Data[i].split('-')
        n = pop[1]
        s = pop[2]
        if(n == "**"):
            n = "Not available"
            print("Network =",n)
            print("state =", State[s])
        else:
            print("Network =", Network[n])
            print("state =", State[s])
        count = 1
if (count==0):
    print("No Data Found...!!!")






#
# ff = open("pop.txt",'w')
# ff.write("[\n")
# for i in range(len(Data)):
#     lol = "'"+Data[i]+"',\n"
#     ff.write(lol)
# ff.write("]")
# ff.close()
#










