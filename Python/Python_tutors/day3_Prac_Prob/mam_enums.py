from enum import Enum , auto

class BatteryType(Enum):
    LI_ION = auto()
    NIMH =  auto()
    LEAD_ACID  = auto()
    SOLID_STATE =  auto()

class BatteryStatus(Enum):
    CHARGING = auto()
    DISCHARGING = auto()
    IDLE = auto()
    FAULT = auto()
