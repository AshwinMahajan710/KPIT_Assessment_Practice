# # Base Class: Sensor
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
    def __init__(self, sensor_id: str, location: str, reading: str, unit: str, alerts: List[str], metadata: Dict[str,Any])->None:
        self._sensor_id = sensor_id
        self._location = location
        self._reading = reading
        self._unit = unit
        self._alerts = alerts
        self._metadata = metadata

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    
    # writing getters and setters
    @property
    def sensor_id(self)-> str:
        return self._sensor_id
    @property
    def location(self)-> str:
        return self._location
    @property
    def reading(self)-> str:
        return self._reading
    @property
    def unit(self)-> str:
        return self._unit
    @property
    def alerts(self)-> List[float]:
        return self._alerts
    @property
    def metadata(self)-> Dict[str, Any]:
        return self._metadata
    
    # all setters
    @sensor_id.setter
    def sensor_id(self, id: str)-> None:
        if(isinstance(id, str)):
            self._sensor_id = id
        else:
            raise ValueError("Invalid type passed")
        
    @location.setter
    def location(self, location: str)-> None:
        if(isinstance(location, str)):
            self._location = location
        else:
            raise ValueError("Invalid type passed")
        
    @reading.setter
    def reading(self, reading: str)-> None:
        if(isinstance(reading, str)):
            self._reading = reading
        else:
            raise ValueError("Invalid type passed")
        
    @unit.setter
    def unit(self, unit: str)-> None:
        if(isinstance(unit, str)):
            self._unit = unit
        else:
            raise ValueError("Invalid type passed")
        
    @alerts.setter
    def alerts(self, alerts: List[float])-> None:
        if(isinstance(alerts, list)):
            self._alerts = alerts
        else:
            raise ValueError("Invalid type passed")
        
    @metadata.setter
    def metadata(self, metadata: Dict[str,Any])-> None:
        if(isinstance(metadata, dict)):
            self._metadata = metadata
        else:
            raise ValueError("Invalid type passed")
         
    # status function
    def status_message(self) -> str: 
        return "Sensor operational"
    