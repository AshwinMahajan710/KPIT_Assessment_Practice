#include"Battery.h"
#include<string>
#include<iostream>
#include"Global.h"

// function to search battery with respective manufacturer
void searchBatteriesByManufacturer(Battery* batteries, int count,const std::string& manufacturer){
    bool found = false;
    for (size_t i = 0; i < count; i++)
    {
        if(batteries[i].getManufacturer() == manufacturer){
            found = true;
            std::cout<<"\nBattery with respective manufacturer found at index "<<i<<": \nBattery Details: \n"<<batteries[i]<<std::endl;
        }
    }
    if(!found){
        std::cout<<"\nBatery with given manufacturer not found..."<<std::endl;
    }
}

// function to display all batteries
void displayAllBatteries(Battery* batteries, int count){
    if (count==0){
        std::cout<<"No Batteries are there to display.."<<std::endl;
    }else{
        for(int i=0;i<count;i++){
            std::cout<<"\nBattery "<<i+1<<": \n"<<batteries[i];
        }
    }
}