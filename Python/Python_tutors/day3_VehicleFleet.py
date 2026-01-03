# Case Study: Automotive Vehicle Management System
 
# A vehicle manufacturing company wants to manage its vehicle inventory, including details such as vehicle type, model, year, color, and engine type. The company also wants to track the sales and maintenance history of each vehicle.
 
# Program Requirements:
 
# Create a Vehicle class to store vehicle information.
# Create a Sales class to store sales information and update the vehicle status.
# Create a Maintenance class to store maintenance information and update the vehicle status.
# Implement functions to:
# Add a vehicle to the inventory.
# Display vehicle information.
# Update vehicle status (e.g., sold, in-maintenance).
# Record sales information.
# Record maintenance information.
# Display sales history for a vehicle.
# Display maintenance history for a vehicle.

from day3_enum_Type import EngineType, Status
from typing import List, Dict, Any

class Vehicle:
    def __init__(self, Make: str, Model: str,Year:int, Color: str, engineType: EngineType, Price: float) -> None : 
        self.make : str = Make
        self.model : str = Model
        self.price : float = Price
        self.year = Year
        self.color = Color
        self.engineType = engineType
        
    def __repr__(self) -> str:
        return f"Car Name: {self.make}  Car Model: {self.model}   Manf. Year: {self.year} Color: {self.color} EngineType: {self.engineType.name} Car Price: {self.price} "

class Sales:
    def __init__(self, status: Status)->None:
        self.status: List[Status] = []
        self.vehicles: List[Dict[str, Any]] = []

    # def add_details(self, )
    def show_details(self) -> str:
        message = "Following are the details for the vehicles stored: \n"
        for idx, vehicle in enumerate(self.vehicles):
            message += str(vehicle)
            message += "  Sale Status: "
            message += self.status[idx] + "\n"
        return message

vehicleDetails = Sales()
vehicleDetails.addVehicle(Vehicle("Toyota","Camry",2021,"RED",EngineType.PETROL, 123456.8))
vehicleDetails.addVehicle(Vehicle("Toyota","Hilux",123456))
vehicleDetails.addVehicle(Vehicle("Toyota","Fortuner",123456))

print(Vehicle.printVehiclesInfo())
