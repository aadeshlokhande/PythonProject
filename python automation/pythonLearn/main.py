import requests
from bs4 import BeautifulSoup
from programiz import topics

a = 1
listTopics = []

for i in topics:
    print(f"{a} : {i}".title())
    a = a + 1
    listTopics.append(i)

Utopic = input("\n\nEnter a topic you want to learn in Python = ").lower()

if Utopic.isdecimal():
    Utopic = listTopics[int(Utopic)-1]

for i in topics:
    if Utopic in i:
        r = requests.get(topics[i])
        soup = BeautifulSoup(r.content, 'html.parser')
        for data in soup.find():
            
            info = data.text

            SP = info.find("Related Topics")

            EndPoint = "Table of Contents"
            EP = info.find(EndPoint)
            
            ep = 0
            if EP>0:
                ep = EP
            
            sp = 0
            if SP > 0:
                sp = SP
            print(info[sp:ep].replace("\n\n","\n"))
        print(f"\n**********************END {i.title()}**********************\n")