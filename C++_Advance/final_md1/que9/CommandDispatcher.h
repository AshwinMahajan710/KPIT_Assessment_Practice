#ifndef COMMANDDISPATCHER_H
#define COMMANDDISPATCHER_H

#include "Controller.h"
#include "BrakeController.h"
#include "SteeringController.h"
#include <string>
#include<iostream>
#include<vector>
#include<functional>

// class command dispatcher
class CommandDispatcher{
    private:
        std::vector<std::function<void()>> m_commands;
        std::vector<std::reference_wrapper<Controller>> m_controllers;
    
    public:
        CommandDispatcher() = default;
        ~CommandDispatcher() = default;

        void addCommand(std::function<void()> cmd);
        void addController(Controller& ctrl);
        void runAllCommands() const; // Invokes all stored commands
        void displayControllers() const; // Prints names of all controllers
};

#endif // COMMANDDISPATCHER_H
