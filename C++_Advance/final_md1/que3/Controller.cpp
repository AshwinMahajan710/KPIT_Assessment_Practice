#include"Controller.h"
#include<string>
#include<iostream>

// constructor --> parameterized
Controller::Controller(const std::string& name):m_name(name){}

// display function
void Controller::displayStatus() const{
    std::cout<<"Name: "<<m_name<<std::endl;    
}