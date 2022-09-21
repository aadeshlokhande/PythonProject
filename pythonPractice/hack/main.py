import pyautogui as pg 
from time import sleep 

file = open("note.txt","r")
data = file.read().split("\n")
file.close()
a = "____________________________________________________________"
sleep(2)
pg.click(400,500)
sleep(1)
count = 0
for que in data:
    count += 1
    pg.typewrite(f"{count} {que}\n\n",0.06)
    for i in range(5):
        pg.typewrite(a)
        pg.typewrite("\n\n",0.08)