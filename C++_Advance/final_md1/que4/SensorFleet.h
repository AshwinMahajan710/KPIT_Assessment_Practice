#ifndef SENSORFLEET_H
#define SENSORFLEET_H

#include<string>
#include"Sensor.h"
#include"PressureSensor.h"
#include"TemperatureSensor.h"
#include<iostream>
#include<vector>
#include<memory>

class SensorFleet{
    private:
        std::vector<std::unique_ptr<Sensor>> sensors;
    public:
        SensorFleet() = default;
        ~SensorFleet()  = default;

        void addSensor(std::unique_ptr<Sensor>& sensor);
        void displayAllSensor() const;
};

#endif // SENSORFLEET_H
