#ifndef ELECTRICMOTOR_H
#define ELECTRICMOTOR_H

#include<iostream>

class ElectricMotor{
    private:
        float m_maxPower;
        float m_maxTorque;

    public:
        
        // constructor
        ElectricMotor();
        ElectricMotor(float maxPower_, float maxTorque_);

        // getters
        float getMaxPower() const;
        float getMaxTorque() const;
        
        // setters
        void setMaxPower(float maxPower_);
        void setMaxTorque(float maxTorque_);

        // overloading << operator
        friend std::ostream& operator <<(std::ostream& out, const ElectricMotor& other);

};

#endif // ELECTRICMOTOR_H
