from abc import ABC, abstractmethod

class VehicleComponent(ABC):
    def __init__(self, component_id: str, status: str, reading: float):
        super().__init__()
        self.component_id = component_id
        self.status = status
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
    
    def __repr__(self):
        return f"{self.__dict__}"
    
def main():
    vehicle: VehicleComponent = VehicleComponent("101","OK",101)
    print(vehicle)
    
# • Attributes: 
# o component_id: str
# o status: str (e.g., "OK", "Fault")
# o reading: float (numeric performance metric)
# • Abstract Methods: 
# o status_message() → Must return a detailed health message.
# o validate_reading() → Must validate readings and raise exceptions if unsafe.
# o compute_efficiency() → Abstract method to calculate efficiency based on component-specific logic.