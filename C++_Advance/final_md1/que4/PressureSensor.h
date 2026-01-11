#ifndef PRESSURESENSOR_H
#define PRESSURESENSOR_H

#include<string>
#include"Sensor.h"

class PressureSensor: public Sensor{
        private:
        double m_pressure;
    
    public:
        PressureSensor(std::string type, double pressure);
        ~PressureSensor() = default;
        void displayReading() const override;
};

#endif // PRESSURESENSOR_H
