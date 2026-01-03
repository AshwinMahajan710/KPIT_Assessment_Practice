# class Vehicle:
#     """Represents a vehicle in the fleet."""

#     def __init__(self, vehicle_id, vehicle_type, fuel_capacity, maintenance_cost, last_service_days, delivery_rating):
#         self.vehicle_id = vehicle_id
#         self.vehicle_type = vehicle_type  # e.g., "Van", "Truck"
#         self.fuel_capacity = fuel_capacity  # Liters
#         self.maintenance_cost = maintenance_cost  # Last maintenance cost
#         self.last_service_days = last_service_days  # Days since last service
#         self.delivery_rating = delivery_rating # Rating between 1-5

#     def __repr__(self):
#         return (f"Vehicle ID: {self.vehicle_id}, Type: {self.vehicle_type}, Fuel: {self.fuel_capacity}, "
#                 f"Maintenance: {self.maintenance_cost}, Service Days: {self.last_service_days}, Rating: {self.delivery_rating}")


# class VehicleFleetManager:
#     """Manages a fleet of vehicles."""

#     def __init__(self):
#         self.vehicles = []

#     def add_vehicle(self, vehicle):
#         """Adds a vehicle to the fleet."""
#         self.vehicles.append(vehicle)
#         print(f"Vehicle {vehicle.vehicle_id} added to the fleet.")

#     def remove_vehicle(self, vehicle_id):
#         """Removes a vehicle from the fleet by ID."""
#         self.vehicles = [v for v in self.vehicles if v.vehicle_id != vehicle_id]
#         print(f"Vehicle {vehicle_id} removed from the fleet.")

#     def get_vehicle(self, vehicle_id):
#         """Retrieves a vehicle by its ID."""
#         for vehicle in self.vehicles:
#             if vehicle.vehicle_id == vehicle_id:
#                 return vehicle
#         return None

#     def get_vehicles_by_type(self, vehicle_type):
#        """Returns a list of vehicles of a specific type."""
#        return [vehicle for vehicle in self.vehicles if vehicle.vehicle_type == vehicle_type]

#     def calculate_statistic(self, operation):
#         """Calculates a statistic (avg, sum, min, max) for maintenance_cost."""
#         if not self.vehicles:
#             return None  # Handle empty fleet case

#         values = [vehicle.maintenance_cost for vehicle in self.vehicles]

#         if operation == "avg":
#             return sum(values) / len(values)
#         elif operation == "sum":
#             return sum(values)
#         elif operation == "min":
#             return min(values)
#         elif operation == "max":
#             return max(values)
#         else:
#             return None # Invalid operation

#     def filter_greater_than(self, threshold):
#         """Filters vehicles where maintenance_cost is greater than the threshold."""
#         return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost > threshold]

#     def filter_less_than(self, threshold):
#         """Filters vehicles where maintenance_cost is less than the threshold."""
#         return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost < threshold]

#     def filter_equal_to(self, threshold):
#         """Filters vehicles where maintenance_cost is equal to the threshold."""
#         return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost == threshold]


#     def sort_vehicles(self, reverse=False):
#         """Sorts vehicles based on maintenance_cost."""
#         return sorted(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost, reverse=reverse)

#     def find_min_vehicle(self):
#         """Finds the vehicle with the minimum maintenance_cost."""
#         if not self.vehicles:
#             return None
#         return min(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost)

#     def find_max_vehicle(self):
#         """Finds the vehicle with the maximum maintenance_cost."""
#         if not self.vehicles:
#             return None
#         return max(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost)

# # Example Usage:
# fleet_manager = VehicleFleetManager()
# v1 = Vehicle("V101", "Van", 60, 500, 30, 4)
# v2 = Vehicle("V102", "Van", 70, 600, 15, 5)
# v3 = Vehicle("T201", "Truck", 200, 2000, 60, 3)
# fleet_manager.add_vehicle(v1)
# fleet_manager.add_vehicle(v2)
# fleet_manager.add_vehicle(v3)

# print(f"Average Maintenance Cost: {fleet_manager.calculate_statistic('avg')}")
# print(f"Sum of Maintenance Costs: {fleet_manager.calculate_statistic('sum')}")
# print(f"Minimum Maintenance Cost: {fleet_manager.calculate_statistic('min')}")
# print(f"Maximum Maintenance Cost: {fleet_manager.calculate_statistic('max')}")

# high_maintenance_vehicles = fleet_manager.filter_greater_than(700)
# print(f"Vehicles with Maintenance Cost > 700: {high_maintenance_vehicles}")

# sorted_by_maintenance = fleet_manager.sort_vehicles()
# print(f"Sorted by Maintenance Cost: {sorted_by_maintenance}")

# min_maintenance_vehicle = fleet_manager.find_min_vehicle()
# print(f"Vehicle with Minimum Maintenance Cost: {min_maintenance_vehicle}")

# max_maintenance_vehicle = fleet_manager.find_max_vehicle()
# print(f"Vehicle with Maximum Maintenance Cost: {max_maintenance_vehicle}")

#  ===================================================================================================================================

# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self): #getter method- to access value of particular attribute
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Name must be a string")
#         self._name = value

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("Age must be a non-negative integer")
#         self._age = value

 
# person = Person("John", 30)
# person.name = "Jane"
# print(person.name)  # person._name()





