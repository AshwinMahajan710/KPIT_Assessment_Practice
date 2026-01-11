#include"Controller.h"
#include<string>
#include<iostream>
#include"BrakeController.h"

// constructor --> parameterized
BrakeController::BrakeController(const std::string& name, int pressure): Controller(name) ,m_pressure(pressure){}

// execute command --> virtual override
void BrakeController::executeCommand() const {
    std::cout<<"Executing Brake Command: Pressure = "<<m_pressure<<std::endl;
}

// display status --> virtual override
void BrakeController::displayStatus() const{
    Controller::displayStatus();
    std::cout<<"Pressure = "<<m_pressure<<std::endl;
} 