#include"HeapSensor.h"

// necessary initializations
float HeapSensor::MIN_VOLTAGE = 0.0f;
float HeapSensor::MAX_VOLTAGE = 5.0f;
float HeapSensor::MIN_TEMPERATURE = -40.0f;
float HeapSensor::MAX_TEMPERATURE = 125.0f;

// constructor --> default
HeapSensor::HeapSensor(): m_id(-1), m_voltageV(0.0f), m_temperatureC(25.0f), m_active(false){};

// constructor --> parameterized 
// increment total instances
HeapSensor::HeapSensor(int id, float voltageV, float temperatureC, bool active): m_id(id), m_voltageV(voltageV), m_temperatureC(temperatureC), m_active(active){
    s_totalInstances++;
} 

// decrement total instances
HeapSensor::~HeapSensor(){
    s_totalInstances --;
} 

// Getters
int HeapSensor::getId() const{
    return m_id;
};
float HeapSensor::getVoltageV() const{
    return m_voltageV;
};
float HeapSensor::getTemperatureC() const{
    return m_temperatureC;
};
bool HeapSensor::getActive() const{
    return m_active;
};
int HeapSensor::getTotalInstances(){
    return s_totalInstances;
}

// setters

// to set id
void HeapSensor::setId(int id){
    m_id = id;
}

// to set voltage: clamp to max voltage and min voltage
void HeapSensor::setVoltageV(float voltage){
   m_voltageV = (voltage > MAX_VOLTAGE ? MAX_VOLTAGE : (voltage < MIN_VOLTAGE ? MIN_VOLTAGE: voltage)); 
} 

// to set temperature: max temperature and min temperature
void HeapSensor::setTemperatureC(float temperature){
    m_temperatureC = (temperature > MAX_TEMPERATURE ? MAX_TEMPERATURE : (temperature < MIN_TEMPERATURE ? MIN_TEMPERATURE: temperature));
} 

// set active
void HeapSensor::setActive(bool active){
    m_active = active;
}    

// overloaded member functions
void HeapSensor::calibrate(float tempOffset){
    setTemperatureC(getTemperatureC() + tempOffset); 
}
void HeapSensor::calibrate(float tempScale, float tempOffset){
    setTemperatureC((getTemperatureC()*tempScale) + tempOffset);
}
