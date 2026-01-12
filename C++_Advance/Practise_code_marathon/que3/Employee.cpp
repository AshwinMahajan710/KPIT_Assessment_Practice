#include<string>
#include"Employee.h"
#include<iostream>

// constructor --> parameterized
Employee::Employee(const std::string& name, const std::string& id, float salary): m_id(id), m_name(name), m_salary(salary){}

// display function
void Employee::displayDetails() const{
    std::cout<<"\nEmp Name: "<<m_name<<std::endl;
    std::cout<<"Emp ID: "<<m_id<<std::endl;
    std::cout<<"Emp Salary: "<<m_salary<<std::endl;
}