import pyautogui as pg
while True:
    a = pg.confirm("are you ok","hello",("yes","no"))
    if(a == "yes"):
        break

# a = pg.getInfo()
# for i in a:
#     print(i)
