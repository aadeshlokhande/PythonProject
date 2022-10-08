# file = open("data.txt","r")
# dat = file.read()
# file.close()
# a = dat.split(", ")
# b = f"tk14 : {str(a)}\n"

# file = open("number.txt", "a")
# file.write(b)


import time
from Data import *
import pyautogui as pg
from time import sleep
time = 0.05
msg = "Register guys... fast"

sleep(2)
for name in GrpName:
    pg.click(289,187,interval=1)
    pg.typewrite(name,time)
    pg.press("enter")
    sleep(3)
    pg.click(790,740,interval=1)
    a = GrpNumber[name]
    for number in a:
        pg.typewrite(f"@{number}",time)
        # sleep(1)
        pg.press("enter")
        # pg.hotkey("shift","enter")
    pg.press("enter")
    pg.typewrite(msg,time)
    pg.press("enter")
    sleep(2)



