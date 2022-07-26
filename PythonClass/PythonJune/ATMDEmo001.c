#include<stdio.h>
int main()
{
    int pin , bal=12000 ,a,b, c, d, e, f;
    printf("press 1:withdraw \npress 2:check balance \npress 3:change pin \npress 4:deposit");
    printf("\nEnter a number=");
    scanf("%d",&a);
    switch(a)
    {
        case 1:
            printf("\nEnter a pin=");
            scanf("%d",&pin);
            if(pin==1234)
            {
                printf("\nEnter a amount=");
                scanf("%d",&a);
                if(a<=12000)
                {
                    printf("\ntransaction done");
                    b= bal-a;
                    printf("\ncurrent balance=%d",b);
                }
                else
                {
                    printf("\ninsufficient balance");
                }
            }
            else
            {
                printf("\nwrong pin");
            }
            break;
            
        case 2:
            printf("\nEnter a pin =");
            scanf("%d",&pin);
            if(pin==1234)
            {
                printf("\ncurrent balance=%d",bal);
            }
            else
            {
                printf("\nwrong pin ");
            }
            break;
         
        case 3:
            printf("\nEnter a old pin=");
            scanf("%d",&pin);
            if(pin==1234)
            {
                printf("\nEnter a new pin =");
                scanf("%d",&c);
                printf("\nConfirm your pin=");
                scanf("%d",&d);
                if(c==d)
                {
                    printf("\npin changed");
                }
                else 
                {
                    printf("\npin doesn't match");
                } 
            }
            else
            {
                printf("\nWrong pin ");
            }
            break;
        
        case 4:
            printf("\nEnter a pin =");
            scanf("%d",&pin);
            if(pin==1234)
            {
                printf("\nEnter a amount=");
                scanf("%d",&e);
                f=bal+e;
                printf("\ncurrent balance=%d",f);
            }
            else 
            {
                printf("\nwrong pin");
            }
            break;
     
     }   
     printf("\nthank you"); 
    
    return 0;
}