
#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<functional>
#include"EventProcessor.h"

void printFilteredEvents(const std::vector<SensorEvent>& events,
const std::function<bool(const SensorEvent&)>& filter);