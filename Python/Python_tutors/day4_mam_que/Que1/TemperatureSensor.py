# Derived Class 1: TemperatureSensor
# • Additional Attributes: 
# o historical_readings (list of floats): e.g., [22.5, 23.0, 21.8]
# o calibration_values (dict): e.g.{"offset": 0.5, "scale": 1.02}
# • Methods: 
# o Override status_message(): "Temperature Sensor: Normal" if reading between 15°C and 35°C else "Temperature Sensor: Alert".
# o average_temperature(): Compute average from historical_readings.
# o apply_calibration(): Adjust reading using calibration_values.

from Sensor import Sensor
from typing import List, Dict, Any
from typing_extensions import override

# temperature Sensor
class TemperatureSensor(Sensor):
    
    def __init__(self, sensor_id: str, location: str, reading: str, unit: str, alerts: List[float], metadata: Dict[str, Any], historical_readings: List[float], calibration_values: Dict[str, Any]):
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.historical_readings = historical_readings
        self.calibration_values = calibration_values
    
    @override
    def status_message(self) -> str:
        return "Temperature Sensor: Normal" if 15.0 < float(self.reading) < 35.0 else "Temperature Sensor: Alert"

    def average_temperature(self) -> float:
        return sum(reading for reading in self.historical_readings)/ len(self.historical_readings)
    
    def apply_calibration(self) -> None:
        scale = self.calibration_values.get("scale",1.0)
        offset = self.calibration_values.get("offset",0.0)
        self.reading = (float(self.reading) * scale) + offset
    



    
    