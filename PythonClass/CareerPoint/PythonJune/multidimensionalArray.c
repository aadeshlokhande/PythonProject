#include<stdio.h>

int fact(int num)
{
    if(num==1 || num==0)
    {
        return 1;
    }
    else 
    {
        return num * fact(num-1);
    }
}

int main()
{
    printf("%d\n",fact(5));
}