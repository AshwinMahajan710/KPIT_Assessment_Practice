#include"DetectedVehicle.h"
#include"Global.h"
#include<iostream>

int main(){

    // // TC1:- creating vehicles array
    // DetectedVehicle vehicles[10];
    // vehicles[0] = DetectedVehicle(0,12.5,-2.0,false);
    // vehicles[1] = DetectedVehicle(1,8.0,-1.5,true);
    // vehicles[2] = DetectedVehicle(2,20.0,0.0,false);
    // float maxDistanceForBrakingCount = 10.0;
    // std::cout<<"Closest Distance: "<<computeClosestDistance(vehicles,10)<<std::endl;
    // std::cout<<"Max Distance for braking count: "<<countBrakingVehiclesWithin(vehicles,10, maxDistanceForBrakingCount)<<std::endl;

    // // TC2:- creating vehicles array
    // DetectedVehicle vehicles[10];
    // vehicles[0] = DetectedVehicle(0,0.0,-3.0,true);
    // vehicles[1] = DetectedVehicle(1,-5.0,1.0,true);
    // float maxDistanceForBrakingCount = 1.0;
    // std::cout<<"Closest Distance: "<<computeClosestDistance(vehicles,10)<<std::endl;
    // std::cout<<"Max Distance for braking count: "<<countBrakingVehiclesWithin(vehicles,10, maxDistanceForBrakingCount)<<std::endl;

    // TC2:- creating vehicles array
    DetectedVehicle vehicles[10];
    float maxDistanceForBrakingCount = 1.0;
    std::cout<<"Closest Distance: "<<computeClosestDistance(vehicles,10)<<std::endl;
    std::cout<<"Max Distance for braking count: "<<countBrakingVehiclesWithin(vehicles,10, maxDistanceForBrakingCount)<<std::endl;

    return 0;
}