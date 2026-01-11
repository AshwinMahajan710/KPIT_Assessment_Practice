#include<vector>
#include"DiagnosticRecord.h"
#include"DiagnosticManager.h"
#include"Severity.h"
#include<iostream>
#include<string>

void DiagnosticManager::addRecord(const DiagnosticRecord& record){
    records.push_back(record);
    std::cout<<"Record added successfully: "<<std::endl;
}

// adding recode in list
void DiagnosticManager::displayAll() const{
    for(DiagnosticRecord record: records){
        record.display();
    }
}

RecordPtr DiagnosticManager::findRecordByCode(int code){
    for(DiagnosticRecord record: records){
        if (record.getCode() == code){
            return &record;
        }
    }
    return nullptr;
}