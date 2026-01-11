#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<functional>
#include"EventProcessor.h"
#include"freefunction.h"

// printing filtered events
void printFilteredEvents(const std::vector<SensorEvent>& events, const std::function<bool(const SensorEvent&)>& filter){
    for (auto& event: events){
        if(filter(event)){
            event.display();
        }
    }
}