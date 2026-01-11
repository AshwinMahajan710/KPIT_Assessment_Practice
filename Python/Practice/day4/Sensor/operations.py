from HumiditySensor import HumiditySensor
from Sensor import Sensor
from TemperatureSensor import TemperatureSensor
from typing import Dict, List, Any

# Function 1: filter_sensors_with_alerts(sensors)
# • Input: sensors (list of Sensor objects)
# • Task: Return all sensors that have at least one alert.
# • Output: List of Sensor objects with non-empty alerts.
# def filter_sensors_with_alerts(sensors: )
# Function 2: sort_sensors_by_reading(sensors)
# • Input: sensors (list of Sensor objects)
# • Task: Sort sensors in ascending order of their reading.
# • Output: Sorted list of Sensor objects.

# Function 3: extract_sensor_ids(sensors)
# • Input: sensors (list of Sensor objects)
# • Task: Extract all sensor IDs into a list.
# • Output: List of strings (sensor IDs).

# Function 4: compute_average_reading(sensors)
# • Input: sensors (list of Sensor objects)
# • Task: Compute the average of all sensor readings.
# • Output: Float (average reading).

# Function 5: add_alert_to_sensor(sensor, alert)
# • Input: 
# o sensor → A single Sensor object (or derived class object).
# o alert → String representing the alert message (e.g., "Low Battery").
# • Task: 
# o Add the given alert to the sensor’s alerts list only if it is not already present.
# • Output: 
# o Updated Sensor object with the new alert added.
# • Constraints: 
# o Must handle: 
#  Duplicate prevention.
#  Empty alert string (ignore if blank).

# Function 6: display_all_sensors
# • Name: display_all_sensors(sensors)
# • Input: 
# o sensors → List of Sensor objects (including derived classes).
# • Task: 
# o Print details of each sensor in the list 
# o Include sensor type (TemperatureSensor or HumiditySensor).
# • Output: 
# o Printed representation of all sensor objects.
# '''
