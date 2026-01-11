#ifndef DIAGNOSTICMANAGER_H
#define DIAGNOSTICMANAGER_H

#include<vector>
#include"DiagnosticRecord.h"
#include"Severity.h"
#include<iostream>
#include<string>

using RecordList = std::vector<DiagnosticRecord>;
using RecordPtr = DiagnosticRecord*;

class DiagnosticManager{
    private:
        RecordList records;
    public:
        DiagnosticManager() = default;
        ~DiagnosticManager() =default;
        void addRecord(const DiagnosticRecord& record);
        void displayAll() const;
        RecordPtr findRecordByCode(int code);
};


#endif // DIAGNOSTICMANAGER_H
