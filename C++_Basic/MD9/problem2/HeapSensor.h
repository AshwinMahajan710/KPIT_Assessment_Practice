#ifndef HEAPSENSOR_H
#define HEAPSENSOR_H

class HeapSensor{
    private:
        int m_id;
        float m_voltageV;
        float m_temperatureC;
        bool m_active;
        static int s_totalInstances;

    public:
        static float MIN_VOLTAGE;
        static float MAX_VOLTAGE;
        static float MIN_TEMPERATURE;
        static float MAX_TEMPERATURE;

        HeapSensor();
        HeapSensor(int id, float voltageV, float temperatureC, bool active); // also increment total instances
        ~HeapSensor(); // decrement total instances

        // Getters
        int getId() const;
        float getVoltageV() const;
        float getTemperatureC() const;
        bool getActive() const;
        static int getTotalInstances();

        // setters
        void setId(int id);
        void setVoltageV(float voltage); // clamp to max voltage and min voltage
        void setTemperatureC(float temperature); // clamp to max temperature and min temperature
        void setActive(bool active);    
        
        // overloaded member functions
        void calibrate(float tempOffset); // adding offset to temperature via setter (old temp + offset)
        void calibrate(float tempScale, float tempOffset); // (oldtemp * scale) + offset

};

#endif // HEAPSENSOR_H
