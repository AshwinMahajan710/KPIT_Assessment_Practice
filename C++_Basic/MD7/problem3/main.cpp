#include"Battery.h"
#include<string>
#include<iostream>
#include"Global.h"

int main(){

    // creating array of batteries
    Battery* batteries = new Battery[3]{Battery(1,"Type 1","Manufacturer 1",1000.0,12.0),
                                        Battery(2,"Type 2","Manufacturer 2",2000.0,24.0),
                                        Battery(3,"Type 3","Manufacturer 1",3000.0,36.0)};
    
    // TC2 --> displaying all available battery objects
    std::cout<<"Displaying all batteries: "<<std::endl;
    displayAllBatteries(batteries,3);

    // TC3 --> Searching batteries by manufacturer 1
    std::cout<<"Batteries by \"Manufacturer 1\": "<<std::endl;
    searchBatteriesByManufacturer(batteries,3,"Manufacturer 1");

    // TC3 --> Searching batteries by manufacturer 9
    std::cout<<"Batteries by \"Manufacturer 9\": "<<std::endl;
    searchBatteriesByManufacturer(batteries,3,"Manufacturer 9");

    return 0;
}