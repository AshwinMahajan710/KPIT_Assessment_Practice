#include"DetectedVehicle.h"
#include<iostream>
#include<stdexcept>

// constructor --> default
DetectedVehicle::DetectedVehicle(): m_id(-1), m_distanceMeters(0.0f), m_relativeSpeedMps(0.0f), m_isBraking(false){}

// constructor --> parameterized
DetectedVehicle::DetectedVehicle(int id, float distanceMeter, float relativeSpeed, bool isBraking){
    
    // validate id
    m_id = (id <0) ? -1 : id;

    // validate distance
    m_distanceMeters = (distanceMeter < 0) ? 0.0f : distanceMeter;

    // assign remaining as it is
    m_isBraking = isBraking;
    m_relativeSpeedMps = relativeSpeed;
}

// getters
int DetectedVehicle::getId() const{
    return m_id;
}
float DetectedVehicle::getDistanceMeters() const{
    return m_distanceMeters;
}
float DetectedVehicle::getRelativeSpeedMps() const{
    return m_relativeSpeedMps;
}
bool DetectedVehicle::getIsBraking() const{
    return m_isBraking;
}

// setters
void DetectedVehicle::setId(int id){
    // validate id
    m_id = (id <0) ? -1 : id;
}

// set distance meter
void DetectedVehicle::setDistanceMeters(float distanceMeter ){
    // validate distance
    m_distanceMeters = (distanceMeter < 0) ? 0.0f : distanceMeter;
}

// relative speed
void DetectedVehicle::setRelativeSpeedMps(float relativeSpeed){
    m_relativeSpeedMps = relativeSpeed;
}

// set is braking
void DetectedVehicle::setIsBraking(bool isBraking){
    m_isBraking = isBraking;
}