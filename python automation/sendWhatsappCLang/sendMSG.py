import pyautogui as pg
from time import sleep 
sleep(10)
# # print(pg.position())

file = open("payment.txt","r")
contacts = file.read().split("\n")
file.close()

msgs = """*C Language Course*
Date:- *30 oct 2022*
Your Session is scheduled in the morning 8 O'clock
Link will provided at sharp *7.50* am
Don't Miss the Session of C Programming
"""

msgs = """ C Language Course At Just 999/-
:- YOU HAVE TO COMPLETE YOUR FEES BEFORE 10 NOVEMBER
:- MAKE PAYMENT AND UPLOAD THE SCREENSHOT
:- FEES AMOUNT 999/- ONLY
:- LINK : https://forms.gle/UjTx8gMzAupifL796"""


# msgs = """C Programming Online Class
# *Date* : *30 october 2022*
# *Session* : 02
# *Recorded session* : https://youtu.be/PKnyQ27DA7M
# *Code* : https://tinyl.io/7HKI

# *Note* : Solve all given homework and send me
# *Whatsapp* :- wa.me/917058232826 """

msgs = msgs.split("\n")

# whatsapp
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


# youtube email
# file = open("email.txt", "r")
# emails = file.read().split("\n")
# sleep(2)
# for email in emails:
#     pg.typewrite(email, 0.06)
#     pg.press("enter")