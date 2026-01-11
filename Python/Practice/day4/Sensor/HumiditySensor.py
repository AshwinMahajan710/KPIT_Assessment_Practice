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
from typing import Dict, List, Any
from typing_extensions import override
from functools import reduce

class HumiditySensor(Sensor):

    # constructor
    def __init__(self, sensor_id:str, location:str, reading:float, unit:str, alerts: List[str], metadata: Dict[str,Any],sensor_age_years: int, maintenance_log: List[str], performance_metrics: Dict[str, float|int]):
        super().__init__(sensor_id, location, reading, unit, alerts, metadata)
        self.sensor_age_years = sensor_age_years
        self.maintenance_log = maintenance_log
        self.performance_metrics = performance_metrics
    
    # status message
    def status_message(self): 
        return "Humidity Sensor: Optimal" if self.reading>=30 and self.reading <=60 else "Humidity Sensor: Alert"
    
    # predicting remaining life
    def predict_remaining_life(self): 
        return  max(0, 10 - self.sensor_age_years)
    
    # return last maintainince log
    def last_maintenance(self) -> str:
        if(len(self.last_maintenance) == 0):
            return "No last record found"
        else:
            return self.maintenance_log[-1]
                
    #  to print details
    def __repr__(self):
        return f"{self.__dict__}"
    