#ifndef STEERINGCONTROLLER_H
#define STEERINGCONTROLLER_H

#include "Controller.h"
#include <string>
#include <iostream>

class SteeringController final : public Controller
{
private:
    int m_angle;

public:
    SteeringController() = default;
    SteeringController(const std::string &name, int angle);

    ~SteeringController() = default;

    void executeCommand() const override;

    void displayStatus() const override;
};
#endif // STEERINGCONTROLLER_H
