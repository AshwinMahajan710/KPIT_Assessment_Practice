# Case Study1:
# Design a Vehicle Management System that allows users to store, update, and manage records of different types of vehicles. The system should:
# Support multiple vehicle types (Car, Truck, Motorcycle) using Enum for type safety.
# Allow adding, removing, updating, and retrieving vehicle details.
# Track mileage and maintenance history for each vehicle.
# Provide filtering capabilities based on vehicle type.
# Display all stored vehicle records in a readable format.
# Class and Function Details:
# 1. Enum: VehicleType
# Purpose: Defines allowed vehicle types using Python's Enum for type safety.
# Values: CAR, TRUCK, MOTORCYCLE
# Why Enum? Prevents invalid vehicle type entries and improves code readability.
# 2. Class: VehicleRecords
# This class acts as the core of the system, managing all vehicle-related operations.
# Attributes:
# self.vehicles: Dictionary to store vehicle records with vehicle_id as key.
# self.fuel_types: List of allowed fuel types (Gasoline, Diesel, Electric).
# self.transmission_types: List of allowed transmission types (Automatic, Manual).
# Functions in VehicleRecords
# a) __init__(self)
# Purpose: Initializes the vehicle records system.
# Details: Creates an empty dictionary for vehicles and sets allowed fuel and transmission types.
# b) add_vehicle(self, vehicle_type, make, model, year, fuel_type, transmission_type, mileage=0)
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