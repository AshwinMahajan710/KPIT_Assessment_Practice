#include<string>
#include"ElectricMotor.h"
#include<string>
#include"ElectricVehicle.h"
#include<iostream>

// constructor --> default
ElectricVehicle::ElectricVehicle(): m_vehicleId(0), m_vehicleModel("unknown"), m_batteryCapacity(0.0), m_motor(){};

// constructor --> parameterized
ElectricVehicle::ElectricVehicle(const std::string& vehicleId_, const std::string& vehicleModel_, float batteryCapacity_, ElectricMotor motor_): m_vehicleId(vehicleId_), m_vehicleModel(vehicleModel_), m_batteryCapacity(batteryCapacity_), m_motor(motor_){};

// getters
std::string ElectricVehicle::getVehicleId() const{
    return m_vehicleId;
}
std::string ElectricVehicle::getVehicleModel() const{
    return m_vehicleModel;
}
float ElectricVehicle::getBatteryCapacity() const{
    return m_batteryCapacity;
}
ElectricMotor ElectricVehicle::getMotor() const{
    return m_motor;
}

// setters
void ElectricVehicle::setVehicleId(const std::string& vehicleId_){
    m_vehicleId = vehicleId_;
}
void ElectricVehicle::setVehicleModel(const std::string& vehicleModel_){
    m_vehicleModel = vehicleModel_;
}
void ElectricVehicle::setBatteryCapacity(float batteryCapacity_){
    m_batteryCapacity = batteryCapacity_;
}
void ElectricVehicle::setMotor(ElectricMotor motor_){
    m_motor = motor_;
}

// to display
std::ostream& operator<<(std::ostream& out, const ElectricVehicle& other){
    out<<"Vehicle ID: "<<other.m_vehicleId<<std::endl;
    out<<"Vehicle Model: "<<other.m_vehicleModel<<std::endl;
    out<<"Vehicle Battery Capacity: "<<other.m_batteryCapacity<<std::endl;
    out<<"Vehicle Motor: "<<other.m_motor<<std::endl;
    return out;
}

// operator + overload to return sum of 2 battery capacities
float ElectricVehicle::operator + (const ElectricVehicle& other){
    return (this->m_batteryCapacity + other.m_batteryCapacity);
}

