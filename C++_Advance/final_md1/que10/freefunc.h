#include "Controller.h"
#include "BrakeController.h"
#include "SteeringController.h"
#include <string>
#include<iostream>
#include<vector>
#include<functional>
#include"CommandDispatcher.h"

void printControllerInfo(const Controller& ctrl);
