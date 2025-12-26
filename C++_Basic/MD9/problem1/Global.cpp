#include"DetectedVehicle.h"
#include"Global.h"
#include<limits>
#include <cstddef>

// return smallest possible distance among entries with id >=0 . if no vehicle found return -1.0f
float computeClosestDistance(const DetectedVehicle arr[], int count){
    float minDist = std::numeric_limits<float>::max();
    for (size_t i = 0; i < count; i++)
    {
        if(arr[i].getId()>=0  && arr[i].getDistanceMeters()< minDist){
            minDist = arr[i].getDistanceMeters();
        }
    }
    if(count == 0){return -1.0f;}
    return minDist;
}

// return how many vehicles have getIsBraking() == true and getDistanceMeters()<=maxDistance and id>=0
int countBrakingVehiclesWithin(const DetectedVehicle arr[], int count, float maxDistance){
    int vehicleCount = 0;
    for (size_t i = 0; i < count; i++)
    {
        if(arr[i].getId()>=0  && arr[i].getDistanceMeters()<= maxDistance && arr[i].getIsBraking()==true){
            vehicleCount ++;
        }
    }
    return vehicleCount;
}