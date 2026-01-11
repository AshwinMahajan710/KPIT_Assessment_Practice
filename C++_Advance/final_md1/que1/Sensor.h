#ifndef SENSOR_H
#define SENSOR_H

#include"SensorStatus.h"
#include<string>

class Sensor{
    private:
        SensorStatus m_status;         
        int m_id;
    public:

        // constructors
        Sensor(int id, SensorStatus status);
        Sensor(const Sensor&) = default;
        Sensor(Sensor&&) = delete;

        //assignment operator
        Sensor& operator=(const Sensor&) = delete;
        Sensor operator= (Sensor&&) = delete;

        //destructor
        ~Sensor() = default;

        // getters
        int getId() const;
        SensorStatus getStatus() const;

        //setters
        void setStatus(SensorStatus newStatus);

        // display status string
        const std::string getStatusString() const;
};

#endif // SENSOR_H
