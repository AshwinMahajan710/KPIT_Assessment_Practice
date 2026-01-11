#include"Datalog.h"
#include<vector>
#include<cstddef>
#include<iostream>
#include<memory>
#include"SharedLogger.h"

void SharedLogger::addLog(std::shared_ptr<Datalog> log){
    if(log==nullptr){
        std::cout<<"It is nullptr... cannot add log"<<std::endl;
    }else{
        m_logs.emplace_back(log);
        std::cout<<"Successfully added...."<<std::endl;
    }
};

void SharedLogger::displayAll() const{
    for (auto& i: m_logs){
        i->display();
    }
}