import pyautogui as pg
from msg import typemsg
from AllData import listData
from time import sleep

file = open("remain.txt",'w')

for i in range(len(listData)):
    pg.click(279,187)
    pg.hotkey("ctrl","a")
    pg.press('del')
    pg.typewrite(str(listData[i][0]),0.01)
    sleep(1)
    try:
        o,p = pg.locateCenterOnScreen('contact.png')
        pg.click(o,p+60)
        sleep(1)
        pg.click(1158,733)
        typemsg(listData[i])
    except:
        file.write(str(listData[i]))
        file.write('\n')
    print(i)
file.close()
