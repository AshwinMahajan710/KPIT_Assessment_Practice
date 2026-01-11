#include"Datalog.h"
#include<vector>
#include<cstddef>
#include<iostream>
#include<memory>
#include"SharedLogger.h"
#include"freefunc.h"

int main(){
    
    // std::vector<int> with 1,000 integers and use it to construct a DataLog object with ID 101.
    std::vector<int> datalogs(1000,5);
    Datalog log(201,std::move(datalogs));
    
    // displaying all logs in logger
    log.display();

    // printing the size of original datalog
    std::cout<<"Size of original logger: "<<datalogs.size()<<std::endl;

    // Create another DataLog with ID 102 and move it into the Logger.
    Datalog log2(102, std::vector<int>(100,2));

    // creating shared logger object
    SharedLogger logs;

    // adding log to shared log
    auto sharedDataLog = std::make_shared<Datalog>(log);
    logs.addLog(sharedDataLog);

    // displaying all logs
    logs.displayAll();

    // getting sharedobj count
    std::cout<<"Shared obj count: "<<sharedDataLog.use_count()<<std::endl;
    
    // printing by external funct
    printLogInfo(log);

    return 0;
}