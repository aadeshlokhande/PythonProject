// // struct union
// #include<stdio.h>
// #include<string.h>
// struct Car
// {
//     int price;
//     float milage;
//     char compony[20];
// } nano;

// int main()
// {
//     nano.price = 120000;
//     nano.milage = 18.6;
//     strcpy(nano.compony,"TATA");
//     printf("price = %d\nmilage = %f\ncompony = %s\n",nano.price,nano.milage,nano.compony);

//     // struct Car audi = {.milage = 9.6, .price = 2342784};
//     // strcpy(audi.compony, "Audi");
//     // printf("price = %d\nmilage = %f\ncompony = %s\n",audi.price,audi.milage,audi.compony);

// }



// ======================================================
// union

// struct union
#include<stdio.h>
#include<string.h>
union Car
{
    int price;
    int milage;
} nano;

int main()
{
    nano.milage = 18;
    nano.price = 120000;
    printf("price = %d\nmilage = %d\n",nano.price,nano.milage);
}










