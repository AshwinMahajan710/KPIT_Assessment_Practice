#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<algorithm>
#include<iostream>
#include"EventAnalytics.h"
#include"freefunction.h"

// printing top events
void printTopEvents(const std::vector<SensorEvent>& events, size_t topN){
    for(int i=0;i<topN;i++){
        events[i].display();
    }
}