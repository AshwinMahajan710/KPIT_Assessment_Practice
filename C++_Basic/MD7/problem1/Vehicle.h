#ifndef VEHICLE_H
#define VEHICLE_H
#include<string>

class Vehicle{
    private:
        std::string m_vehicleID{};
        std::string m_fuelType{};
        double m_fuelEfficiency;
        double m_totalDistanceTravelled;
        double m_totaFuelConsumed;
        static double s_averageFuelPrice;
    
    public:
        Vehicle();
        Vehicle(const std::string& vehicleID_, const std::string& fuelType_, double fuelEfficiency_);
        void TrackFuelConsumption(double fuelConsumed_, double distanceTravelled_); // should update vals
        double calculateFuelEconomy(); // calculate current fuel efficiency
        void displayVehicleInfo() const;
        static void updateAvergaeFuelPrice(double avergaeFuelPrice);
        double calculateTotalFuelCost(double distanceToTravel) const;
};

#endif // VEHICLE_H
