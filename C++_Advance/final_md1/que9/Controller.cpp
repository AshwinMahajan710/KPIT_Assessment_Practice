#include<string>
#include"Controller.h"

// constructor --> parameterized
explicit Controller::Controller(const std::string& name): m_name(name){}

// getter for name
std::string Controller::getName() const{
    return m_name;
}