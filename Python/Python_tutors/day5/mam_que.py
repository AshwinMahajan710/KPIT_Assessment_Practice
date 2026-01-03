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
 
 

from enum import Enum

# Define Enum for Vehicle Types

class VehicleType(Enum):

    CAR = "Car"

    TRUCK = "Truck"

    MOTORCYCLE = "Motorcycle"

class VehicleRecords:

    def __init__(self):

        self.vehicles = {}

        self.fuel_types = ["Gasoline", "Diesel", "Electric"]

        self.transmission_types = ["Automatic", "Manual"]

    def add_vehicle(self, vehicle_type: VehicleType, make, model, year, fuel_type, transmission_type, mileage=0):

        if not isinstance(vehicle_type, VehicleType):

            raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")

        vehicle_id = len(self.vehicles) + 1

        self.vehicles[vehicle_id] = {

            "vehicle_type": vehicle_type.value,  # Store the string value

            "make": make,

            "model": model,

            "year": year,

            "fuel_type": fuel_type,

            "transmission_type": transmission_type,

            "mileage": mileage,

            "maintenance_records": []

        }

        print(f"Vehicle added with ID: {vehicle_id}")

    def remove_vehicle(self, vehicle_id):

        if vehicle_id in self.vehicles:

            del self.vehicles[vehicle_id]

            print(f"Vehicle with ID {vehicle_id} removed")

        else:

            print(f"Vehicle with ID {vehicle_id} not found")

    def update_vehicle(self, vehicle_id, make=None, model=None, year=None, fuel_type=None, transmission_type=None, mileage=None):

        if vehicle_id in self.vehicles:

            if make:

                self.vehicles[vehicle_id]["make"] = make

            if model:

                self.vehicles[vehicle_id]["model"] = model

            if year:

                self.vehicles[vehicle_id]["year"] = year

            if fuel_type:

                self.vehicles[vehicle_id]["fuel_type"] = fuel_type

            if transmission_type:

                self.vehicles[vehicle_id]["transmission_type"] = transmission_type

            if mileage:

                self.vehicles[vehicle_id]["mileage"] = mileage

            print(f"Vehicle with ID {vehicle_id} updated")

        else:

            print(f"Vehicle with ID {vehicle_id} not found")

    def get_vehicle_info(self, vehicle_id):

        return self.vehicles.get(vehicle_id, None)

    def drive_vehicle(self, vehicle_id, miles):

        if vehicle_id in self.vehicles:

            self.vehicles[vehicle_id]["mileage"] += miles

            print(f"Vehicle with ID {vehicle_id} driven for {miles} miles")

        else:

            print(f"Vehicle with ID {vehicle_id} not found")

    def perform_maintenance(self, vehicle_id, maintenance_type, description):

        if vehicle_id in self.vehicles:

            self.vehicles[vehicle_id]["maintenance_records"].append({

                "maintenance_type": maintenance_type,

                "description": description

            })

            print(f"Maintenance performed on Vehicle with ID {vehicle_id}")

        else:

            print(f"Vehicle with ID {vehicle_id} not found")

    def display_all_vehicles(self):

        for vehicle_id, vehicle_info in self.vehicles.items():

            print(f"Vehicle ID: {vehicle_id}")

            print(f"Vehicle Type: {vehicle_info['vehicle_type']}")

            print(f"Make: {vehicle_info['make']}")

            print(f"Model: {vehicle_info['model']}")

            print(f"Year: {vehicle_info['year']}")

            print(f"Fuel Type: {vehicle_info['fuel_type']}")

            print(f"Transmission Type: {vehicle_info['transmission_type']}")

            print(f"Mileage: {vehicle_info['mileage']}")

            print(f"Maintenance Records: {vehicle_info['maintenance_records']}")

            print("--------------------")

    def filter_vehicles_by_type(self, vehicle_type: VehicleType):

        if not isinstance(vehicle_type, VehicleType):

            raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")

        filtered_vehicles = {

            vehicle_id: vehicle_info

            for vehicle_id, vehicle_info in self.vehicles.items()

            if vehicle_info["vehicle_type"] == vehicle_type.value

        }

        return filtered_vehicles

# Example Usage

vehicle_records = VehicleRecords()

# Add vehicles using Enum

vehicle_records.add_vehicle(VehicleType.CAR, "Toyota", "Corolla", 2015, "Gasoline", "Automatic", 50000)

vehicle_records.add_vehicle(VehicleType.TRUCK, "Ford", "F-150", 2018, "Diesel", "Manual", 30000)

vehicle_records.add_vehicle(VehicleType.MOTORCYCLE, "Honda", "CBR500R", 2020, "Gasoline", "Manual", 10000)

# Display all vehicles

vehicle_records.display_all_vehicles()

# Filter by Enum type

filtered_vehicles = vehicle_records.filter_vehicles_by_type(VehicleType.CAR)

print("Filtered Vehicles by Type:")

