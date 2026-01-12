#include"Controller.h"
#include<string>
#include<iostream>
#include"SteeringController.h"

// constructor --> parameterized
SteeringController::SteeringController(const std::string& name, int angle): Controller(name) ,m_angle(angle){}

// execute command --> virtual override
void SteeringController::execute() const {
    std::cout<<"Executing Steering Command: Angle = "<<m_angle<<std::endl;
}
