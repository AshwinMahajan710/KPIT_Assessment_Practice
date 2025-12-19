#include<iostream>
#include"ElectricMotor.h"

// constructor --> default
ElectricMotor::ElectricMotor(): m_maxPower(0), m_maxTorque(0){};

// constructor --> parameterized
ElectricMotor::ElectricMotor(float maxPower_, float maxTorque_): m_maxPower(maxPower_), m_maxTorque(maxTorque_){}

// getters
float ElectricMotor::getMaxPower() const{
    return m_maxPower;
}
float ElectricMotor::getMaxTorque() const{
    return m_maxTorque;
}

// setters
void ElectricMotor::setMaxPower(float maxPower_){
    m_maxPower = maxPower_;
}
void ElectricMotor::setMaxTorque(float maxTorque_){
    m_maxTorque = maxTorque_;
}

// overloading << operator
std::ostream& operator <<(std::ostream& out, const ElectricMotor& other){
    out<<"Max Power: "<<other.m_maxPower<<std::endl;
    out<<"Max Torque: "<<other.m_maxTorque<<std::endl;
    return out;
}
