#include<iostream>
#include<string>
#include"ElectricMotor.h"
#include"ElectricVehicle.h"
#include"Global.h"
#include<limits>

int main(){

    // taking user input for size
    int size = 0;
    std::cout<<"Enter the size of array (max 4): "<<std::endl;
    std::cin>>size;

    // creating dynamic array by uses given size
    ElectricVehicle* vehicles = new ElectricVehicle[size];

    // Taking user input for each object 
    for(size_t i=0;i<size;i++){
        std::string vehicleId_ = "", vehicleModel_ = "";
        float batteryCapacity_, maxPower_, maxTorque_;

        std::cout<<"Enter Vehicle Id for vehicle "<<i<<": ";
        getline(std::cin, vehicleId_);

        std::cout<<"Enter Vehicle model for vehicle "<<i<<": ";
        getline(std::cin,vehicleModel_);

        std::cout<<"Enter Vehicle Battery Capacity "<<i<<": ";
        std::cin>> batteryCapacity_;
        
        std::cout<<"Enter Vehicle Battery maxPower "<<i<<": ";
        std::cin>> maxPower_;

        std::cout<<"Enter Vehicle Battery MaxTorque "<<i<<": ";
        std::cin>> maxTorque_;

        vehicles[i] = ElectricVehicle();
    }


    return 0;
}