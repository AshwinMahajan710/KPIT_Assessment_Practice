# Manages a dictionary of Battery objects and performs operations using lambda and comprehensions.
from typing import Dict, List, Any, Optional
from Battery import Battery
from enums import BatteryStatus, BatteryType
from CustomExceptions import InvalidDataTypeException
from functools import reduce

# class BatteryManagementSystem
class BatteryManagementSystem:
    def __init__(self, batteries: Optional[Dict[int,Battery]] = None, max_voltage_limit: float = 0.0, min_voltage_limit: float = 0.0, max_temp_limit:float = 0.0, alerts: Optional[List[str]]= None):

        # now check battries provided or not and based on that assign them to class variables
        self.batteries = batteries if batteries else {}
        self.alerts = alerts if alerts else []

        # validate batteries 
        if not isinstance(self.batteries, dict):
            raise InvalidDataTypeException(f"InvalidDataTypeException: Expected Dict got {type(self.batteries)}")

        for k,v in self.batteries.items():
            if not isinstance(k,int): 
                raise InvalidDataTypeException(f"InvalidDataTypeException: Expected int for id got {type(k)}")
            if not isinstance(v,Battery): 
                raise InvalidDataTypeException(f"InvalidDataTypeException: Expected type 'Battery' for value got {type(v)}")
        
        # validate alerts 
        if not isinstance(self.alerts, list):
            raise InvalidDataTypeException(f"InvalidDataTypeException: Expected List got {type(self.alerts)}")

        for val in self.alerts:
            if not isinstance(val,str): 
                raise InvalidDataTypeException(f"InvalidDataTypeException: Expected str for alert got {type(val)}")
        
        # validate max_voltage_limit, min_voltage_limit, max_temp_limit
        if not isinstance(max_voltage_limit, (float,int)):
            raise InvalidDataTypeException("voltage limit not as per type")
        if not isinstance(min_voltage_limit, (float,int)):
            raise InvalidDataTypeException("voltage limit not as per type")
        if not isinstance(max_temp_limit, (float,int)):
            raise InvalidDataTypeException("temperature limit not as per type")

        # assign values
        self.max_voltage_limit = max_voltage_limit
        self.min_voltage_limit = min_voltage_limit
        self.max_temp_limit=max_temp_limit # → Safety thresholds.
    
    # Function to add battery
    def add_battery(self):
        try:
            battery_id = int(input("Enter battery id: "))

            battery_type = BatteryType(
                input("Enter battery type (Li_ion, NIMH, Lead_Acid, Solid_State): ").strip()
            )

            status = BatteryStatus(
                input("Enter Battery Status (Charging, Discharging, Idle, Fault): ").strip()
            )

            voltage = float(input("Enter voltage: "))
            temperature = float(input("Enter Temperature: "))

            self.batteries[battery_id] = Battery(
                battery_id, battery_type, status, voltage, temperature
            )

            print(f"Battery object with id {battery_id} added successfully...")

        except ValueError as e:
            print("Invalid input:", e)
    
    # find battery by id
    def find_battery(self, battery_id: int) -> bool:
        if not isinstance(battery_id, int):
            raise InvalidDataTypeException(f"Expected battery_id type to search is expected as int got {type(battery_id )}")
        return True if battery_id in self.batteries.keys() else False
            
    # Remove a Battery by ID
    def remove_battery(self, battery_id: int) -> bool:
        if self.find_battery(battery_id):
            del self.batteries[battery_id]
            print(f"Battery with id {battery_id} removed successfully...")
            return True
        else:
            print(f"Battery with id {battery_id} not found")
            return False
            
    # Update Battery status:→ Change Enum status dynamically.
    def update_battery_status(self, battery_id: int, new_status: BatteryStatus)->bool:
        if not self.find_battery(battery_id):
            print(f"Battery with id {battery_id} not found...")
            return False
        if not isinstance(new_status, BatteryStatus):
            raise InvalidDataTypeException(f"Expected type BatteryStatus, got {type(new_status)}")
        self.batteries[battery_id].status = new_status
        print("Battery status updated successfully....")
        
    # * * * * * * * * * * Monitoring & Calculation * * * * * * * * * * 

    # Calculate total voltage of all batteries.
    def calculate_total_voltage(self) -> float:
        return reduce(lambda acc,y: acc + y.voltage, self.batteries.values(), 0.0)
    
    # Calculate average temperature.
    def calculate_average_temperature(self) -> float:
        return reduce(lambda acc,y : acc + y.temperature, self.batteries.values(), 0.0) / len(self.batteries)
    
    # Find battery with max voltage
    def battery_with_max_voltage(self) -> Battery:
        if len(self.batteries) == 0:
            print("No Batteries present")
            return None
        else:
            return reduce(lambda x,y: x if x.voltage > y.voltage else y, self.batteries.values())
    
    # Find battery with min temperature
    def battery_with_min_temperature(self) -> Battery:
        if len(self.batteries) == 0:
            print("No Batteries present")
            return None
        else:
            return reduce(lambda x,y: x if x.temperature < y.temperature else y, self.batteries.values())
    
    # Filter batteries above max temperature
    # Filter batteries below min voltage.
    # Generate alerts for abnormal conditions:→ Use lambda to check and append alerts.
    # Create summary dictionary of battery voltages.
    # Create list of battery types.
    # Sort batteries by voltage
    # Sort batteries by temperature descending
    # Count batteries by status
    # Predict charging completion time:→ Lambda based on voltage difference and charging rate.
    # Generate historical voltage trend:→ Extract voltages from logs using [h['voltage'] for h in history].
    # Check if all batteries are healthy (within limits)
    
    