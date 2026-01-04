from enum import Enum , auto

class BatteryType(Enum):
    # LI_ION = auto() // alternate option if don't want to give names and give auto numbering
    # NI_CAD = auto()
    LI_ION = 0
    NI_CAD = 1