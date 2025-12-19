#include"Inventory.h"
#include"Global.h"
#include<iostream>

// searching product from inventory
void search(Inventory arr[], int size, int productCode){
    bool found = false;
    for (size_t i = 0; i < size; i++)
    {
        if(arr[i].getProductCode() == productCode){
            found = true;
            std::cout<<"\nProduct found at index "<<i<<": \nProduct Details: "<<std::endl;
            arr[i].display();
        }
    }
    if(!found){
        std::cout<<"\nGiven Product not found..."<<std::endl;
    }
}
