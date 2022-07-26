# list = [
# "Hemant vaishnav",
# "BHAVESH Khanorkar",
# "Aashitosh Gajbhiye",
# "Ashish Kadwe",
# "Abhishek Wadichar",
# "Premraj Sakure",
# "Prajwal wadichar",
# "Chandrabhan uikey ",
# "Pratik kshirsagar",
# "Piyush nimkar",
# "Deepak thakre",
# "Swapnil Shambharkar",
# "Harshal shende"]
# count = 1
# data = ""
# list.sort()
# for i in range(len(list)):
#     data += f"*{list[i].upper()}*\n"
#     for j in range(3):
#         data += f"Question No. *{count}*  :->  \n"
#         count+=1
#     data += "\n"

# data += "*AADESH LOKHANDE*\nQuestion No. *40*  :->"


# file = open("studentlist.txt","w")
# file.write(data)
# file.close()



list = [
"Hemant vaishnav",
"BHAVESH Khanorkar",
"Aashitosh Gajbhiye",
"Ashish Kadwe",
"Abhishek Wadichar",
"Premraj Sakure",
"Prajwal wadichar",
"Chandrabhan uikey ",
"Pratik kshirsagar",
"Piyush nimkar",
"Deepak thakre",
"Swapnil Shambharkar",
"Harshal shende"]
count = 1
data = ""
list.sort()
for i in range(len(list)):
    data += f"*{list[i].upper()}*\n"
    for j in range(3):
        data += f"Question No. *{count}*  :->  \n"
        count+=1
    data += "\n"

data += "*AADESH LOKHANDE*\nQuestion No. *40*  :->"




