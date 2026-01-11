#include"DiagnosticRecord.h"
#include"Severity.h"
#include<iostream>
#include<string>

// constructor --> default
DiagnosticRecord::DiagnosticRecord(int code, Severity severity) : m_code(code), m_severity(severity){}

// getters
int DiagnosticRecord::getCode() const{
    return m_code;
}
Severity DiagnosticRecord::getSeverity() const{
    return m_severity;
}

std::string DiagnosticRecord::getSeverityStr() const{
    switch (m_severity)
    {
        case Severity::Critical:
            return "Critical";
       
        case Severity::High:
            return "High";
       
        case Severity::Low:
            return "Low";

        case Severity::Medium:
            return "Medium";
    
        default:
            return "None";
    }
}

//to display
void DiagnosticRecord::display() const{
    std::cout<<"Code: "<<m_code<<std::endl;
    std::cout<<"Severity: "<<getSeverityStr()<<std::endl;
}