for vehicle_id, vehicle_info in filtered_vehicles.items():

    print(vehicle_info) 
 
#  ===============================================================================================================================

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
#      → Validate Enums and store in batteries.
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
 
 
# Solution:
# from enum import Enum
 
# class BatteryType(Enum):
#    LI_ION = "Lithium-Ion"
#    NIMH = "Nickel-Metal Hydride"
#    LEAD_ACID = "Lead Acid"
#    SOLID_STATE = "Solid State"
 
# class BatteryStatus(Enum):
#    CHARGING = "Charging"
#    DISCHARGING = "Discharging"
#    IDLE = "Idle"
#    FAULT = "Fault"
 
# class Battery:
#    def __init__(self, battery_id, battery_type: BatteryType, status: BatteryStatus, voltage: float, temperature: float):
#        if not isinstance(battery_type, BatteryType):
#            raise ValueError("Invalid battery type. Must be BatteryType Enum.")
#        if not isinstance(status, BatteryStatus):
#            raise ValueError("Invalid battery status. Must be BatteryStatus Enum.")
       
#        self.battery_id = battery_id
#        self.battery_type = battery_type
#        self.status = status
#        self.voltage = voltage
#        self.temperature = temperature
 
#    def __repr__(self):
#        return f"Battery(ID={self.battery_id}, Type={self.battery_type.value}, Status={self.status.value}, Voltage={self.voltage}, Temp={self.temperature})"
 
# class BatteryManagementSystem:
#    def __init__(self, max_voltage_limit=4.2, min_voltage_limit=2.5, max_temp_limit=60):
#        self.batteries = {}
#        self.max_voltage_limit = max_voltage_limit
#        self.min_voltage_limit = min_voltage_limit
#        self.max_temp_limit = max_temp_limit
#        self.alerts = []
 
#    # Add Battery
#    def add_battery(self, battery: Battery):
#        self.batteries[battery.battery_id] = battery
#        print(f"Battery {battery.battery_id} added.")
 
#    # Remove Battery
#    def remove_battery(self, battery_id):
#        if battery_id in self.batteries:
#            del self.batteries[battery_id]
#            print(f"Battery {battery_id} removed.")
#        else:
#            print("Battery not found.")
 
#    # Update Status
#    def update_status(self, battery_id, new_status: BatteryStatus):
#        if battery_id in self.batteries:
#            self.batteries[battery_id].status = new_status
#            print(f"Battery {battery_id} status updated to {new_status.value}.")
#        else:
#            print("Battery not found.")
 
#    # Monitoring & Calculations
#    def calculate_total_voltage(self):
#        return sum(b.voltage for b in self.batteries.values())
 
#    def calculate_average_temperature(self):
#        return sum(b.temperature for b in self.batteries.values()) / len(self.batteries) if self.batteries else 0
 
#    def battery_with_max_voltage(self):
#        return max(self.batteries.values(), key=lambda b: b.voltage)
 
#    def battery_with_min_temperature(self):
#        return min(self.batteries.values(), key=lambda b: b.temperature)
 
#    def filter_above_max_temp(self):
#        return {bid: b for bid, b in self.batteries.items() if b.temperature > self.max_temp_limit}
 
#    def filter_below_min_voltage(self):
#        return {bid: b for bid, b in self.batteries.items() if b.voltage < self.min_voltage_limit}
 
#    # Alerts using lambda
#    def generate_alerts(self):
#        check_alert = lambda b: (
#            f"Alert: Battery {b.battery_id} abnormal condition!" 
#            if b.voltage > self.max_voltage_limit or b.voltage < self.min_voltage_limit or b.temperature > self.max_temp_limit 
#            else None
#        )
#        self.alerts = [alert for b in self.batteries.values() if (alert := check_alert(b))]
#        return self.alerts
 
#    # Summary dictionary of voltages
#    def summary_voltages(self):
#        return {bid: b.voltage for bid, b in self.batteries.items()}
 
#    # List of battery types
#    def list_battery_types(self):
#        return [b.battery_type.value for b in self.batteries.values()]
 
#    # Sort batteries by voltage
#    def sort_by_voltage(self):
#        return sorted(self.batteries.values(), key=lambda b: b.voltage)
 
#    # Sort by temperature descending
#    def sort_by_temperature_desc(self):
#        return sorted(self.batteries.values(), key=lambda b: b.temperature, reverse=True)
 
#    # Count batteries by status
#    def count_by_status(self):
#        return {status.value: sum(1 for b in self.batteries.values() if b.status == status) for status in BatteryStatus}
 
#    # Predict charging completion time (simple model)
#    def predict_charging_time(self, battery_id, charging_rate=0.1):
#        if battery_id in self.batteries and self.batteries[battery_id].status == BatteryStatus.CHARGING:
#            remaining = self.max_voltage_limit - self.batteries[battery_id].voltage
#            return (lambda r: remaining / r)(charging_rate)
#        return None
 
