#ifndef ELECTRICVEHICLE_H
#define ELECTRICVEHICLE_H

#include<string>
#include"ElectricMotor.h"
#include<string>
class ElectricVehicle{
    private:
        std::string m_vehicleId;
        std::string m_vehicleModel;
        float m_batteryCapacity;
        ElectricMotor m_motor;

    public:

    // constructors
    ElectricVehicle();
    ElectricVehicle(const std::string& vehicleId_, const std::string& vehicleModel_, float batteryCapacity_, ElectricMotor motor_);

    // getters
    std::string getVehicleId() const;
    std::string getVehicleModel() const;
    float getBatteryCapacity() const;
    ElectricMotor getMotor() const;
    
    // setters
    void setVehicleId(const std::string& vehicleId_);
    void setVehicleModel(const std::string& vehicleModel_);
    void setBatteryCapacity(float batteryCapacity_);
    void setMotor(ElectricMotor motor_);

    friend std::ostream& operator<<(std::ostream& out, const ElectricVehicle& other);
    
};

#endif // ELECTRICVEHICLE_H
