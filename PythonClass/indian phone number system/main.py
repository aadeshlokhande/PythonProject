from data import state,network 
file = open("info.txt",'r')
num = input("Enter your mobile number = ")[:4]
for i in range(1000):
    data = file.readline()
    if num in data:
        a = data.split("-")  
        net = network[a[1]]
        loc = state[a[2][:2]] 
        print(f"Network\t= {net}\nState\t= {loc}")
file.close()