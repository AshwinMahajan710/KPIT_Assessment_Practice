#ifndef ENGINE_H
#define ENGINE_H

#include<string>
#include"EngineType.h"

class Engine{
    public:
        std::string m_engineId;
        int m_horsePower;
        EngineType m_engineType;
        float m_engineCapacity;
        float m_engineTorque;

        // Engine();
        Engine(const std::string& id, int hp, EngineType type, float capacity, float torque);

        // display function
        void display();

        // function to get type as string
        std::string getTypeName() const;
};

#endif // ENGINE_H
