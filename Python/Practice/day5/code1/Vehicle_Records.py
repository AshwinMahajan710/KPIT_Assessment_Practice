# 2. Class: VehicleRecords
# This class acts as the core of the system, managing all vehicle-related operations.
# Attributes:
# self.vehicles: Dictionary to store vehicle records with vehicle_id as key.
# self.fuel_types: List of allowed fuel types (Gasoline, Diesel, Electric).
# self.transmission_types: List of allowed transmission types (Automatic, Manual).

from typing import Dict, List, Any
from Vehicle_Types import VehicleType
from Vehicle import Vehicle
from Exceptions import InvalidArgumentException

class VehicleRecords():

    # static variable to maintain id:
    vehicle_id = 0

    # a) create empy dictionary with vehicle_id and vehicle_object
    def __init__(self):
        self.vehicles: Dict[int, Vehicle] = {}
        self.fuel_types: List = ['Gasoline', 'Diesel', 'Electric'] 
        self.transmission_types: List = ['Automatic', 'Manual']
    
    # b) adding new vehicle object
    def add_vehicle(self, vehicle_type: VehicleType, make: str, model: str,price: float | int, fuel_type: str, transmission_type: str, mileage: float) -> None:
        VehicleRecords.vehicle_id = VehicleRecords.vehicle_id + 1
        if fuel_type not in self.fuel_types or transmission_type not in self.transmission_types:
            InvalidArgumentException("Invalid fuel type or transmission type given as argument")
        newVehicle:Vehicle = Vehicle(VehicleRecords.vehicle_id, make, model, price, vehicle_type, fuel_type, transmission_type, mileage)
        self.vehicles[VehicleRecords.vehicle_id] = newVehicle
        print("New Vehicle added successfully")
    

    # c) remove_vehicle(self, vehicle_id)
    def remove_vehicle(self, vehicle_id: int) -> None:
        if vehicle_id not in self.vehicles.keys():
            print("Not found")
            return
        else:
            del self.vehicles[vehicle_id]
            print("Object deleted successfully")
    
    # d) update_vehicle(self, vehicle_id, make=None, model=None, year=None, fuel_type=None, transmission_type=None, mileage=None)   
    def update_vehicle(self, vehicle_id, make=None, model=None, fuel_type=None, transmission_type=None, mileage=None):
        if vehicle_id not in self.vehicles.keys():
            print("Not found")
            return
        else:
            if make is not None:
                self.vehicles[vehicle_id][make]= make
            if model is not None:
                self.vehicles[vehicle_id][model] = model
            if fuel_type is not None:
                if fuel_type not in self.fuel_types:
                    InvalidArgumentException("Invalid fuel type given as argument")
                self.vehicles[vehicle_id][fuel_type] =fuel_type
            if transmission_type is not None:
                if transmission_type not in self.transmission_types:
                    InvalidArgumentException("Invalid transmission type given as argument")
                self.vehicles[vehicle_id][fuel_type] =fuel_type
            if mileage is not None:
                self.vehicles[vehicle_id][mileage] = mileage
            print("Updated details sucessfully")

    # e) get_vehicle_info(self, vehicle_id)
    def get_vehicle_info(self, vehicle_id) -> None:
        if vehicle_id not in self.vehicles.keys():
            print("Not found")
            return
        else:
            print("Object fund given are the details: ", self.vehicles[vehicle_id])
            
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