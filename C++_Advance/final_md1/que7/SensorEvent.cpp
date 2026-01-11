#include<iostream>
#include<string>
#include"SensorEvent.h"

// constructor --> parameterized
SensorEvent::SensorEvent(int id, std::string type, double value): m_eventId(id), m_type(type), m_value(value) {}

// getters
int SensorEvent::getId() const{
    return m_eventId;
}
std::string SensorEvent::getType() const{
    return m_type;
}
double SensorEvent::getValue() const{
    return m_value;
}

// setter
void SensorEvent::setValue(double value){
    m_value = value;
}

// display function
void SensorEvent::display() const{
    std::cout<<"Id: "<<m_eventId<<"Type: "<<m_type<<"Value: "<<m_value<<std::endl;
}