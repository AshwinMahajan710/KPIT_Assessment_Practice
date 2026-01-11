#include<string>
#include"Sensor.h"
#include"PressureSensor.h"
#include<iostream>

// constructor
PressureSensor::PressureSensor(std::string type, double pressure): Sensor(type), m_pressure(pressure){}

// display reading function --> pure virtual override
void PressureSensor::displayReading() const{
    std::cout<<"Type: "<<getType()<<std::endl;
    std::cout<<"Pressure: "<<m_pressure<<std::endl;
}