#ifndef EVENTPROCESSOR_H
#define EVENTPROCESSOR_H

#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<functional>

class EventProcessor{
    private:
        std::vector<SensorEvent> m_events;
    public:
        EventProcessor() = default;
        ~EventProcessor() = default;

        // member functions

        // to add event
        void addEvent(const SensorEvent& event);

        // to processEvents
        void processEvents(const std::function<bool(const SensorEvent&)>& filter, const std::function<void(SensorEvent&)>& action);

        // to display all events information
        void displayAll() const;

        // getting sensorEvent vector
        std::vector<SensorEvent>& getEvents();


};


#endif // EVENTPROCESSOR_H
