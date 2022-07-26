
//2

#include <stdio.h>
int main()
{
    int date ;
    printf(" Enter the date =");
    scanf("%d",&date);
    date = date % 7;
    if(date==1)
    {
        printf(" Sunday ");
    }
    
    else if(date==2)
    {
        printf(" Monday " );
        
    }
    
    else if(date==3)
    {
        printf( " Tuesday");
    }
     
    else if (date==4)
    {
        printf(" Wednesday");
        
    }
    else if (date==5)
    {
        printf(" Thursday");
        
    }
    else if(date==6)
    {
        printf( " Friday ");
    }
    else if (date==0)
    {
        printf(" Saturday ");
    }
    else
    {
        printf(" INVALID DATE ");
    }
    
}