from Vehicle_Type import VehicleType
from VehicleRecords import VehicleRecords

vehicle_records = VehicleRecords()

vehicle_records.add_vehicle(VehicleType.CAR, "Toyota", "Corolla", 2015, "Gasoline", "Automatic", 50000)
vehicle_records.add_vehicle(VehicleType.TRUCK, "Ford", "F-150", 2018, "Diesel", "Manual", 30000)
vehicle_records.add_vehicle(VehicleType.MOTORCYCLE, "Honda", "CBR500R", 2020, "Gasoline", "Manual", 10000)

vehicle_records.display_all_vehicles()

filtered = vehicle_records.filter_vehicles_by_type(VehicleType.CAR)
print(filtered)