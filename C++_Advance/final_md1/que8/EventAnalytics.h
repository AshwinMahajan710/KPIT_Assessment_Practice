#ifndef EVENTANALYTICS_H
#define EVENTANALYTICS_H

#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<algorithm>
#include<iostream>

class EventAnalytics{
    private:
        std::vector<SensorEvent> m_events;
    
    public:
        EventAnalytics() = default;
        ~EventAnalytics() = default;

        void addEvent(const SensorEvent& event);

        void sortByValue(); // Uses std::sort with lambda

        int countByType(const std::string& type) const; // Uses std::countif with lambda

        void increaseValues(double percentage); // Uses std::foreach with lambda

        void displayAll() const;

        // getting sensorEvent vector
        std::vector<SensorEvent>& getEvents();

};

#endif // EVENTANALYTICS_H
