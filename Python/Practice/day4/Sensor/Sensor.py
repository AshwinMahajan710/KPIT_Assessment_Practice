# Base Class: Sensor
# • Attributes: 
# o sensor_id (string)
# o location (string)
# o reading (float)
# o unit (string)
# o alerts (list of strings): e.g., ["Low Battery", "Signal Lost"]
# o metadata (dict): e.g.{"manufacturer": "ABC Corp", "model": "X100", "warranty_years": 2}
# • Methods: 
# o Initialize attributes.
# o Getters and setters.
# o __repr__() for readable representation.
# o status_message(): Default message: "Sensor operational" (to be overridden).

from typing import List, Dict, Any

class Sensor:
    def __init__(self, sensor_id: str, location: str, reading: float, unit: str, alerts: List[str], metadata: Dict[str,Any]):
        sensor_id: str = sensor_id
        location: str = location
        reading: float = reading
        unit: str = unit
        alerts: List[str] = alerts
        metadata: Dict[str,Any] = metadata
    
    def __repr__(self):
        return f"{self.__dict__}"
    
    def status_message(self)-> str:
        return f"Sensor operational"