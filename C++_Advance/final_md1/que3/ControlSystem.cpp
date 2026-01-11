#include"Controller.h"
#include<string>
#include<iostream>
#include"BrakeController.h"
#include"SteeringController.h"
#include"ControlSystem.h"

// constructor --> default
ControlSystem::ControlSystem(): m_activeController(nullptr) {}

// function to set controller
void ControlSystem::setActiveController(Controller* controller){
    m_activeController = controller;
} 

// running active controller
void ControlSystem::runActiveController() const{
    if(m_activeController == nullptr){
        std::cout<<"No controller is initialized..."<<std::endl;
    }else{
        m_activeController->executeCommand();
    }
} 