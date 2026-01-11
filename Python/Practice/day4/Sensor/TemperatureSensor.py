# Derived Class 1: TemperatureSensor
# • Additional Attributes: 
# o historical_readings (list of floats): e.g., [22.5, 23.0, 21.8]
# o calibration_values (dict): e.g.{"offset": 0.5, "scale": 1.02}
# • Methods: 
# o Override status_message(): "Temperature Sensor: Normal" if reading between 15°C and 35°C else "Temperature Sensor: Alert".
# o average_temperature(): Compute average from historical_readings.
# o apply_calibration(): Adjust reading using calibration_values.

from Sensor import Sensor
from typing import Dict, List, Any
from typing_extensions import override
from functools import reduce

class TemperatureSensor(Sensor):
    def __init__(self, sensor_id:str, location:str, reading:float, unit:str, alerts: List[str], metadata: Dict[str,Any], historical_readings: List[float], calibration_values: Dict[str,float]):
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.historical_readings = historical_readings
        self.calibration_values = calibration_values

    @override    
    def status_message(self) -> str:
        return "Temperature Sensor: Normal" if self.reading >= 15 and self.reading <= 35 else "Temperature Sensor: Alert"
    
    def average_temperature(self):
        return reduce(lambda acc,y: acc + y, self.historical_readings, 0.0)/ len(self.historical_readings)
    
    def apply_calibration(self):
        scale = self.calibration_values.get("scale",1.0)
        offset = self.calibration_values.get("offset",0.0)
        self.reading = (float(self.reading) * scale) + offset
    
    def __repr__(self):
        return f"{self.__dict__}"

