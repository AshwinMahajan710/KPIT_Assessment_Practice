#include"Sensor.h"
#include"SensorStatus.h"
#include"SensorCluster.h"
#include<vector>
#include<string>
#include<iostream>

int main(){

    // creating 3 objects
    Sensor obj1(101,SensorStatus::ACTIVE);
    Sensor obj2(102,SensorStatus::INACTIVE);
    Sensor obj3(103,SensorStatus::FAULTY);

    // create cluster obj
    SensorCluster cl1("ECU Sensor");

    // add objs in cl1
    cl1.addSensor(&obj1);
    cl1.addSensor(&obj2);
    cl1.addSensor(&obj3);

    // display all info
    cl1.displayClusterInfo();

    return 0;
}