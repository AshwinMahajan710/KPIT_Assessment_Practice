# 2. Class: VehicleRecords
# This class acts as the core of the system, managing all vehicle-related operations.
# Attributes:
# self.vehicles: Dictionary to store vehicle records with vehicle_id as key.
# self.fuel_types: List of allowed fuel types (Gasoline, Diesel, Electric).
# self.transmission_types: List of allowed transmission types (Automatic, Manual).

from typing import Dict, List, Any
from Vehicle_Types import VehicleType
from Vehicle import Vehicle

class VehicleRecords():

    # static variable to maintain id:
    vehicle_id = 0

    # a) create empy dictionary with vehicle_id and vehicle_object
    def __init__(self):
        self.vehicles: Dict[int, Vehicle] = {}
        self.fuel_types: List = ['Gasoline', 'Diesel', 'Electric'] 
        self.transmission_types: List = ['Automatic', 'Manual']
    
    # b) adding new vehicle object
    def add_vehicle(self, vehicle_type: VehicleType, make: str, model: str, fuel_type: str, transmission_type: str, mileage: float):
        
# Purpose: Adds a new vehicle to the system.
# Steps:
# Validate vehicle_type is an instance of VehicleType.
# Generate a unique vehicle_id based on current count.
# Store vehicle details in self.vehicles dictionary.
# Key Features: Initializes maintenance_records as an empty list for future service logs.
# c) remove_vehicle(self, vehicle_id)
# Purpose: Deletes a vehicle record by its ID.
# Behavior: Prints confirmation if removed, else shows "not found".
# d) update_vehicle(self, vehicle_id, make=None, model=None, year=None, fuel_type=None, transmission_type=None, mileage=None)
# Purpose: Updates specific details of a vehicle.
# Logic: Checks if vehicle_id exists, then updates only provided fields (partial update supported).
# e) get_vehicle_info(self, vehicle_id)
# Purpose: Retrieves details of a specific vehicle.
# Returns: Dictionary of vehicle info or None if not found.
# f) drive_vehicle(self, vehicle_id, miles)
# Purpose: Simulates driving the vehicle by adding miles to its mileage.
# Validation: Ensures vehicle exists before updating mileage.
# g) perform_maintenance(self, vehicle_id, maintenance_type, description)
# Purpose: Logs maintenance activity for a vehicle.
# Details: Appends a dictionary with maintenance_type and description to maintenance_records.
# h) display_all_vehicles(self)
# Purpose: Prints all vehicle records in a readable format.
# Output: Displays each vehicle's details and maintenance history.
# i) filter_vehicles_by_type(self, vehicle_type)
# Purpose: Returns a dictionary of vehicles matching the given type.
# Validation: Ensures vehicle_type is a valid VehicleType.