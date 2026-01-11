# Class 2: BrakeSensor
# • Additional Attributes: 
# o pad_thickness: float (in mm)
# o fluid_level: float (in %)
# o ideal_thickness=5.0
# • Complex Methods: 
# o Override compute_efficiency(): 
#  Efficiency = (fluid_level / 100) * (pad_thickness / ideal_thickness)
#  Use lambda for quick ratio calculation.
# o Override status_message(): 
#  Return "Brakes optimal" or "Brake maintenance required" with severity level.
# (if status is not “OK” then " Brake maintenance required” otherwise " Brakes optimal ")
# o Override validate_reading(): 
#  Raise BrakeFailureException if pad_thickness < 1 mm.
#  Suggest maintenance schedule dynamically.

from VehicleComponent import VehicleComponent
from typing_extensions import override
from custom_exceptions import BrakeFailureException

class BrakeSensor(VehicleComponent):
    
    def __init__(self, component_id: str, status: str, reading: int, pad_thickness: float, fluid_level:float, ideal_thickness=5.0):
        super().__init__(component_id, status, reading)
        self._pad_thickness: float = pad_thickness
        self.fluid_level: float = fluid_level
        self.ideal_thickness = ideal_thickness

    @property
    def pad_thickness(self):
        return self._pad_thickness

    @pad_thickness.setter
    def pad_thickness(self, val):
        self._pad_thickness = 123

    @override
    def compute_efficiency(self) -> float:
        ans = lambda: (self.fluid_level / 100) * (self.pad_thickness / self.ideal_thickness)
        return ans()

    @override
    def status_message(self) -> str:
        return "Brakes Optimal" if self.status.upper()=="OK" else "Brake Maintainance Required"
    
    @override
    def validate_reading(self) -> bool:
        if self.pad_thickness<1:
            raise BrakeFailureException("Pad thickness critical as they are less that 1mm")
        else :
            print("Validated pad thickness")
            return True
    
    def __repr__(self):
        return f"{self.__dict__}"