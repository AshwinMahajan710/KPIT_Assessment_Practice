#  Class 1: EngineSensor
# • Additional Attributes: 
# o rpm: int
# o temperature: float
# o max_rpm=6000
# • Complex Methods: 
# o Override compute_efficiency(): 
#  Efficiency = (rpm / max_rpm) * (1 - temperature_penalty)
#  Use lambda for penalty calculation.
# o Override status_message(): 
#  Include dynamic analysis: "Engine running smoothly" or "Engine alert!" based on condition of status.(if status is not “OK” then "Engine alert!” otherwise "Engine running smoothly")
# o Override validate_reading(): 
#  Raise EngineOverheatException if temperature > 150°C.
#  Log warnings if rpm exceeds safe range.

from VehicleComponent import VehicleComponent
from typing_extensions import override
from custom_exceptions import EngineOverheatException
import warnings

class EngineSensor(VehicleComponent):
    rpm = 10
    def __init__(self, component_id:str, status:str, reading:int, rpm: int, temperature: float, max_rpm:int = 6000):
        super().__init__(component_id, status, reading)
        self.rpm = rpm
        self.temperature = temperature
        self.max_rpm = max_rpm
    
    @override
    def compute_efficiency(self) -> float:
        temperature_penalty = 0.001 * self.temperature
        return (self.rpm / self.max_rpm) * (1 - temperature_penalty)

    @override 
    def status_message(self) -> str:
        alert = "Engine alert!" if self.status.upper() != "OK" else "Engine Running Smoothly"
        return alert
    
    @override 
    def validate_reading(self) -> bool:
        if (self.temperature > 150):
            raise EngineOverheatException()
        if self.rpm > self.max_rpm:
            warnings.warn("Rpm is exceeding its safe range")
                        
        
    