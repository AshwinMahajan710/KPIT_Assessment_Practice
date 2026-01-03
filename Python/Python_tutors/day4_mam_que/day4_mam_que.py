 
# Abstract Base Class: VehicleComponent (Abstract)
# • Attributes: 
# o component_id: str
# o status: str (e.g., "OK", "Fault")
# o reading: float (numeric performance metric)
# • Abstract Methods: 
# o status_message() → Must return a detailed health message.
# o validate_reading() → Must validate readings and raise exceptions if unsafe.
# o compute_efficiency() → Abstract method to calculate efficiency based on component-specific logic.
# Derived Classes
# Class 1: EngineSensor
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
# Custom Exceptions
# • EngineOverheatException : Raised when engine temperature exceeds safe limit.
# • BrakeFailureException : Raised when brake pad thickness is critically low.
# Object Creation
# o Create 3 EngineSensor objects and 2 BrakeSensor objects.
# o Store all objects in a list called components.
# Functions
# Implement the following operations:
# 1. filter_faulty_components(components)
# o Return components where status != "OK".
# o Use list comprehension and isinstance() to group by type.
# 2. sort_components_by_efficiency(components)
# o Sort components by computed efficiency using their compute_efficiency() method.
# o Use lambda with sorted().
# 3. generate_health_report(components)
# Output a dictionary: 
# {
#   "total_components": int,
#   "engine_alerts": int,
#   "brake_alerts": int,
#   "average_efficiency": float
# }
# Use dictionary comprehension and map().
# # EngineSensor Objects
# e1 = EngineSensor(component_id="E001", status="OK", reading=85.0, rpm=2500, temperature=95.0)
# e2 = EngineSensor(component_id="E002", status="Fault", reading=70.0, rpm=7000, temperature=160.0)
# e3 = EngineSensor(component_id="E003", status="OK", reading=90.0, rpm=1500, temperature=110.0)
# # BrakeSensor Objects
# b1 = BrakeSensor(component_id="B001", status="OK", reading=60.0, pad_thickness=4.5, fluid_level=80.0)
# b2 = BrakeSensor(component_id="B002", status="Fault", reading=40.0, pad_thickness=0.8, fluid_level=30.0)
# # Combine into a single list
# components = [e1, e2, e3, b1, b2]
 

from abc import ABC , abstractmethod
from typing import Any, List, Dict
from typing_extensions import override
from warnings import warn

# Custom Exception class
class EngineOverheatException(Exception):
    def __init__(self, max):
        super().__init__(f"Engine temperatutre should be less than {max} ")

class BrakeFailureException(Exception):
    def __init__(self, min_thickness):
        super().__init__(f"Pad thickness should be at least {min_thickness} mm")

# Abstract Base Class
class VehicleComponent(ABC):
    def __init__(self, comp_id : str, status: str, reading: float) -> None:
        self.status = status
        self.component_id = comp_id
        self.reading = reading
    
    @abstractmethod
    def status_message(self) -> str:
        pass

    @abstractmethod
    def validate_reading(self) -> bool:
        pass

    @abstractmethod
    def compute_efficiency(self) -> float:
        pass

# Engine Sensor class
class EngineSensor(VehicleComponent):
    def __init__(self, comp_id, status, reading, rpm, temperature, max_rpm = 6000):
        super().__init__(comp_id, status, reading)
        self.rpm = rpm
        self.temperature = temperature
        self.max_rpm = max_rpm

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"
    
    @override
    def compute_efficiency(self) -> float:
        temp_penalty = 0.001 * self.temperature
        efficiency_cal = lambda : (self.rpm / self.max_rpm) * (1 - temp_penalty)
        return efficiency_cal() 
    @override
    def status_message(self) -> str:
        if self.status.upper() == 'OK':
            return "Engine running smoothly"
        elif self.status.upper() == 'FAULT':
            return "Engine alert!"
        else:
            return 'unknown'
    
    @ override
    def validate_reading(self) -> bool:
        if(self.temperature > 150.0):
           raise EngineOverheatException(150.0)
        elif(self.rpm >self.max_rpm):
            warn("RPM value is breaking the max rpm threshold")
            return True

class BreakSensor(VehicleComponent):
    def __init__(self, comp_id: str, status: str, reading: float, pad_thickness: float, fluid_level: float, ideal_thickness : float = 5.0)-> None:
        super().__init__(comp_id, status, reading)
        self.pad_thickness = pad_thickness
        self.fluid_level = fluid_level
        self.ideal_thickness = ideal_thickness
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    
    @override
    def compute_efficiency(self) -> float:
        efficiency_cal =  lambda: (self.fluid_level / 100) * (self.pad_thickness / self.ideal_thickness)
        return efficiency_cal()
    
    @override
    def status_message(self) -> str:
        return "Brakes optimal" if self.status.upper() == 'OK' else "Brake maintenance required"
    
    @override
    def validate_reading(self) -> bool:
        if self.pad_thickness < 1:
            raise BrakeFailureException(1)
        else :
            print("Validated pad thickness")
            return True

# function to sort by efficiency
def sort_components_by_efficiency(components: List[VehicleComponent]) -> List:
    return sorted(components, key = lambda x: x.compute_efficiency(), reverse= True)

# health report
def generate_health_report(components: List[VehicleComponent]) -> Dict[str,Any]:
    total = len(components)

    return {
        "Total Components: ": len(components),
        "engine_alerts": sum( 1 for c in components if isinstance(c,EngineSensor)),
        "Brake_alerts": sum( 1 for c in components if isinstance(c,BreakSensor)),
        "average_efficiency": sum(c.compute_efficiency() for c in components) / len(components)
    }

def main():
    
    # creating 2 objs of breaksensor
    b1: VehicleComponent = BreakSensor(comp_id="B001", status="OK", reading=60.0, pad_thickness=4.5, fluid_level=80.0)
    b2: VehicleComponent = BreakSensor(comp_id="B002", status="Fault", reading=40.0, pad_thickness=0.8, fluid_level=30.0)

    # creating 3 objs of Engine Sensor
    e1: VehicleComponent = EngineSensor(comp_id="E001", status="OK", reading=85.0, rpm=2500, temperature=95.0)
    e2: VehicleComponent = EngineSensor(comp_id="E002", status="Fault", reading=70.0, rpm=7000, temperature=160.0)
    e3: VehicleComponent = EngineSensor(comp_id="E003", status="OK", reading=90.0, rpm=1500, temperature=110.0)

    # creating list of combined
    components = [b1,b2,e1,e2,e3]

    # 1. filter_faulty_components(components) --> lamda and isinstance
    filter_faulty_components_breaksensor = [component for component in components if isinstance(component, BreakSensor) and component.status.upper() != 'OK']
    filter_faulty_components_enginesensor = [component for component in components if isinstance(component, EngineSensor) and component.status.upper() != 'OK']
    print(f"BreakSensor objs:" ,filter_faulty_components_breaksensor)
    print(f"EngineSensor objs:" ,filter_faulty_components_enginesensor)

    # 2. sort_components_by_efficiency(components) --> using compute_efficiency and lambda
    sorted_list = sort_components_by_efficiency(components=components)
    for c in sorted_list:
        print(c.component_id, c.compute_efficiency())

    # 3. generate_health_report(components)
    health_report = generate_health_report(components=components)
    print(health_report)

if __name__ == "__main__":
    main()