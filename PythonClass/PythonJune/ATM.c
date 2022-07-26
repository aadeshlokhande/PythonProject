// ATM

#include<stdio.h>
int readPin()
{
    int a;
    FILE *file;
    file = fopen("pin.txt","r");
    fscanf(file,"%d",&a);
    fclose(file);
    return a;
}


int readBal()
{
    int a;
    FILE *file;
    file = fopen("bal.txt","r");
    fscanf(file,"%d",&a);
    fclose(file);
    return a;
}
void writePin(int a)
{
    FILE *file;
    file = fopen("pin.txt","w");
    fprintf(file,"%d",a);
    fclose(file);
}

void writeBal(int a)
{
    FILE *file;
    file = fopen("bal.txt","w");
    fprintf(file,"%d",a);
    fclose(file);
}


int main()
{
    int choice, pin, upin, npin,cpin, amount,balance;
    printf("Press 1 : Withdraw\n");
    printf("Press 2 : Check balance\n");
    printf("Press 3 : Change pin\n");
    printf("Press 4 : deposit\n");
    printf("Enter your choice = ");
    scanf("%d",&choice);

    switch(choice)
    {
        case 1:
            printf("Enter a pin = ");
            scanf("%d",&upin);
            pin = readPin();
            if(pin==upin)
            {
                printf("Enter a amount = ");
                scanf("%d",&amount);
                balance = readBal();
                if(balance>=amount)
                {
                    balance = balance - amount;
                    printf("Transaction successfull\ncurrent bal = %d",balance);
                    writeBal(balance);
                }
                else
                {
                    printf("Insufficient balance");
                }
            }
            else
            {
                printf("Wrong pin");
            }
            break;

        case 2:
            printf("Enter a pin = ");
            scanf("%d",&upin);
            pin = readPin();
            if(pin==upin)
            {
                balance = readBal();
                printf("Current balance = %d",balance);
            }
            else
            {
                printf("Wrong pin");
            }
            break;
        
        case 3:
            printf("Enter a pin = ");
            scanf("%d",&upin);
            pin = readPin();
            if(pin==upin)
            {
                printf("Enter a new pin = ");
                scanf("%d",&npin);
                printf("confirm your pin = ");
                scanf("%d",&cpin);
                if(cpin==npin)
                {
                    printf("Pin changed!!!");
                    writePin(npin);
                }
                else
                {
                    printf("pin doesn't match");
                }
            }
            else
            {
                printf("Wrong pin");
            }
            break;
        case 4:
            printf("Enter a pin = ");
            scanf("%d",&upin);
            pin = readPin();
            if(pin==upin)
            {
                printf("Enter a amount = ");
                scanf("%d",&amount);
                balance = readBal();
                balance = balance + amount;
                writeBal(balance);
            }
            else
            {
                printf("Wrong pin");
            }
            break;

    }
    printf("\nThanks for using our service");
}
