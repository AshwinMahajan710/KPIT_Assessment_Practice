#include<string>
#include"Sensor.h"
#include"PressureSensor.h"
#include"TemperatureSensor.h"
#include<iostream>
#include<vector>
#include<memory>
#include"SensorFleet.h"

// function to add sensor 
void SensorFleet::addSensor(std::unique_ptr<Sensor>& sensor){
    if(sensor != nullptr){
        sensors.emplace_back(std::move(sensor));
    }
    else{
        std::cout<<"provided sensor is nullptr"<<std::endl;
    }
}

// function to display
void SensorFleet::displayAllSensor() const{
    for (auto &sensor : sensors){
        sensor->displayReading();
    }
}