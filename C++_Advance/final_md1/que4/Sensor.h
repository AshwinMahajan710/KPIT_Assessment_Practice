#ifndef SENSOR_H
#define SENSOR_H

#include<string>
class Sensor{
    private:
        std::string m_type;
    public:
        Sensor() = default;
        explicit Sensor(std::string type);

        ~Sensor() = default;

        virtual void displayReading() const = 0;

        std::string getType() const;
};

#endif // SENSOR_H
