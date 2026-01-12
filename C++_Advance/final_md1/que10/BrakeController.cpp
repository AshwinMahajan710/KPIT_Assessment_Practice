#include"Controller.h"
#include<string>
#include<iostream>
#include"BrakeController.h"

// constructor --> parameterized
BrakeController::BrakeController(const std::string& name, int pressure): Controller(name) ,m_pressure(pressure){}

// execute command --> virtual override
void BrakeController::execute() const {
    std::cout<<"Executing Brake Command: Pressure = "<<m_pressure<<std::endl;
}

// function to update pressure
void BrakeController::applyPressure(int extraPressure){
    m_pressure = m_pressure + extraPressure;
    std::cout<<"Pressure updated to "<<m_pressure<<std::endl;
}