# Create a class Battery with the following attributes:
# cell_voltage (list of floats): Voltage of each cell in the battery pack.
# current (float): Current flowing through the battery (positive for discharge, negative for charge).
# temperature (float): Battery pack temperature in Celsius.
# cycle_count (int): Number of charge/discharge cycles completed.

from typing import Dict, List, Any

# def Battery
class Battery:
    def __init__(self, cell_voltage: List[float], current: float, temperature: float, cycle_count: int):
        self.cell_voltage = cell_voltage
        self.current = current
        self.temperature = temperature
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    
    

        