#ifndef BRAKECONTROLLER_H
#define BRAKECONTROLLER_H

#include"Controller.h"
#include<string>
#include<iostream>

class BrakeController final: public Controller{
    private:
        int m_pressure;
    public:
        BrakeController() = default;
        BrakeController(const std::string& name, int pressure);

        ~BrakeController() = default;

        void executeCommand() const override;

        void displayStatus() const override;
};


#endif // BRAKECONTROLLER_H
