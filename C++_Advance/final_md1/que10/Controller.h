#ifndef CONTROLLER_H
#define CONTROLLER_H

#include<string>

class Controller{
    private:
        std::string m_name;
    
    public:    
        explicit Controller(const std::string& name);
        virtual ~Controller() = default;
        virtual void execute() const = 0;
        std::string getName() const;
};

#endif // CONTROLLER_H
