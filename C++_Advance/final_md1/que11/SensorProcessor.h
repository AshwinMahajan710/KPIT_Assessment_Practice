#ifndef SENSORPROCESSOR_H
#define SENSORPROCESSOR_H

#include<string>
#include"Sensor.h"
#include<iostream>
#include<vector>

class SensorProcessor{
    private:
        std::vector<Sensor> m_sensors;
    public:
        SensorProcessor() = default;
        ~SensorProcessor() = default;

        void addSensor(const Sensor& sensor);
        void processSensor(Sensor& sensor); // Simulates processing by adding random offset
        void displayAll() const;
};

#endif // SENSORPROCESSOR_H
