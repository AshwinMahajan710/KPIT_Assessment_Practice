#include<string>
#include"EngineType.h"
#include"Engine.h"
#include<exception>
#include<stdexcept>
#include<iostream>
#include<memory>
#include<vector>
#include"functionalities.h"

// function to filter engine
std::vector<std::unique_ptr<Engine>> getFilterdEngines( std::vector<std::unique_ptr<Engine>>& allEngines){
    std::vector<std::unique_ptr<Engine>> filterd_engines;
    for (auto & e: allEngines){
        if(e->m_engineCapacity<2.0 && e->m_horsePower > 1000){
            filterd_engines.emplace_back(std::move(e));
        }
    }
    return filterd_engines;
}

// function to check all torques are above 110
bool checkTorquesOfAll( std::vector<std::unique_ptr<Engine>>& allEngines){
    for (auto & e: allEngines){
        if(e->m_engineTorque < 110.0f){
            return false;
        }
    }
    return true;
}

// function to count the values where engineCapacity is greater
int countCapacityGreaterThanThreshold( std::vector<std::unique_ptr<Engine>>& allEngines, float threshold){
    int count = 0;
    for (auto & e: allEngines){
        if(e->m_engineCapacity > threshold){
            count = count + 1;
            
        }
        std::cout<<"current count: "<<count<<std::endl;
    }
    return count;
}

// function to display all engine info
void displayAllEngineInfo(std::vector<std::unique_ptr<Engine>>& allEngines){
    std::cout<<"Displaying all engines info: "<<std::endl;
    for(auto& e: allEngines){
        e->display();
    }
}

