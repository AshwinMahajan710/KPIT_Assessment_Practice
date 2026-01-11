#include"Controller.h"
#include<string>
#include<iostream>
#include"BrakeController.h"
#include"SteeringController.h"
#include"ControlSystem.h"
#include"global.h"

// function to print controller info
void printControllerInfo(const Controller* controller){
    if(controller == nullptr){
        std::cout<<"Controller object not initialized..."<<std::endl;
    }
    else{
        controller->displayStatus();
    }
}