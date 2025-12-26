#ifndef GLOBAL_H
#define GLOBAL_H

#include"DetectedVehicle.h"

// return smallest possible distance among entries with id >=0 . if no vehicle found return -1.0f
float computeClosestDistance(const DetectedVehicle arr[], int count);

// return how many vehicles have getIsBraking() == true and getDistanceMeters()<=maxDistance and id>=0
int countBrakingVehiclesWithin(const DetectedVehicle arr[], int count, float maxDistance);

#endif // GLOBAL_H
