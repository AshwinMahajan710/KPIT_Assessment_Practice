#include<string>
#include"Sensor.h"
#include<iostream>
#include<vector>
#include"SensorProcessor.h"
#include"freefunc.h"
#include<thread>

// process in thread
void processInThread(SensorProcessor& processor, Sensor& sensor){
    std::thread th1(std::ref(processor.processSensor), std::ref(sensor));
    th1.join();
}