#    # Check if all batteries are healthy
#    def all_batteries_healthy(self):
#        return all(self.min_voltage_limit <= b.voltage <= self.max_voltage_limit and b.temperature <= self.max_temp_limit for b in self.batteries.values())
 
# # Example Usage
# bms = BatteryManagementSystem()
# # Add batteries
# b1 = Battery(1, BatteryType.LI_ION, BatteryStatus.CHARGING, 3.7, 35)
# b2 = Battery(2, BatteryType.NIMH, BatteryStatus.IDLE, 2.4, 40)
# b3 = Battery(3, BatteryType.LEAD_ACID, BatteryStatus.DISCHARGING, 4.3, 65)
 
# bms.add_battery(b1)
# bms.add_battery(b2)
# bms.add_battery(b3)
 
# print("\nTotal Voltage:", bms.calculate_total_voltage())
# print("Average Temperature:", bms.calculate_average_temperature())
# print("Max Voltage Battery:", bms.battery_with_max_voltage())
# print("Min Temp Battery:", bms.battery_with_min_temperature())
# print("Alerts:", bms.generate_alerts())
# print("Summary Voltages:", bms.summary_voltages())
# print("Battery Types:", bms.list_battery_types())
# print("Sorted by Voltage:", bms.sort_by_voltage())
# print("Sorted by Temp Desc:", bms.sort_by_temperature_desc())
# print("Count by Status:", bms.count_by_status())
# print("Charging Time Prediction for Battery 1:", bms.predict_charging_time(1))
# print("All Batteries Healthy?", bms.all_batteries_healthy())
# ===============================================================================================================================

# Abstract Base Class: VehicleComponent (Abstract)
# Attributes:  
# component_id: str
# status: str (e.g., "OK", "Fault")
# reading: float (numeric performance metric)
# Abstract Methods:
# status_message() → Must return a detailed health message.
# validate_reading() → Must validate readings and raise exceptions if unsafe.
# compute_efficiency() → Abstract method to calculate efficiency based on component-specific logic.
 
# Derived Classes
# Class 1: EngineSensor
# Additional Attributes:
# rpm: int
# temperature: float
# max_rpm=6000
# Complex Methods:
# Override compute_efficiency():
# Efficiency = (rpm / max_rpm) * (1 - temperature_penalty)
# Use lambda for penalty calculation.
# Override status_message():
# Include dynamic analysis: "Engine running smoothly" or "Engine alert!" based on condition of status.(if status is not “OK” then "Engine alert!” otherwise "Engine running smoothly")
# Override validate_reading():
# Raise EngineOverheatException if temperature > 150°C.
# Log warnings if rpm exceeds safe range.
 
# Class 2: BrakeSensor
# Additional Attributes:
# pad_thickness: float (in mm)
# fluid_level: float (in %)
# ideal_thickness=5.0
# Complex Methods:
# Override compute_efficiency():
# Efficiency = (fluid_level / 100) * (pad_thickness / ideal_thickness)
# Use lambda for quick ratio calculation.
# Override status_message():
# Return "Brakes optimal" or "Brake maintenance required" with severity level.
# (if status is not “OK” then " Brake maintenance required” otherwise " Brakes optimal ")
 
# Override validate_reading():
# Raise BrakeFailureException if pad_thickness < 1 mm.
# Suggest maintenance schedule dynamically.
 
# Custom Exceptions
# EngineOverheatException : Raised when engine temperature exceeds safe limit.
# BrakeFailureException : Raised when brake pad thickness is critically low.
 
# Object Creation
# Create 3 EngineSensor objects and 2 BrakeSensor objects.
# Store all objects in a list called components.
 
# Functions
# Implement the following operations:
# filter_faulty_components(components)
# Return components where status != "OK".
# Use list comprehension and isinstance() to group by type.
# sort_components_by_efficiency(components)
# Sort components by computed efficiency using their compute_efficiency() method.
# Use lambda with sorted().
# generate_health_report(components)
# Output a dictionary:
# {
# "total_components": int,
# "engine_alerts": int,
# "brake_alerts": int,
# "average_efficiency": float
# }
# Use dictionary comprehension and map().
 
# # EngineSensor Objects
# e1 = EngineSensor(component_id="E001", status="OK", reading=85.0, rpm=2500, temperature=95.0)
# e2 = EngineSensor(component_id="E002", status="Fault", reading=70.0, rpm=7000, temperature=160.0)
# e3 = EngineSensor(component_id="E003", status="OK", reading=90.0, rpm=1500, temperature=110.0)
 
# # BrakeSensor Objects
# b1 = BrakeSensor(component_id="B001", status="OK", reading=60.0, pad_thickness=4.5, fluid_level=80.0)
# b2 = BrakeSensor(component_id="B002", status="Fault", reading=40.0, pad_thickness=0.8, fluid_level=30.0)
 
# # Combine into a single list
# components = [e1, e2, e3, b1, b2]

# ================================================================================================================================