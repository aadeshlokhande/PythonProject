from data import States,Network
file = open("info.txt",'r')
num = input("Enter your mobile no : ")[:4]
for i in range(2000):
    data = file.readline()
    if num in data:
        a = data.split("-")
        Net = Network[a[1]]
        loc = States[a[2][:2]]
        print(f"Network={Net}\nState={loc}")








# f = open("data.py",'r')
# info = open("info.txt",'w')
# for i in range(2000):
#     a = f.readline().replace("\t",'-').replace("    ","-").replace("--",'-@@-')..replace("  ","-@@-@@-")
#     print(a)
#     info.write(a)
# f.close()
# info.close()