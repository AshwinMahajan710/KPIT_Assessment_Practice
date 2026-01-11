#include"Sensor.h"
#include"SensorStatus.h"
#include"SensorCluster.h"
#include<vector>
#include<string>
#include<iostream>

void printSensorInfo(const Sensor& sensor){
        std::cout<<"Sensor Id: "<<sensor.getId()<<std::endl;
        std::cout<<"Sensor status: "<<sensor.getStatusString()<<std::endl;
}