# try:
#     person.name = 123
# except TypeError as e:
#     print(e)  

 
# person.age = 25

 
# try:
#     person.age = -1
# except ValueError as e:
#     print(e)   

# =========================================================================================================================================

# from enum import Enum

# # Define Enum for Vehicle Types
# class VehicleType(Enum):
#     CAR = "Car"
#     TRUCK = "Truck"
#     MOTORCYCLE = "Motorcycle"

# class VehicleRecords:
#     def __init__(self):
#         self.vehicles = {}
#         self.fuel_types = ["Gasoline", "Diesel", "Electric"]
#         self.transmission_types = ["Automatic", "Manual"]

#     def add_vehicle(self, vehicle_type: VehicleType, make, model, year, fuel_type, transmission_type, mileage=0):
#         if not isinstance(vehicle_type, VehicleType):
#             raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")
        
#         vehicle_id = len(self.vehicles) + 1
#         self.vehicles[vehicle_id] = {
#             "vehicle_type": vehicle_type.value,  # Store the string value
#             "make": make,
#             "model": model,
#             "year": year,
#             "fuel_type": fuel_type,
#             "transmission_type": transmission_type,
#             "mileage": mileage,
#             "maintenance_records": []
#         }
#         print(f"Vehicle added with ID: {vehicle_id}")

#     def remove_vehicle(self, vehicle_id):
#         if vehicle_id in self.vehicles:
#             del self.vehicles[vehicle_id]
#             print(f"Vehicle with ID {vehicle_id} removed")
#         else:
#             print(f"Vehicle with ID {vehicle_id} not found")

#     def update_vehicle(self, vehicle_id, make=None, model=None, year=None, fuel_type=None, transmission_type=None, mileage=None):
#         if vehicle_id in self.vehicles:
#             if make:
#                 self.vehicles[vehicle_id]["make"] = make
#             if model:
#                 self.vehicles[vehicle_id]["model"] = model
#             if year:
#                 self.vehicles[vehicle_id]["year"] = year
#             if fuel_type:
#                 self.vehicles[vehicle_id]["fuel_type"] = fuel_type
#             if transmission_type:
#                 self.vehicles[vehicle_id]["transmission_type"] = transmission_type
#             if mileage:
#                 self.vehicles[vehicle_id]["mileage"] = mileage
#             print(f"Vehicle with ID {vehicle_id} updated")
#         else:
#             print(f"Vehicle with ID {vehicle_id} not found")

#     def get_vehicle_info(self, vehicle_id):
#         return self.vehicles.get(vehicle_id, None)

#     def drive_vehicle(self, vehicle_id, miles):
#         if vehicle_id in self.vehicles:
#             self.vehicles[vehicle_id]["mileage"] += miles
#             print(f"Vehicle with ID {vehicle_id} driven for {miles} miles")
#         else:
#             print(f"Vehicle with ID {vehicle_id} not found")

#     def perform_maintenance(self, vehicle_id, maintenance_type, description):
#         if vehicle_id in self.vehicles:
#             self.vehicles[vehicle_id]["maintenance_records"].append({
#                 "maintenance_type": maintenance_type,
#                 "description": description
#             })
#             print(f"Maintenance performed on Vehicle with ID {vehicle_id}")
#         else:
#             print(f"Vehicle with ID {vehicle_id} not found")

#     def display_all_vehicles(self):
#         for vehicle_id, vehicle_info in self.vehicles.items():
#             print(f"Vehicle ID: {vehicle_id}")
#             print(f"Vehicle Type: {vehicle_info['vehicle_type']}")
#             print(f"Make: {vehicle_info['make']}")
#             print(f"Model: {vehicle_info['model']}")
#             print(f"Year: {vehicle_info['year']}")
#             print(f"Fuel Type: {vehicle_info['fuel_type']}")
#             print(f"Transmission Type: {vehicle_info['transmission_type']}")
#             print(f"Mileage: {vehicle_info['mileage']}")
#             print(f"Maintenance Records: {vehicle_info['maintenance_records']}")
#             print("--------------------")

#     def filter_vehicles_by_type(self, vehicle_type: VehicleType):
#         if not isinstance(vehicle_type, VehicleType):
#             raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")
        
#         filtered_vehicles = {
#             vehicle_id: vehicle_info
#             for vehicle_id, vehicle_info in self.vehicles.items()
#             if vehicle_info["vehicle_type"] == vehicle_type.value
#         }
#         return filtered_vehicles

# # Example Usage
# vehicle_records = VehicleRecords()

# # Add vehicles using Enum
# vehicle_records.add_vehicle(VehicleType.CAR, "Toyota", "Corolla", 2015, "Gasoline", "Automatic", 50000)
# vehicle_records.add_vehicle(VehicleType.TRUCK, "Ford", "F-150", 2018, "Diesel", "Manual", 30000)
# vehicle_records.add_vehicle(VehicleType.MOTORCYCLE, "Honda", "CBR500R", 2020, "Gasoline", "Manual", 10000)

# # Display all vehicles
# vehicle_records.display_all_vehicles()

# # Filter by Enum type
# filtered_vehicles = vehicle_records.filter_vehicles_by_type(VehicleType.CAR)
# print("Filtered Vehicles by Type:")
# for vehicle_id, vehicle_info in filtered_vehicles.items():
#     print(vehicle_info)
 

# ====================================================================================================================================================================

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
 
# ====================================================================================================================================