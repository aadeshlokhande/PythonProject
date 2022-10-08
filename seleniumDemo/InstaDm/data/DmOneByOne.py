import pyautogui as pg
from time import sleep
from msgs import msg
from fbid import ids,passwords
sleep(2)

list = []
a = open('phillips.txt', 'r')
for aa in a:
    list.append(aa.replace("\n", ""))
count = 1

rotation = len(ids)+1

for idr in range(rotation):
    if(rotation == idr ):
        pass 
    else:
        for i in range(20):
            pg.click(234, 201)          # search
            pg.typewrite(list[count],0.1)
            sleep(2)
            try:
                a,b = pg.locateCenterOnScreen('moreOnInstagram.png')        #aadesh
                pg.click(a,b+30)
                sleep(1)
                pg.click(895,745,interval=1)
                sleep(1)
                msg()
                sleep(2)
            except:
                try:
                    a,b = pg.locateCenterOnScreen('moreOnInstagra.png') #others
                    pg.click(a,b+30)
                    sleep(1)
                    pg.click(895,745,interval=1)
                    sleep(1)
                    msg()
                    sleep(2)
                except:
                    try:
                        a,b = pg.locateCenterOnScreen('instagramAc.png')
                        pg.click(a,b+30)
                        sleep(1)
                        pg.click(895,745,interval=1)
                        sleep(1)
                        msg()
                        sleep(2)
                    except:
                        pg.click(234,201,interval=1)
                        pg.hotkey("ctrl","a")
                        pg.hotkey("ctrl","x")
            print(count,list[count])
            count = count + 1

        pg.click(230,140)
        sleep(2)
        pg.click(293,651)

        sleep(10)
        pg.click(633,460)
        pg.hotkey('ctrl','a')
        sleep(1)
        pg.hotkey('ctrl','x')
        sleep(1)
        pg.typewrite(ids[idr],0.06)
        pg.click(200,200)
        sleep(1)

        pg.click(633,517)
        pg.hotkey('ctrl','a')
        sleep(1)
        pg.hotkey('ctrl','x')
        sleep(1)
        pg.typewrite(passwords[idr],0.06)
        pg.click(200,200)
        sleep(1)
        pg.click(670,585)
        sleep(15)




