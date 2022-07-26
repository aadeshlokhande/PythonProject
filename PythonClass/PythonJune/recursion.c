// recursion

// void abc()
// {
//     printf("Hello ");
//     abc();
// }

// int main()
// {
//     abc();
// }


// #include<stdio.h>
// void abc(int a)
// {
//     if(a>=1)
//     {
//         printf("Hello ");
//         --a;
//         abc(a);
//     }
// }

// int main()
// {
//     abc(5);
// }


// ========================================

// 5! = 5x4x3x2x1
// 4! = 4x3x2x1

// 5! = 5x4!
// n! = n x (n-1)!

// 1! = 1 
// 0! = 1

// #include<stdio.h>
// int fact(int a)
// {
//     if(a==1 || a==0)
//     {
//         return 1;
//     }
//     else
//     {
//         return a * fact(a-1); 
//     }
// }

// int main()
// {
//     int a;
//     printf("Enter a number = ");
//     scanf("%d",&a);
//     printf("Factorial of %d is %d\n",a,fact(a));
// }










