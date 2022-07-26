import pyautogui as pg
from time import sleep
from palekarmsg import msg

contact = open("palekarContacts.txt",'r')
for i in range(1088):
    a = contact.readline()
    name = a.split(",")[0]

    # x,y = pg.locateCenterOnScreen("search.png")
    sleep(0.50)
    pg.click(180,180)
    sleep(0.50)
    pg.typewrite(name,0.05)
    # x,y = pg.locateCenterOnScreen("contact.png")
    sleep(1)
    pg.press("enter")
    sleep(0.50)
    pg.click(980,743)
    sleep(0.50)
    msg()
    # pg.hotkey("ctrl","a")
    # pg.hotkey('ctrl','x')
    
    print(name)


