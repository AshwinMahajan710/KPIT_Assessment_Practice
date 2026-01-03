# Derived Class 2: HumiditySensor
# • Additional Attributes: 
# o sensor_age_years (int)
# o maintenance_log (list of strings): e.g., ["Filter replaced", "Firmware updated"]
# o performance_metrics (dict): e.g.{"accuracy": 98.5, "response_time_ms": 120}
# • Methods: 
# o Override status_message(): "Humidity Sensor: Optimal" if reading between 30% and 60% else "Humidity Sensor: Alert".
# o predict_remaining_life(): Remaining life = max(0, 10 - sensor_age_years).
# o last_maintenance(): Return last entry from maintenance_log.

from Sensor import Sensor
from typing import List, Dict, Any
from typing_extensions import override

# temperature Sensor
class HumiditySensor(Sensor):
    
    def __init__(self, sensor_id: str, location: str, reading: str, unit: str, alerts: List[float], metadata: Dict[str, Any], sensor_age_years: int, maintenance_log: List[str], performance_metrics: Dict[str,float]):
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.sensor_age_years = sensor_age_years
        self.maintenance_log = maintenance_log
        self.performance_metrics = performance_metrics
    
    @override
    def status_message(self) -> str:
        return "Humidity Sensor: Optimal" if 30.0 < float(self.reading) < 60.0 else "Humidity Sensor: Alert"

    def predict_remaining_life(self) -> float:
        return max(0,10-self.sensor_age_years)
    
    def last_maintenance(self) -> str:
        return self.maintenance_log[-1] if self.maintenance_log else "No maintenance recorded"
    