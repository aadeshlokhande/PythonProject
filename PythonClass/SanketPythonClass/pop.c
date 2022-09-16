#include<stdio.h>
int main()
{ 
      for(int i=1;i<=5;i++)
      {
            for(int j=5;j>=i;j--)
            {
                  if(i!=j || j<i)
                  {
                        printf(" * ");
                  }
                  else
                  {
                        printf(" ");
                  }
            }
            printf("\n");
      }
      return 0;
}