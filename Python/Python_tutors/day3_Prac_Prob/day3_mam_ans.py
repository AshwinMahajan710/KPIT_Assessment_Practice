# Create two classes:
# Battery → Represents individual battery cells with 5 attributes (including Enums).
# BatteryManagementSystem → Manages a dictionary of Battery objects and performs operations using lambda and comprehensions.
 
# -Enums to Use
# BatteryType → LI_ION, NIMH, LEAD_ACID, SOLID_STATE
# BatteryStatus → CHARGING, DISCHARGING, IDLE, FAULT
 
# -Battery Class
# Attributes:
# battery_id → Unique identifier for the battery.
# battery_type → Enum BatteryType.
# status → Enum BatteryStatus.
# voltage → Current voltage of the battery.
# temperature → Current temperature of the battery.
 
# BatteryManagementSystem Class
# Attributes:
# batteries → Dictionary where key = battery_id, value = Battery object.
# max_voltage_limit, min_voltage_limit, max_temp_limit → Safety thresholds.
# alerts → List of alerts generated.
 
# Functionalities (using lambda & comprehensions)
# Add a new Battery object to dictionary
#       → Validate Enums and store in batteries.

# Remove a Battery by ID
# Update Battery status:→ Change Enum status dynamically.
# Monitoring & Calculation
# Calculate total voltage of all batteries.
# Calculate average temperature.
# Find battery with max voltage
# Find battery with min temperature.
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

from mam_enums import BatteryType, BatteryStatus
from typing import List, Dict, Any, Optional

class Battery:
    def __init__(self, id_: int, type_: BatteryType, status_: BatteryStatus ,voltage_: float, temperature_:float)-> None:
        self.battery_id = id_
        self.battery_type = type_
        self.battery_status = status_
        self.voltage = voltage_
        self.temperature = temperature_
    
    def __repr__(self) -> str:
        return f"| Battery_Id: {self.battery_id} | Battery_Type: {self.battery_type.name} | Battery_Status: {self.battery_status.name} | Voltage: {self.voltage} |   Temperature: {self.temperature} |"

# BatteryManagementSystem Class
class BatteryManagementSystem:
    def __init__(self, max_voltage_limit: float, min_voltage_limit: float, max_temp_limit: float):
        self.batteries : Dict[int , Battery] = {}
        self.max_voltage_limit: float = max_voltage_limit
        self.min_voltage_limit: float = min_voltage_limit
        self.max_temp_limit: float = max_temp_limit
    
    # function to add battery
    def addBattery(self, battery: Battery) -> None:
        if (isinstance(battery.battery_type , BatteryType) and isinstance(battery.battery_status, BatteryStatus)):
            self.batteries[battery.battery_id] = battery
        else:
            raise RuntimeError("Invalid Battry types")  
    
    # function to show all stored batter objs
    def show_batteries(self) -> None:
        for battery in self.batteries.items():
            print(battery)
    
    # function to remove battery 
    def remove_Battery_by_id(self,  id: int) -> None:
        if id in self.batteries:
            del(self.batteries[id])
            print(f"Battery details of id {id} deleted successfully...")
        else:
            print(f"Battery details of id {id} not found")
    
    # function to update battery status
    def update_battery_status(self, id: int, status: BatteryStatus) -> None:
        if(id in self.batteries):
            print(f"Battery Status updated successfully")
            self.batteries[id].battery_status = status
        else:
            print(f"Battery details of id {id} not found")
    
    # function to calculate average temperature
    def calculateAverageTemperature(self) -> float:
        ''' --> works but not best practice
        sum = 0
        for battery in self.batteries:
            sum += self.batteries[battery].temperature
        return sum/len(self.batteries)
        '''
        return sum(b.temperature for b in self.batteries.values()) / len(self.batteries)

    # function to get total voltage of all batteries
    def calculateTotalVoltage(self) -> float:
            return sum(b.voltage for b in self.batteries.values())

    # function to return battery with highest voltage
    def findBatteryWithMaxVoltage(self) -> Battery:
        return max(self.batteries.values(), key = lambda b: b.voltage)
    
    # function to return battery with min temperature
    def findBatteryWithMinTemp(self) -> Battery:
        return min(self.batteries.values(), key = lambda b: b.temperature)
    
    # function to return battery with highest voltage
    def findBatteryWithMAXTemp(self) -> Battery:
        return max(self.batteries.values(), key = lambda b: b.temperature)

    # function to filter batteries with temp higher than max_temp_limit
    def filter_batteries_above_max_temp(self) -> List[Battery]:
        return list(filter(battery for battery in self.batteries.values() if (battery.temperature > self.max_temp_limit)))
    

if __name__=="__main__":
    system: BatteryManagementSystem = BatteryManagementSystem(240, 100, 100)
    system.addBattery(Battery(101,BatteryType.LEAD_ACID, BatteryStatus.CHARGING, 102, 30))
    system.addBattery(Battery(102,BatteryType.LI_ION, BatteryStatus.DISCHARGING, 92, 30))
    system.addBattery(Battery(103,BatteryType.NIMH, BatteryStatus.FAULT, 192, 130))
    system.addBattery(Battery(104,BatteryType.SOLID_STATE, BatteryStatus.IDLE, 92, 50))
    system.addBattery(Battery(105,BatteryType.NIMH, BatteryStatus.FAULT, 2, 13))

    # # 0. Showing the stored batteries
    # system.show_batteries()

    # # 1. Removing battery by id
    # system.remove_Battery_by_id(101)
    # system.show_batteries()

    # # 2. updating status of battery
    # system.update_battery_status(id=101 ,status= BatteryStatus.DISCHARGING)
    # system.show_batteries()
    
    # # 4. Getting total voltage
    # print(f"Total Voltage of batteries is: ",system.calculateTotalVoltage()) 

    # # 5. Calculate average temperature.
    # print(f"Average temperature of all batteries is: ",system.calculateAverageTemperature()) 

    # # 6. Find battery with max voltage
    # print(f"Following are the details of battery with maximum voltage: ", {system.findBatteryWithMaxVoltage()})

    # # 7. Find batteries with min temp
    # print(f"Following are the details of battery with min temperature: ", {system.findBatteryWithMinTemp()})

    # # 7.2. find battries with max temp
    # print(f"Following are the details of battery with max temperature: ", {system.findBatteryWithMAXTemp()})

    # 8. Filter batteries above max temperature


