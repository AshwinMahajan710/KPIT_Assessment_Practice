#include"Inventory.h"
#include"Global.h"
#include<iostream>
#include<string>
#include<stdexcept>

int main(){

    // TC 1 --> Creating an instance
    Inventory inv1("Food",20,1);

    // TC2 --> adding 10 units
    inv1.purchase(10);

    // TC3 --> selling 5 units
    inv1.sale(5);

    // TC4 --> selling with insufficient stock
    try{
        inv1.sale(30);
    }catch(const std::exception & e){
        std::cout<<e.what()<<std::endl;
    }

    // TC5 --> Creating an inventory
    Inventory arr[3] = {Inventory("Shampoo",20,12),
    Inventory("Food",20,1),
    Inventory("Soap",20,3)};

    // TC6 --> Searching valid code
    search(arr,3,12);
    
    // TC7 --> Searching invalid code
    search(arr,3,123);

    return 0;
}