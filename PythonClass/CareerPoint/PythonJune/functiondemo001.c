#include<stdio.h>
float div(float a,float b)
{
    float c;
    c = a/b;
    return c;
}

int main()
{
    int a = 10,b=20;
    float ans;
    ans = div(a,b);
    printf("Div = %.2f\n",ans);

}