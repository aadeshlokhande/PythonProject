import pyautogui as pg 
from time import sleep 

sleep(2)
# print(pg.position())
# exit()


pg.click(pg.locateCenterOnScreen("unfl.png"))
sleep(3)
pg.click(pg.locateCenterOnScreen("red.png"))
