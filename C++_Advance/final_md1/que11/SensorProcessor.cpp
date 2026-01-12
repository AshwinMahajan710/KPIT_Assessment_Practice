#include<string>
#include"Sensor.h"
#include<iostream>
#include<vector>
#include"SensorProcessor.h"

// function to add sensor
void SensorProcessor::addSensor(const Sensor& sensor){
    m_sensors.emplace_back(sensor);
    std::cout<<"Sensor added successfully"<<std::endl;
}

// function to process sensor
void SensorProcessor::processSensor(Sensor& sensor){
    std::cout<<"Processing sensor with id: "<<sensor.getId()<<std::endl;
}

// function to display all things
void SensorProcessor::displayAll() const{
    for (auto &sensor: m_sensors){
        sensor.display();
    }
}   

