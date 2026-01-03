from enum import Enum, auto

# enum for batterytype
class BatteryType(Enum):
    LI_ION = "Li_ion"
    NIMH = "NIMH"
    LEAD_ACID = "Lead_Acid" 
    SOLID_STATE = "Solid_State"

# enum for battery status
class BatteryStatus(Enum):
    CHARGING = "Charging"
    DISCHARGING =  "Discharging"
    IDLE = "Idle"
    FAULT = "Fault"