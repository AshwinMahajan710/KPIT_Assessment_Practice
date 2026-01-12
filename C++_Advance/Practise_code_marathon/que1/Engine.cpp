#include<string>
#include"EngineType.h"
#include"Engine.h"
#include<exception>
#include<stdexcept>
#include<iostream>

// constructor --> default
// Engine::Engine():m_engineId("0"), m_horsePower(0), m_engineType(EngineType::HYBRID), m_engineCapacity(0), m_engineTorque(20){}

// constructor --> parameterized
Engine::Engine(const std::string& id, int hp, EngineType type, float capacity, float torque){

    // validation
    if(hp<0){
        throw std::invalid_argument("Horsepower can never be less than 0...");           
    }
    if(torque < 20 || torque > 150){
        throw std::out_of_range("Torque value enterd is out of range...");
    }

    // assigning
    m_engineId = id;
    m_engineCapacity = capacity;
    m_engineType = type;
    m_horsePower = hp;
    m_engineTorque = torque;
    std::cout<<"Object created successfully..."<<std::endl;
}

// display function
void Engine::display(){
    std::cout<<"\nEngine Id: "<<m_engineId<<std::endl;
    std::cout<<"Engine HorsePower: "<<m_horsePower<<std::endl;
    std::cout<<"Engine Type: "<<getTypeName()<<std::endl;
    std::cout<<"Engine Capacity: "<<m_engineCapacity<<std::endl;
    std::cout<<"Engine Torque: "<<m_engineTorque<<std::endl;
}

// function to get engine Type
std::string Engine::getTypeName() const{
    switch (m_engineType)
    {
    case EngineType::DIESEL:
        return "Diesel";
        break;
    
    case EngineType::PETROL:
        return "Petrol";
        break;

    default:
        return "Hybrid";
        break;
    }
}