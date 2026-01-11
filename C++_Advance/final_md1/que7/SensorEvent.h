#ifndef SENSOREVENT_H
#define SENSOREVENT_H

#include<string>

class SensorEvent{
    private:
        int m_eventId;
        std::string m_type; // (e.g., "Temperature", "Pressure")
        double m_value;
    
    public:

        // constructors
        SensorEvent() = default;
        SensorEvent(int id, std::string type, double value);
        SensorEvent(const SensorEvent&) = default;
        SensorEvent(SensorEvent&&) = default;
        
        // assignment
        SensorEvent& operator = (const SensorEvent&) = default;
        SensorEvent& operator = (SensorEvent&&) = default;

        // destructor
        ~SensorEvent() = default;

        // setter for value
        void setValue(double value);
        
        // member funcs
        int getId() const;
        std::string getType() const;
        double getValue() const;
        void display() const; // Prints: Event[ID=…, Type=…, Value=…]
};

#endif // SENSOREVENT_H
