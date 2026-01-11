#ifndef TEMPERATURE_H
#define TEMPERATURE_H

#include<string>
#include"Sensor.h"

class TemperatureSensor: public Sensor{
    private:
        double m_temperature;
    
    public:
        TemperatureSensor(std::string type, double temperature);
        ~TemperatureSensor() = default;
        void displayReading() const override;
};

#endif // TEMPERATURE_H
