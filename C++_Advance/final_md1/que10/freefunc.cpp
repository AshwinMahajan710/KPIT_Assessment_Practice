#include "Controller.h"
#include "BrakeController.h"
#include "SteeringController.h"
#include <string>
#include<iostream>
#include<vector>
#include<functional>
#include"CommandDispatcher.h"
#include"freefunc.h"

void printControllerInfo(const Controller& ctrl){
    std::cout<<"controller name: "<<ctrl.getName()<<std::endl;
}
