# enums.py
from enum import Enum

class BatteryType(Enum):
    LI_ION = "Lithium-Ion"
    NIMH = "Nickel-Metal Hydride"
    LEAD_ACID = "Lead Acid"
    SOLID_STATE = "Solid State"

class BatteryStatus(Enum):
    CHARGING = "Charging"
    DISCHARGING = "Discharging"
    IDLE = "Idle"
    FAULT = "Fault"
