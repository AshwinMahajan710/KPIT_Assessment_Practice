#include<string>
#include"EngineType.h"
#include"Engine.h"
#include<exception>
#include<stdexcept>
#include<iostream>
#include<memory>
#include<vector>

// function to filter engine
std::vector<std::unique_ptr<Engine>> getFilterdEngines( std::vector<std::unique_ptr<Engine>>& allEngines);

// function to check all torques are above 110
bool checkTorquesOfAll( std::vector<std::unique_ptr<Engine>>& allEngines);

// function to count the values where engineCapacity is greater
int countCapacityGreaterThanThreshold( std::vector<std::unique_ptr<Engine>>& allEngines, float threshold);

// function to display all engines
void displayAllEngineInfo(std::vector<std::unique_ptr<Engine>>& allEngines);