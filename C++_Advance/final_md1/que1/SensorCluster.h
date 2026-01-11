#ifndef SENSORCLUSTER_H
#define SENSORCLUSTER_H
#include"Sensor.h"
#include"SensorStatus.h"
#include<vector>
#include<string>

class SensorCluster final{
    private:
        std::string m_clusterName;
        std::vector<Sensor*> sensors;
    public:

        explicit SensorCluster(const std::string& );

        // deleting assignment ops
        SensorCluster& operator = (const SensorCluster&) = delete;
        SensorCluster& operator = (SensorCluster&&) = delete;

        // default destructor
        ~SensorCluster() = default;

        void addSensor(Sensor* sensor);
        void displayClusterInfo() const;

};

#endif // SENSORCLUSTER_H
