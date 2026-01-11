#ifndef DIAGNOSTICRECORD_H
#define DIAGNOSTICRECORD_H

#include"Severity.h"
#include<string>

class DiagnosticRecord{
    private:
        int m_code;
        Severity m_severity;

    public:

        // constructor
        DiagnosticRecord(int code, Severity severity);
        DiagnosticRecord(const DiagnosticRecord&) =  default;
        DiagnosticRecord(DiagnosticRecord&&) =  default;

        // destructor
        ~DiagnosticRecord()=default;

        // getters
        int getCode() const;
        Severity getSeverity() const;
        std::string getSeverityStr() const;

        //to display
        void display() const;
};

#endif // DIAGNOSTICRECORD_H
