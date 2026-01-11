#include<string>
#include"Sensor.h"
#include"PressureSensor.h"
#include"TemperatureSensor.h"
#include<iostream>
#include<vector>
#include<memory>
#include"SensorFleet.h"

int main(){

    // creating sensorFleet obj
    SensorFleet obj;

    // creating 2 tempsensor obj
    std::unique_ptr<Sensor> t1 = std::make_unique<TemperatureSensor>("Temperature",30);
    std::unique_ptr<Sensor> t2 = std::make_unique<TemperatureSensor>("Temperature",80);
    std::unique_ptr<Sensor> p1 = std::make_unique<TemperatureSensor>("Pressure",123);

    // adding this obj
    obj.addSensor(t1);
    obj.addSensor(t2);
    obj.addSensor(p1);

    // display all sensor
    obj.displayAllSensor();

    return 0;
}