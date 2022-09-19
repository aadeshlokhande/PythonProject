import pyautogui as pg
from time import sleep

filename = "NoteSorting.c"

credit = "// Author : @Tech_In_Seconds\n"

data = """#include <stdio.h>
int main() 
{
    int amt, total;
    printf("Input the amount: ");
    scanf("%d",&amt);
    total = (int)amt/100;
    printf("There are: \\n");
    printf("%d Note(s) of 100.00\\n", total);
    amt = amt-(total*100);
    total = (int)amt/50;
    printf("%d Note(s) of 50.00\\n", total);
    amt = amt-(total*50);
    total = (int)amt/20;
    printf("%d Note(s) of 20.00\\n", total);
    amt = amt-(total*20);
    total = (int)amt/10;
    printf("%d Note(s) of 10.00\\n", total);
    amt = amt-(total*10);
    total = (int)amt/5;
    printf("%d Coin(s) of 5.00\\n", total);
    amt = amt-(total*5);
    total = (int)amt/2;
    printf("%d Coin(s) of 2.00\\n", total);
    amt = amt-(total*2);
    total = (int)amt/1;
    printf("%d Coin(s) of 1.00\\n", total);
    return 0;
}
"""

data = credit + data

data = data.replace("    ","")

sleep(1)
pg.click(400,300)
sleep(1)

for i in data:
    if(i=="<"):
        pg.hotkey("ctrl","v")
    elif(i=="{"):
        pg.typewrite(i)
        pg.press("del")
    else:
        pg.typewrite(i)

sleep(2)


pg.hotkey("alt","t")
sleep(2)
pg.typewrite(f"gcc {filename} && ./a.out",0.05)
pg.press("Enter")