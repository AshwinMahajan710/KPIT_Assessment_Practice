#include"Controller.h"
#include<string>
#include<iostream>
#include"SteeringController.h"

// constructor --> parameterized
SteeringController::SteeringController(const std::string& name, int angle): Controller(name) ,m_angle(angle){}

// execute command --> virtual override
void SteeringController::executeCommand() const {
    std::cout<<"Executing Steering Command: Angle = "<<m_angle<<std::endl;
}

// display status --> virtual override
void SteeringController::displayStatus() const{
    Controller::displayStatus();
    std::cout<<"Angle = "<<m_angle<<std::endl;
} 
