#include<string>
#include"EngineType.h"
#include"Engine.h"
#include<exception>
#include<stdexcept>
#include<iostream>
#include<memory>
#include<vector>
#include"functionalities.h"

int main(){

    // 1. Create 3 objects on heap using smart pointers
    std::unique_ptr<Engine> e1 = std::make_unique<Engine>("101",1100, EngineType::DIESEL, 1.3, 120);
    std::unique_ptr<Engine> e2 = std::make_unique<Engine>("102",110, EngineType::PETROL, 1.4, 120);
    std::unique_ptr<Engine> e3 = std::make_unique<Engine>("103",1200, EngineType::HYBRID, 1.2, 120);

    // creating container to store all above values
    std::vector<std::unique_ptr<Engine>> allEngines;
    allEngines.emplace_back(std::move(e1));
    allEngines.emplace_back(std::move(e2));
    allEngines.emplace_back(std::move(e3));

    //  displaying all sensors first
    displayAllEngineInfo(allEngines);

    
    // 3. chekcing if all have engineTorque above 110
    bool isTrue = checkTorquesOfAll(allEngines);
    if (isTrue) std::cout<<"\nAll torques are great..."<<std::endl;
    else std::cout<<"\nSome engines have less torques are great..."<<std::endl;
    
    // 4. Instances with higher engine capacity
    std::cout<<"\ncount of Engines with higher capacity than 1.0 liters: "<<countCapacityGreaterThanThreshold(allEngines,1.1)<<std::endl;

    // 2. Adding all values in container if hp over 1000 and capacity less than 2.0f
    std::vector<std::unique_ptr<Engine>> filterd = getFilterdEngines(allEngines);
    std::cout<<"\nDisplaying all filterd engine info: "<<std::endl;
    displayAllEngineInfo(filterd);

    return 0;
}