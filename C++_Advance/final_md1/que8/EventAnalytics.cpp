#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<algorithm>
#include<iostream>
#include"EventAnalytics.h"

// function to add events 
void EventAnalytics::addEvent(const SensorEvent& event){
    m_events.emplace_back(event);
    std::cout<<"Event added successfully..."<<std::endl;
}

// function to sort all events by value
void EventAnalytics::sortByValue(){
    std::sort(m_events.begin(), m_events.end(), [](auto& event1, auto& event2){return event1.getValue()>event2.getValue();});
}

// function to count by type
int EventAnalytics::countByType(const std::string& type) const{
   return std::count_if(m_events.begin(), m_events.end(), [=](auto& event){return event.getType() == type;}); 
} // Uses std::countif with lambda

// function to increase values
void EventAnalytics::increaseValues(double percentage){
    std::for_each(m_events.begin(),m_events.end(), [=](auto& event){event.setValue(event.getValue()+percentage);});
}

// function to display all events
void EventAnalytics::displayAll() const{
    for(auto &event : m_events){
        event.display();
    }
}

// to get sensor event
std::vector<SensorEvent>& EventAnalytics::getEvents(){
    return m_events;
}
