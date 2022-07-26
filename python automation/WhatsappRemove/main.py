import pyautogui as pg
from time import sleep
from grps import grps,members

for i in range(len(grps)):
    pg.click(215,186) # click to search box
    pg.click(215,186) # click to search box
    sleep(1)
    pg.typewrite(grps[i], 0.1)
    sleep(1)
    pg.press("enter")
    sleep(1)
    pg.click(693,125)#click to grp name
    pg.moveTo(1186,449,1)
    pg.scroll(-100)
    sleep(1)
    pg.click(1142,551)
    sleep(1)
    for i in range(5):
        pg.scroll(-100)

    for i in range(54):   
        pg.scroll(-20) 
        pg.moveTo(1279,581)
        sleep(1)
        pg.click(1335,563)  # arrow
        pg.click(1224,644)   # remove
        sleep(1)
        pg.click(789,478)   # confirm
        sleep(2)