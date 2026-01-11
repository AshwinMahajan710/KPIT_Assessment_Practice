#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<functional>
#include"EventProcessor.h"
#include"freefunction.h"

int main(){

    // 1. Create an EventProcessor object.
    EventProcessor obj;
    
    // 2. Add five SensorEvent objects with different types and values (e.g., Temperature=85.0, Pressure=101.3).
    obj.addEvent(SensorEvent(101,"Temperature",1020));
    obj.addEvent(SensorEvent(102,"Pressure",123));
    obj.addEvent(SensorEvent(103,"Gase",020));

    // 3. Display all events using displayAll().
    obj.displayAll();
    
    // 4. Use a lambda expression to filter events where type == "Temperature" and print them using printFilteredEvents().
    std::function<bool(const SensorEvent&)>filter = [](const SensorEvent& event){return event.getType()=="Temperature";};
    std::cout<<"Printing filterd events: "<<std::endl;
    printFilteredEvents(obj.getEvents(),filter);

    // 5. Use a lambda function to increase the value of all "Pressure" events by 10% using processEvents().
    std::function<bool(const SensorEvent&)>filter2 = [](const SensorEvent& event){return event.getType()=="Pressure";};
    std::function<void(SensorEvent&)>action = [](SensorEvent& event) mutable -> void {event.setValue(event.getValue() + (event.getValue()*0.1));};

    obj.processEvents(filter2,action);

    // 6. Display all events again to verify changes.
    std::cout<<"\nPrinting all events again: "<<std::endl;
    obj.displayAll();

    return 0;
}