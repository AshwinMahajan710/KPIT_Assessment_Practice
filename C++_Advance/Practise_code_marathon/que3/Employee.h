#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include<string>

class Employee{
    public:
        std::string m_name;
        std::string m_id;
        float m_salary;

        Employee() = default;
        Employee(const std::string& name, const std::string& id, float salary);

        virtual float calculateBonus() const = 0; 

        void displayDetails() const;
};

#endif // EMPLOYEE_H
