#ifndef CONTROLSYSTEM_H
#define CONTROLSYSTEM_H

#include"Controller.h"
#include<string>
#include<iostream>
#include"BrakeController.h"
#include"SteeringController.h"

class ControlSystem{
    private:
        Controller* m_activeController; // (can be nullptr)
    
    public:
        ControlSystem();
        void setActiveController(Controller* controller); // Accepts nullptr
        void runActiveController() const; // Handles nullptr safely
        ~ControlSystem() = default;
};

#endif // CONTROLSYSTEM_H
