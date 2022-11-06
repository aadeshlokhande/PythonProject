import pyautogui as pg 
from time import sleep 
import os
sleep(3)

msg = """ SELECT department_id, avg(salary)
from sessionwithsumit.employees_data
where job_id not in ('AD_PRES', 'AD_VP')
GROUP by department_id
order by avg(salary) desc; """

msg = msg.split("\n")

for i in msg:
    pg.typewrite(i)
    pg.hotkey("shift","enter")

# pg.press("enter")