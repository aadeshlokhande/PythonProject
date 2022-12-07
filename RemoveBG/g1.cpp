// access specifier
// public private
#include<iostream>
using namespace std;

class Mobile
{
    private:    
        int manCost, software;
        string display;
    public:
        int price, camera, ram;
        void getdata(int m,  int s, int p, int c, int r, string d)
        {
            manCost = m;
            software = s;
            price = p;
            camera = c;
            ram = r;
            display = d;
        }

        void printdata()
        {
            cout<<manCost<<endl;
            cout<<software<<endl;
            cout<<price<<endl;
            cout<<camera<<endl;
            cout<<ram<<endl;
            cout<<display<<endl;
        } 
};

int main()
{
    Mobile oppoF19;
    // oppoF19.price = 15000;
    // cout << oppoF19.price;

    // oppoF19.manCost = 10000;
    // cout<<oppoF19.manCost;

    oppoF19.getdata(8000,3, 15000,64,6,"amoled" );
    oppoF19.printdata();
}


