import pyautogui as pg
from time import sleep

filename = "Palindrome.c"

credit = "// Author : @Tech_In_Seconds\n"

data = """#include<stdio.h>  
int main()    
{    
    int n,r,sum=0,temp;    
    printf("enter the number=");    
    scanf("%d",&n);    
    temp=n;    
    while(n>0)    
    {    
        r=n%10;    
        sum=(sum*10)+r;    
        n=n/10;    
    }    
    if(temp==sum)
    {
        printf("palindrome number \\n");
    }
    else 
    {
        printf("not palindrome\\n");   
    }
    return 0;  
}"""

data = credit + data

data = data.replace("    ","")

sleep(1)
pg.click(400,300)
sleep(1)
pg.moveTo(1100,800)

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

pg.typewrite(f"12321",0.2)
pg.press("Enter")
