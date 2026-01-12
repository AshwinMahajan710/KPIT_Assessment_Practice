#include<string>
#include"Employee.h"
#include"Grade.h"
#include"FullTimeEmployee.h"
#include<stdexcept>
#include<iostream>

// constructor --> parameterized
FullTimeEmployee::FullTimeEmployee(const std::string& name, const std::string& id, float salary, const std::string& projName, const std::string& empLocation, Grade grade, int percent): Employee(name,id, salary){

    // validation 
    if(percent<0 || percent>100){
        throw std::out_of_range("Percentage value provided is out of range.....");
    }

    // assignment
    m_projectName = projName;
    m_employeeLocation = empLocation;
    m_grade = grade;
    m_bonusPercent = percent;
    
    std::cout<<"Object created successfully....."<<std::endl;
}

// function to calculate bonus
float FullTimeEmployee::calculateBonus() const{
    switch (m_grade)
    {
        case Grade::A:{
            return m_bonusPercent * m_salary;
        }
        case Grade::B:{
            return m_bonusPercent * (m_salary/2.0);
        }
        default: {
            return m_bonusPercent * (m_salary/4.0);
        }
    }
} 

// function to get the grade name as str
std::string FullTimeEmployee:: getGradeAsString() const{
    switch (m_grade){
        case Grade::A:
            return "A";
        case Grade::B:
            return "B";
        default:
            return "C";
    }
}

void FullTimeEmployee::display() const{
    Employee::displayDetails();
    std::cout<<"ProjectName: "<<m_projectName<<std::endl;
    std::cout<<"Employee Location: "<<m_employeeLocation<<std::endl;
    std::cout<<"Grade: "<<getGradeAsString()<<std::endl;
    std::cout<<"Bonus Percent: "<<m_bonusPercent<<std::endl;
}