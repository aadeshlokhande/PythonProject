# pip install pyautogui

# Pyautogui library 
import pyautogui as pg 
from time import sleep 

# keyboard and mouse control 
# a = pg.position()
# print(a) 

pg.press("win")
sleep(1)
pg.typewrite("chrome",0.09)
pg.press("enter")

sleep(3)
pg.typewrite("web.whatsapp.com",0.08)
pg.press("enter")
sleep(5)
pg.click(423,227)
pg.typewrite("sanket dakhale",0.07)
sleep(1)
pg.press("enter")
sleep(1)
pg.typewrite("Hello sanket...:-) ",0.08)
pg.press("enter")
sleep(1)
pg.hotkey("ctrl","w")




