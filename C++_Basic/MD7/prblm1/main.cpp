#include<string>
#include"Vehicle.h"
#include<iostream>

double Vehicle::s_averageFuelPrice = 70.0;

int main(){

    Vehicle v1("V123","Gasoline",25.0);
    v1.TrackFuelConsumption(250,10);
    std::cout<<"Fuel Economy: "<<v1.calculateFuelEconomy()<<std::endl;
    v1.updateAvergaeFuelPrice(2.75);
    std::cout<<"Calculate Total Fuel Price: "<<v1.calculateTotalFuelCost(200)<<std::endl;
    return 0;
}