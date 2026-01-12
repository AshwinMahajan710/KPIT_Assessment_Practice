#ifndef SENSOR_H
#define SENSOR_H

#include<string>

class Sensor{
    private:
        int m_id;
        std::string m_type;
        double m_value;
    
    public:
        Sensor(int id, std::string type, double value);
        Sensor(const Sensor&) = default;
        Sensor(Sensor&&) = default;

        // assignment
        Sensor& operator = (const Sensor& ) = default;
        Sensor& operator = (Sensor&&) = default;

        ~Sensor() = default;

        // getters
        int getId() const;
        std::string getType() const;
        double getValue() const;

        // setter for value
        void setValue(double newValue);

        // display function
        void display() const; // Prints: Sensor[ID=…, Type=…, Value=…]
};

#endif // SENSOR_H
