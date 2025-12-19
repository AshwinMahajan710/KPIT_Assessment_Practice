#include"Battery.h"
#include<string>
#include<iostream>

// constructor --> default
Battery::Battery(): m_batteryId(0), m_batteryType("Unknown"), m_capacity(100), m_manufacturer("Not Known"), m_voltage(100){}

// constructor --> parameterized
Battery::Battery(int batteryId, const std::string &batteryType, const std::string &manufacturer, double capacity, double voltage): m_batteryId(batteryId), m_batteryType(batteryType), m_capacity(capacity), m_manufacturer(manufacturer), m_voltage(voltage){}

// getters
int Battery::getBatteryId() const{
    return m_batteryId;
}
std::string Battery::getBatteryType() const{
    return m_batteryType;
}
std::string Battery::getManufacturer() const{
    return m_manufacturer;
}
double Battery::getCapacity() const{
    return m_capacity;
}
double Battery::getVoltage() const{
    return m_voltage;
}

// setters
void Battery::setBatteryId(int id){
    m_batteryId = id;
}
void Battery::setBatteryType(const std::string& type){
    m_batteryType = type;
}
void Battery::setManufacturer(const std::string& manufacturer){
    m_manufacturer = manufacturer;
}
void Battery::setCapacity(double capacity){
    m_capacity = capacity;
}
void Battery::setVoltage(double voltage){
    m_voltage = voltage;
}

// friend function to display details
std::ostream& operator <<(std::ostream& out, const Battery& other){
    out<<"Battery Id: "<<other.m_batteryId<<std::endl;
    out<<"Battery Type: "<<other.m_batteryType<<std::endl;
    out<<"Battery Manufacturer: "<<other.m_manufacturer<<std::endl;
    out<<"Battery Capacity: "<<other.m_capacity<<std::endl;
    out<<"Battery Voltage: "<<other.m_voltage<<std::endl;
    return out;
}
