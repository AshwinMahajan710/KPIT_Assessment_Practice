#ifndef SHAREDLOGGER_H
#define SHAREDLOGGER_H

#include"Datalog.h"
#include<vector>
#include<cstddef>
#include<iostream>
#include<memory>

class SharedLogger{
    private:
        std::vector<std::shared_ptr<Datalog>> m_logs;
    
        public:
            SharedLogger() = default;
            ~SharedLogger() = default;

            void addLog(std::shared_ptr<Datalog> log); // Accepts sharedptr

            void displayAll() const; // Prints info of all logs
            
};
#endif // SHAREDLOGGER_H
