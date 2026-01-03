from enum import Enum , auto

class BatteryType(Enum):
    # LI_ION = auto() // alternate option if don't want to give names and give auto numbering
    # NI_CAD = auto()
    LI_ION = "Li_ion"
    NI_CAD = "Ni_cad"