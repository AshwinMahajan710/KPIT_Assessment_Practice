#include<string>
#include"Vehicle.h"
#include<iostream>

// constructor --> Parameterized
Vehicle::Vehicle(): Vehicle("1","Petrol",0.0){};

// constructor --> parameterized
Vehicle::Vehicle(const std::string& vehicleID_, const std::string& fuelType_, double fuelEfficiency_): m_vehicleID(vehicleID_), m_fuelType(fuelType_), m_fuelEfficiency(fuelEfficiency_){}

// For updating values 
void Vehicle::TrackFuelConsumption(double fuelConsumed_, double distanceTravelled_){
    m_totaFuelConsumed = fuelConsumed_;
    m_totalDistanceTravelled = distanceTravelled_;
    m_fuelEfficiency = m_totalDistanceTravelled/m_totaFuelConsumed;
}

// calculate fuel economy
double Vehicle::calculateFuelEconomy(){
    m_fuelEfficiency = m_totalDistanceTravelled/m_totaFuelConsumed;
    return m_fuelEfficiency * s_averageFuelPrice;
}

// 
void Vehicle::displayVehicleInfo() const{
    std::cout<<"Vehicle ID: "<<m_vehicleID<<std::endl;
    std::cout<<"Vehicle FuelType: "<<m_fuelType<<std::endl;
    std::cout<<"Vehicle Fuel consumed: "<<m_totaFuelConsumed<<std::endl;
    std::cout<<"Total distance travel: "<<m_totalDistanceTravelled<<std::endl;
    std::cout<<"Vehicle fuel efficiency: "<<m_fuelEfficiency<<std::endl;
}

// function to update average 
void Vehicle::updateAvergaeFuelPrice(double averageFuelPrice){
    s_averageFuelPrice = averageFuelPrice + (averageFuelPrice*0.10);
}

// calculate total fuelcost
double Vehicle::calculateTotalFuelCost(double distanceToTravel) const{
    return (m_totalDistanceTravelled/m_fuelEfficiency)*s_averageFuelPrice;
}