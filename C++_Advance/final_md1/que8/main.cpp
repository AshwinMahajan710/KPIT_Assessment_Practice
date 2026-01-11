#include<iostream>
#include<string>
#include"SensorEvent.h"
#include<vector>
#include<algorithm>
#include<iostream>
#include"EventAnalytics.h"
#include"freefunction.h"

int main(){

    // creating eventAnalytics object
    EventAnalytics obj;

    // 2. Add five SensorEvent objects with different types and values (e.g., Temperature=85.0, Pressure=101.3, Speed=60.0).
    obj.addEvent(SensorEvent(101,"Temperature",101));
    obj.addEvent(SensorEvent(102,"Pressure",102));
    obj.addEvent(SensorEvent(103,"Temperature",103));
    obj.addEvent(SensorEvent(104,"Pressure",104));
    obj.addEvent(SensorEvent(105,"Gas",105));

    // 3. Display all events using displayAll().
    std::cout<<"\nDisplaying all sensors information: "<<std::endl;
    obj.displayAll();

    // 4. Sort events by value using sortByValue() and display them.
    std::cout<<"\nDisplaying sensors after sorting them: "<<std::endl;
    obj.sortByValue();
    obj.displayAll();

    // 5. Count how many events are of type "Temperature" using countByType() and print the result.
    std::cout<<"\nSensors count with type \"Temperature\": "<<obj.countByType("Temperature")<<std::endl;

    // 6. Increase all event values by 10% using increaseValues() and display them.
    std::cout<<"\nIncreasing all values by 10 and then displaying them: "<<std::endl;    
    obj.increaseValues(10);
    obj.displayAll();

    // 7. Print the top 3 events by value using printTopEvents().
    std::cout<<"\nPrinting top 3 events: "<<std::endl;
    printTopEvents(obj.getEvents(), 3);

    return 0;
}