#include "Controller.h"
#include "BrakeController.h"
#include "SteeringController.h"
#include <string>
#include<iostream>
#include<vector>
#include<functional>
#include"CommandDispatcher.h"
#include"freefunc.h"

int main(){

    // 1. SteeringController obj
    SteeringController str1("Steering",30);
    // 2. Brake obj
    BrakeController str2("Brake",80);
    // 3. Command dispatcher object
    CommandDispatcher obj;
    // 4. adding both controllers
    obj.addController(str1);
    obj.addController(str2);
    // 5. writing lambdas to to execute steering controller and Brake controller
    auto func1 = std::bind(&SteeringController::execute, &str1);
    auto func2 = std::bind(&BrakeController::execute, &str2);
    // adding the commands
    obj.addCommand(func1);
    obj.addCommand(func2);
    // 6. displaying all controllers
    std::cout<<"\nDisplaying all controllers information: "<<std::endl;
    obj.displayControllers();
    // 7. binding the command applypressure
    auto func3 = std::bind(&SteeringController::adjustAngle, &str1, 10);
    auto func4 = std::bind(&BrakeController::applyPressure, &str2, 20);
    // adding the commands
    obj.addCommand(func3);
    obj.addCommand(func4);
    std::cout<<"\nRunning all commands: "<<std::endl;
    obj.runAllCommands();
    // 6. displaying all controllers
    std::cout<<"\nDisplaying all controllers information: "<<std::endl;
    obj.displayControllers();

    return 0;
}