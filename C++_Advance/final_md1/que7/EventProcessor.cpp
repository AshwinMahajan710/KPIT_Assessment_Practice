#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<functional>
#include"EventProcessor.h"

// to add event
void EventProcessor::addEvent(const SensorEvent& event){
    m_events.emplace_back(event);
    std::cout<<"Sensor obj added successfully....."<<std::endl;
}

// to processEvents
void EventProcessor::processEvents(const std::function<bool(const SensorEvent&)>& filter, const std::function<void(SensorEvent&)>& action){
    for(auto& event: m_events){
        if(filter(event)){
            action(event);
        }
    }
}

// to display all events information
void EventProcessor::displayAll() const{
    for(auto& event: m_events){
        event.display();
    }
}

// to get sensor event
std::vector<SensorEvent>& EventProcessor::getEvents(){
    return m_events;
}