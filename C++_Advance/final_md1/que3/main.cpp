#include"Controller.h"
#include<string>
#include<iostream>
#include"BrakeController.h"
#include"SteeringController.h"
#include"ControlSystem.h"
#include"global.h"

int main(){

    // create obj of steering controller
    SteeringController controller1("Steering",30);
    BrakeController controller2("Brake",80);

    //creating controlsystem obj
    ControlSystem obj;

    //set to steeringcontroller
    obj.setActiveController(&controller1);
    obj.runActiveController();
    
    //set to BRAKEcontroller
    obj.setActiveController(&controller2);
    obj.runActiveController();

    //set to BRAKEcontroller
    obj.setActiveController(nullptr);
    obj.runActiveController();

    printControllerInfo(&controller1);
    printControllerInfo(&controller2);

    return 0;
}