#include<string>
#include"Sensor.h"

// constructor --> parameterized
Sensor::Sensor(std::string type): m_type(type){}

// getter
std::string Sensor::getType() const{
    return m_type;
}