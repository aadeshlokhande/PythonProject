import pyautogui as pg
from time import sleep

filename = "001MonthCalender.py"
credit = "# Author : @Tech_In_Seconds\n"

file = open(filename,"r")
data = file.read()
file.close()

data = credit + data
data = data.split("\n")

sleep(1)
pg.click(400,300)
sleep(3)
pg.moveTo(1100,800)

for line in data:
    for ch in line:
        if(ch=="<"):
            pg.hotkey("ctrl","v")
        elif(ch=="{"):
            pg.typewrite(ch)
            pg.press("del")
        else:
            pg.typewrite(ch)
    pg.typewrite("\n")
    
pg.hotkey("shift","r")
pg.press("r")