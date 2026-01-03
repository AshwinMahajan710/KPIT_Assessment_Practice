'''
# Design a system to monitor environmental conditions using different types of sensors.

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

# Derived Class 1: TemperatureSensor
# • Additional Attributes: 
# o historical_readings (list of floats): e.g., [22.5, 23.0, 21.8]
# o calibration_values (dict): e.g.{"offset": 0.5, "scale": 1.02}
# • Methods: 
# o Override status_message(): "Temperature Sensor: Normal" if reading between 15°C and 35°C else "Temperature Sensor: Alert".
# o average_temperature(): Compute average from historical_readings.
# o apply_calibration(): Adjust reading using calibration_values.

# Derived Class 2: HumiditySensor
# • Additional Attributes: 
# o sensor_age_years (int)
# o maintenance_log (list of strings): e.g., ["Filter replaced", "Firmware updated"]
# o performance_metrics (dict): e.g.{"accuracy": 98.5, "response_time_ms": 120}
# • Methods: 
# o Override status_message(): "Humidity Sensor: Optimal" if reading between 30% and 60% else "Humidity Sensor: Alert".
# o predict_remaining_life(): Remaining life = max(0, 10 - sensor_age_years).
# o last_maintenance(): Return last entry from maintenance_log.

# Create Objects
# • Create at least 3 TemperatureSensor objects and 2 HumiditySensor objects.
# • Store all objects in a single list called sensors.

# Function 1: filter_sensors_with_alerts(sensors)
# • Input: sensors (list of Sensor objects)
# • Task: Return all sensors that have at least one alert.
# • Output: List of Sensor objects with non-empty alerts.

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

from Sensor import Sensor
from typing import List, Dict, Any
from TemperatureSensor import TemperatureSensor
from HumiditySensor import HumiditySensor

def main():
    
    # creating 3 temperature Sensor obj and 2 Humidity Sensor obj
    # Create three TemperatureSensor objects
    sensor1: Sensor = TemperatureSensor(
        sensor_id="T01",
        location="Lab Room 1",
        reading="25.0",  # as string
        unit="C",
        alerts=[20.0, 30.0],
        metadata={"manufacturer": "SensorTech", "model": "ST-100"},
        historical_readings=[22.5, 23.0, 24.0],
        calibration_values={"scale": 1.02, "offset": 0.5}
    )

    sensor2: Sensor = TemperatureSensor(
        sensor_id="T02",
        location="Lab Room 2",
        reading="30.0",
        unit="C",
        alerts=[28.0, 32.0],
        metadata={"manufacturer": "SensorTech", "model": "ST-200"},
        historical_readings=[28.0, 29.5, 30.0],
        calibration_values={"scale": 1.01, "offset": 0.2}
    )

    sensor3: Sensor = TemperatureSensor(
        sensor_id="T03",
        location="Server Room",
        reading="18.0",
        unit="C",
        alerts=[15.0, 35.0],
        metadata={"manufacturer": "ThermoCorp", "model": "TC-500"},
        historical_readings=[17.5, 18.0, 18.5],
        calibration_values={"scale": 1.03, "offset": 0.0}
    )

    # Create three HumiditySensor objects
    sensor4: Sensor = HumiditySensor(
        sensor_id="H01",
        location="Greenhouse 1",
        reading="45.0",  # as string
        unit="%",
        alerts=[30.0, 60.0],
        metadata={"manufacturer": "HumidTech", "model": "HT-100"},
        sensor_age_years=2,
        maintenance_log=["Filter replaced", "Firmware updated"],
        performance_metrics={"accuracy": 98.5, "response_time_ms": 120}
    )

    sensor5: Sensor = HumiditySensor(
        sensor_id="H02",
        location="Server Room",
        reading="55.0",
        unit="%",
        alerts=[],
        metadata={"manufacturer": "HumidTech", "model": "HT-200"},
        sensor_age_years=5,
        maintenance_log=["Firmware updated"],
        performance_metrics={"accuracy": 97.0, "response_time_ms": 150}
    )

    # creating list of sensors
    sensors = [sensor1,sensor2,sensor3,sensor4,sensor5]

    ## Function 1: filter_sensors_with_alerts(sensors)
    # • Input: sensors (list of Sensor objects)
    # • Task: Return all sensors that have at least one alert.
    # • Output: List of Sensor objects with non-empty alerts.
    sensors_with_alerts = [sensor for sensor in sensors if len(sensor.alerts)!=0]
    print(list(sensor.sensor_id for sensor in sensors_with_alerts))

    # Function 2: sort_sensors_by_reading(sensors)
    # • Input: sensors (list of Sensor objects)
    # • Task: Sort sensors in ascending order of their reading.
    # • Output: Sorted list of Sensor objects.
    sorted_sensors = sorted(sensors, key=lambda x: x.reading)
    print(list(sensor.sensor_id for sensor in sorted_sensors))

    # // DONE
    # # Function 3: extract_sensor_ids(sensors)
    # • Input: sensors (list of Sensor objects)
    # • Task: Extract all sensor IDs into a list.
    # • Output: List of strings (sensor IDs).

    # Function 4: compute_average_reading(sensors)
    # • Input: sensors (list of Sensor objects)
    # • Task: Compute the average of all sensor readings.
    # • Output: Float (average reading).
    print(sum(float(sensor.reading) for sensor in sensors)/ len(sensors))
    
if __name__ == "__main__":
    main()




