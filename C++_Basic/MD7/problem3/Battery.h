#ifndef BATTERY_H
#define BATTERY_H

#include<string>
#include<iostream>

class Battery{
    private:
        int m_batteryId;
        std::string m_batteryType;
        std::string m_manufacturer;
        double m_capacity;
        double m_voltage;
    
    public:

    // constructor --> default
    Battery();

    // constructor --> parameterized
    Battery(int batteryId, const std::string &batteryType, const std::string &manufacturer, double capacity, double voltage);

    // getters
    int getBatteryId() const;
    std::string getBatteryType() const;
    std::string getManufacturer() const;
    double getCapacity() const;
    double getVoltage() const;

    // setters
    void setBatteryId(int id);
    void setBatteryType(const std::string& type);
    void setManufacturer(const std::string& manufacturer);
    void setCapacity(double capacity);
    void setVoltage(double voltage);

    // friend function to display details
    friend  std::ostream& operator <<(std::ostream& out, const Battery& other);

};

#endif // BATTERY_H
