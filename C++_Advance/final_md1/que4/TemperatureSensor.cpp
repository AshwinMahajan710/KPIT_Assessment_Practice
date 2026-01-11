#include<string>
#include"Sensor.h"
#include"TemperatureSensor.h"
#include<iostream>

// constructor
TemperatureSensor::TemperatureSensor(std::string type, double temperature): Sensor(type), m_temperature(temperature){}

// display reading function --> pure virtual override
void TemperatureSensor::displayReading() const{
    std::cout<<"Type: "<<getType()<<std::endl;
    std::cout<<"Temperature: "<<m_temperature<<std::endl;
}