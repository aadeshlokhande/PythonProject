import pyautogui as pg 
import time

time.sleep(2)
for i in range(5):
    pg.press('r')
    pg.press('u')
    pg.hotkey('shift','r')
    pg.press('u')