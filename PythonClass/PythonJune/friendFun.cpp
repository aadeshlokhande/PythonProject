// // 2 + 3i
// // 3 + 7i
// // ---------
// // 5 + 10i

// #include<iostream>
// using namespace std;

// class Complex
// {
//     int a,b;
//     friend Complex addComplex(Complex o1, Complex o2);
//     public:
//         void getvalue(int n1,int n2)
//         {
//             a = n1;
//             b = n2;
//         }

//         void printvalue()
//         {
//             cout<<a<<" + "<<b<<"i\n";
//         }
// };

// Complex addComplex(Complex o1, Complex o2)
// {
//     Complex o3;
//     o3.getvalue((o1.a+o2.a),(o1.b+o2.b));
//     return o3;
// }

// int main()
// {
//     Complex a1,a2,add;
//     a1.getvalue(2,3);
//     a1.printvalue();

//     a2.getvalue(3,7);
//     a2.printvalue();

//     add = addComplex(a1,a2);
//     add.printvalue();
// }




#include<iostream>
using namespace std;
class abc
{
    int a;
    friend float area(abc ob);
    public:
        void getData(int n1)
        {
            a = n1;
        }
};

float area(abc ob)
{
    float areacircle;
    areacircle = 3.14 * ob.a * ob.a;
    return areacircle;
}


int main()
{
    abc a1;
    float a;
    a1.getData(3);
    a = area(a1);
    cout<<a<<endl;

}
























