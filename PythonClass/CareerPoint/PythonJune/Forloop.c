// loop
// for loop  

// for(init; cond; inc/dec)
// {
//     statements
// }


#include<stdio.h>
int main()
{
    for(int a = 1; a<=10; a++)
    {
        printf("%d\n",a);
    }
    return 0;
}


// #include<stdio.h>
// int main()
// {
//     for(int a = 10; a>=1; a--)
//     {
//         printf("%d\n",a);
//     }
//     return 0;
// }

// #include<stdio.h>
// int main()
// {
//     int num;
//     printf("Enter a number = ");
//     scanf("%d",&num);
//     for(int a = 1; a<=10; a++)
//     {
//         printf("%d x %d = %d\n",num,a,a*num);
//     }
//     return 0;
// }

// print all even numbers from 1 to 100
// print number of odd numbers from 1 to 100
// #include <stdio.h>
// int main()
// { 
//     int odd = 0;
//     for(int a = 1; a<=100;a++)
//     { 
//         if(a%2==1)
//         {
//             ++odd;
//         }
//     }
//     printf("odd = %d\n",odd);
// }
// get a number and print total sum from 1 to that number
// #include <stdio.h>
// int main()
// { 
//    int num,sum = 0;
//    printf("Enter a number = ");
//    scanf("%d",&num);
//    for(int a = 1; a<=num; a++)
//    {
//        sum = sum + a;
//    }
//    printf("sum = %d\n",sum);
// }


// #include<stdio.h>
// int main()
// {
//     int a[10],sum=0;
//     float avg;
//     for(int i=0; i<10;i++)
//     {
//         printf("Enter a number=");
//         scanf("%d",&a[i]);
//     }
//     for(int i=9;i>=0;i--)
//     {
//         printf("a[%d]=%d\n",i,a[i]);
//     }
//     for(int v=0;v<10;v++)
//     {
//         sum=sum+a[v];
//     }
//     printf("sum is %d\n",sum );
//     avg=sum/10.0;
//     printf("avg is %f",avg);
// }




