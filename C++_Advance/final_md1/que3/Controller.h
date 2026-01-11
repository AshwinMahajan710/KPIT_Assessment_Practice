#ifndef CONTROLLER_H
#define CONTROLLER_H

#include<string>

class Controller{
    protected:
        std::string m_name;
    public:
        Controller() = default;
        Controller(const std::string& );

        ~Controller() = default;

        virtual void executeCommand() const = 0;

        virtual void displayStatus() const;
    
};

#endif // CONTROLLER_H
