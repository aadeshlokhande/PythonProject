import pyautogui as pg
from time import sleep 
# sleep(4)
# print(pg.position())

file = open("student.txt","r")
contacts = file.read().split("\n")
file.close()

msgs = """*C Language Course*
Date:- *30 oct 2022*
Your Session is scheduled in the morning 8 O'clock
Link will provided at sharp *7.50* am
Don't Miss the Session of C Programming
"""
msgs = msgs.split("\n")


for contact in contacts:
    # contact = contact.split(",")
    sleep(1)
    pg.click(264,118)
    sleep(1)
    pg.typewrite(contact,0.08)
    sleep(5)
    pg.click(222,192)
    sleep(1)
    for msg in msgs:
        pg.typewrite(msg,0.05)
        pg.hotkey("shift","enter")
    pg.press("enter")