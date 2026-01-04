# - Create a global dictionary of EvCar objects :
# - key should be:  car_reg_id which is a string starting with "MH" of length 9 or 10

# - A function add_new_ev_car_record which take required parameters and create an instance of type sensor. This instance must be added to the global dictionary
#     [Use a helper function to validate data received]

# - A function replace_battery_pack.It 
#     - receives an object of type BatteryPack and car_reg_id 
#     - updates the global dictionary for that car_reg_id by replacing existing battery_pack with newly received data
#     - Throws exceptions if received battery_pack data or car_reg_id is invalid/not-found

# - A function find_max_battery_capacity_car which returns the first EvCar instance whose battery_capacity is the highest.

# - A function to check if car instances have car_battery_pack with battery_capacity above 50 or not

from BatteryPack import BatteryPack
from BatteryType import BatteryType
from exceptions import InvalidArgumentException, InvalidTypeException, NotFoundException
from EVCar import EVCar
from typing import Dict, List, Any, Optional
from functools import reduce
import re

cars : Dict[str,EVCar] = {} # key should be:  car_reg_id which is a string starting with "MH" of length 9 or 10

# Function to validate car registration id
def validate_car_reg_id(car_reg_id: str) -> None:
    if not car_reg_id:
        InvalidArgumentException("Car registration id not provided...")
    pattern = r"^[A-Za-z]{2}\s*\d{2}\s*[A-Za-z]\s*\d{3,4}"
    if not re.match(pattern,car_reg_id):
        InvalidArgumentException("Registration id validation failed")

# function to add new car record
def add_new_ev_car_record(car_reg_id:str,car_seat_count: int, car_price: int|float, battery_serial_no: str, battery_pack_type: BatteryType):

    # Validtion of 'Batterypack' and 'EVCar' will automatically happen in their respective classes
    battery_pack = BatteryPack(battery_serial_no, battery_pack_type)
    new_car = EVCar(car_seat_count, car_price, battery_pack)

    # Validate registration id
    validate_car_reg_id(car_reg_id)

    # now add this in dictionary
    cars[car_reg_id] = new_car
    print("Car added successfully")

# function to replace battery pack
def replace_battery_pack(car_reg_id: str, new_battery_pack: BatteryPack)->None:
    # first validate reg_id 
    validate_car_reg_id(car_reg_id)

    # if not found raise notfound exception
    if car_reg_id not in cars.keys():
        raise NotFoundException("Given car reg id not found")

    # now after all validations replace batterypack
    cars[car_reg_id].car_battery_pack = new_battery_pack
    print("Batterypack of car successfully changed")

# function to display information of all cars
def display_details():
    if len(cars.keys()) == 0:
        print("No records present")
    for reg_id in cars.keys():
        print("Car reg id: ",reg_id,": ",cars[reg_id])

# function to find car with max price
def find_max_battery_capacity() -> Optional[EVCar]:
    if len(cars.keys()) == 0:
        print("dictionary is empty")
        return None
    else:
        return reduce(lambda x,y: x if x.car_price > y.car_price else y, cars.values()) 
    
    
