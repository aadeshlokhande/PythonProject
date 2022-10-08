from AllData import listData

file = open('number91.txt','w')
file.write("Name,Phone")
for i in range(len(listData)):
    name = listData[i][0]
    num = '+91'+listData[i][1] 
    dd = f"{name},{num}\n"
    file.write(dd)

file.close()