import pyautogui as pg
from time import sleep

filename = "Fibonacci.c"

credit = "// Author : @Tech_In_Seconds\n"

data = """#include<stdio.h>    
int main()    
{    
    int n1=0,n2=1,n3,i,number;    
    printf("Enter the number of elements:");    
    scanf("%d",&number);    
    printf("\\n%d %d ",n1,n2);
    for(i=2;i<number;i++)
    {    
        n3=n1+n2;    
        printf("%d ",n3);    
        n1=n2;    
        n2=n3;    
    }  
    printf("\\n");
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
