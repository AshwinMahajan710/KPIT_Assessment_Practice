from typing import Dict, List, Any
from Vehicle_Types import VehicleType
from Vehicle import Vehicle
from Exceptions import InvalidArgumentException
from Vehicle_Records import VehicleRecords

def main():
    records = VehicleRecords()
    records.add_vehicle(VehicleType(1), 'Honda', "cb350", 5673.9, 'Gasoline', 'Manual', 1234)
    records.get_vehicle_info(1)

main()