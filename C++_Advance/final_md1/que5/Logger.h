#ifndef LOGGER_H
#define LOGGER_H

#include"Datalog.h"
#include<vector>
#include<cstddef>
#include<iostream>

class Logger{
    private:
        std::vector<Datalog> m_logs;
    public:
        Logger() = default;
        ~Logger() = default;

        void addLog(Datalog log); // Should use move semantics when adding
        void displayAll() const; // Prints info of all logs
};

#endif // LOGGER_H
