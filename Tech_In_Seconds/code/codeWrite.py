import pyautogui as pg
from time import sleep

filename = "addition.c"

credit = "// Author : @Tech_In_Seconds\n"

data = """#include <stdio.h>
int main()
{
    int num1,num2,ans;
    printf("Enter a first number = ");
    scanf("%d",&num1);
    printf("Enter a first number = ");
    scanf("%d",&num2);
    ans = num1 + num2;
    printf("%d + %d = %d\\n",num1,num2,ans);
    return 0;
}
"""

data = credit + data

data = data.replace("    ","")

sleep(1)
pg.click(400,300)
sleep(1)
pg.moveTo(800,800)

for i in data:
    if(i=="<"):
        pg.hotkey("ctrl","v")
    elif(i=="{"):
        pg.typewrite(i)
        pg.press("del")
    else:
        pg.typewrite(i)

sleep(1)


pg.hotkey("alt","t")
sleep(2)
pg.typewrite(f"gcc {filename} && ./a.out",0.08)
pg.press("Enter")
sleep(1)

pg.typewrite(f"10",0.2)
pg.press("Enter")

pg.typewrite(f"20",0.2)
pg.press("Enter")