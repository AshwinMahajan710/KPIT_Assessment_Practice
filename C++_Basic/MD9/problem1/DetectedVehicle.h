#ifndef DETECTEDVEHICLE_H
#define DETECTEDVEHICLE_H

class DetectedVehicle{
    private:
        int m_id;
        float m_distanceMeters;
        float m_relativeSpeedMps;
        bool m_isBraking;
    
    public:
        DetectedVehicle();
        DetectedVehicle(int id, float distanceMeter, float relativeSpeed, bool isBraking);

        // getters
        int getId() const;
        float getDistanceMeters() const;
        float getRelativeSpeedMps() const;
        bool getIsBraking() const;

        // setters
        void setId(int id); // accept only non negative id
        void setDistanceMeters(float distanceMeter ); // if newDist < 0.0f then dist = 0.0f
        void setRelativeSpeedMps(float relativeSpeed);
        void setIsBraking(bool isBraking);
};

#endif
