#include"Sensor.h"
#include"SensorStatus.h"
#include"SensorCluster.h"
#include<vector>
#include<string>
#include<iostream>

//constructor --> default
SensorCluster::SensorCluster(const std::string& clusterName){
    m_clusterName = clusterName;
}

// function to add clusters
void SensorCluster::addSensor(Sensor* sensor){
    if(sensor!=nullptr){
        sensors.push_back(sensor);
        std::cout<<"Object added successfully.."<<std::endl;
    }
    else{
        std::cout<<"as it is null we cannot add object"<<std::endl;
    }
}

// display info
void SensorCluster::displayClusterInfo() const{
    std::cout<<"\nCluster Name: "<<m_clusterName<<std::endl;
    for(auto i: sensors){
        std::cout<<"Sensor Id: "<<i->getId()<<std::endl;
        std::cout<<"Sensor status: "<<i->getStatusString()<<std::endl;
    }
}