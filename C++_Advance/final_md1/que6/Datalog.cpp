#include"Datalog.h"
#include<vector>
#include<cstddef>
#include<iostream>

// constructor --> parameterized
Datalog::Datalog(int id, std::vector<int> rawdata): m_logId(id), m_rawData(rawdata){}

// constructor --> move
Datalog::Datalog(Datalog&& other) noexcept : m_logId(other.m_logId), m_rawData(std::move(other.m_rawData)){}

// assignment --> move
Datalog& Datalog::operator = (Datalog&& other){
    m_logId = other.m_logId;
    m_rawData = std::move(other.m_rawData);
    return *this;
}

// member funcs
int Datalog::getId() const{
    return m_logId;
}

size_t Datalog::getDataSize() const{
    return m_rawData.size();
}

// display funct
void Datalog::display() const{
    std::cout<<"Data log Id: "<<m_logId<<std::endl;
    std::cout<<"Rawdata: ";
    for (auto i : m_rawData){
        std::cout<<i<<" ";
    }
    std::cout<<std::endl;
}