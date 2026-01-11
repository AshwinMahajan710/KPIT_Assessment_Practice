from HumiditySensor import HumiditySensor
from Sensor import Sensor
from TemperatureSensor import TemperatureSensor
from typing import Dict, List, Any

# Create Objects
# • Create at least 3 TemperatureSensor objects and 2 HumiditySensor objects.
# • Store all objects in a single list called sensors.

def main():
    temp_sensor1: Sensor = TemperatureSensor("101","ECU",101,"asd", ["Low Battery", "Signal Lost"], {"manufacturer": "ABC Corp", "model": "X100", "warranty_years": 2} , [12.3,34.5],{"offset": 0.5, "scale": 1.02})
    temp_sensor2: Sensor = TemperatureSensor("101","ECU",101,"asd", ["Low Battery", "Signal Lost"], {"manufacturer": "ABC Corp", "model": "X100", "warranty_years": 2} , [12.3,34.5],{"offset": 0.7, "scale": 1.09})
    temp_sensor3: Sensor = TemperatureSensor("101","ECU",101,"asd", ["Low Battery", "Signal Lost"], {"manufacturer": "ABC Corp", "model": "X100", "warranty_years": 2} , [12.3,34.5],{"offset": 0.9, "scale": 0.02})
    hum_sensor2: Sensor = HumiditySensor("101","ECU",101,"asd", ["Low Battery", "Signal Lost"], {"manufacturer": "ABC Corp", "model": "X100", "warranty_years": 2},5, ["not miantained", "maintained on 12/10/25"],{"Good": 101,"Bad": 102})

    sensors = [temp_sensor1,temp_sensor2,temp_sensor3, hum_sensor2]
if __name__ == "__main__":
    main()