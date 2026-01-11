#include"Datalog.h"
#include<vector>
#include<cstddef>
#include<iostream>
#include"Logger.h"

// function to add log
void Logger::addLog(Datalog log){ // Should use move semantics when adding
    m_logs.emplace_back(std::move(log));
    std::cout<<"Log added successfully..."<<std::endl;
}

// function to display all things
void Logger::displayAll() const{
    for(auto &i : m_logs){
        i.display();
    }
} 