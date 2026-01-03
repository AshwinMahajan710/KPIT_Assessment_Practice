# Battery Management System Class:
# Create a class BMS that manages the Battery object and implements SoH estimation.
# Implement the following functions using Lambda expressions where appropriate:
# calculate_average_cell_voltage():
# Input: cell_voltages (List of floats): A list representing the voltage of each cell in the battery.
# Task: Calculate the average voltage of all cells in the input list. Uses a Lambda function for a concise calculation.
# Output: float: The average cell voltage. Returns 0.0 if the input list is empty.
# Constraints:
# Input list must contain only numerical values (floats or integers).
# Handles empty input list gracefully.
# detect_overvoltage(threshold):
# Input:
# cell_voltages (List of floats): A list representing the voltage of each cell.
# threshold (float): The voltage threshold. Cells with voltage exceeding this threshold are considered overvoltage.
# Task: Identify cells in cell_voltages that exceed the specified threshold. Uses a Lambda function with filter() to achieve this. Returns a list of indices (positions) of the overvoltage cells.
# Output: List[int]: A list of indices corresponding to the cells exceeding the threshold. Returns an empty list if no cells exceed the threshold.

from Battery import Battery

class BMS:
    
    battery: Battery = None 

    # change the battery
    def changeBattery(cls, newBattery: Battery):
        if(isinstance(newBattery, Battery)):
            cls.battery = newBattery
            print("New Battery assigned..")
        else:
            raise
    