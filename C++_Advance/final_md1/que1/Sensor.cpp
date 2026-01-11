#include"SensorStatus.h"
#include"Sensor.h"

// constructor --> parameterized
Sensor::Sensor(int id, SensorStatus status): m_id(id), m_status(status){};

// getters
int Sensor::getId() const{
    return m_id; 
}

SensorStatus Sensor::getStatus() const{
    return m_status;
}

//setters
void Sensor::setStatus(SensorStatus newStatus){
    m_status = newStatus;
}

// getting status string
const std::string Sensor::getStatusString() const{
    if(m_status == SensorStatus::ACTIVE){
        return "Active";
    } 
    else if(m_status == SensorStatus::INACTIVE){
        return "InActive";
    } 
    else return "Faulty";
}