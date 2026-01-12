#ifndef FULLTIMEEMPLOYEE_H
#define FULLTIMEEMPLOYEE_H

#include<string>
#include"Employee.h"
#include"Grade.h"

class FullTimeEmployee : public Employee{
    public:
        std::string m_projectName;
        std::string m_employeeLocation;
        Grade m_grade;
        int m_bonusPercent;

        FullTimeEmployee() = default;
        FullTimeEmployee(const std::string& name, const std::string& id, float salary, const std::string& projName, const std::string& empLocation, Grade grade, int percent);

        float calculateBonus() const override; 

        void display() const;
        std::string getGradeAsString() const;
};

#endif // FULLTIMEEMPLOYEE_H
