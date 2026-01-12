#include<string>
#include"Sensor.h"
#include<iostream>

// constructor --> parameterized constructor
Sensor::Sensor(int id, std::string type, double value):m_id(id),m_type(type),m_value(value){}

// getters
int Sensor::getId() const{
    return m_id;
}

std::string Sensor::getType() const{
    return m_type;
}

double Sensor::getValue() const{
    return m_value;
}

// setter for value
void Sensor::setValue(double newValue){
    m_value = newValue;
    std::cout<<"Value changed to "<<m_value<<" Successfully..."<<std::endl;
}

// display function
void Sensor::display() const{
    std::cout<<"Sensor Info -> Id: "<<m_id<<" Type: "<<m_type<<" Value: "<<m_value<<std::endl;
} 
