#include "Controller.h"
#include "BrakeController.h"
#include "SteeringController.h"
#include <string>
#include<iostream>
#include<vector>
#include<functional>
#include"CommandDispatcher.h"

// function to add command
void CommandDispatcher::addCommand(std::function<void()> cmd){
    m_commands.emplace_back(std::move(cmd));
    std::cout<<"Command added successfully...."<<std::endl;
}

// function to add controller
void CommandDispatcher::addController(Controller& ctrl){
    m_controllers.emplace_back(ctrl);
    std::cout<<"Controller added successfully...."<<std::endl;
}

// function to run all commands
void CommandDispatcher::runAllCommands() const{
    for (auto & command: m_commands){
        command();
    }
}

// function to display controller info
void CommandDispatcher::displayControllers() const{
    // Prints names of all controller
    for(auto& controller: m_controllers){
        std::cout<<controller.get().getName()<<std::endl;
    }
}