from BatteryPack import BatteryPack
from BatteryType import BatteryType
from exceptions import InvalidArgumentException, InvalidTypeException
from EVCar import EVCar
from typing import Dict, List, Any
from operations import display_details, add_new_ev_car_record, replace_battery_pack, find_max_battery_capacity
import re

# main function
def main():

    # Trying to add normal one --> success
    add_new_ev_car_record("MH15CD1234",4,12345,"12345",BatteryType(0))

    # Try to add faulty one
    try:
        add_new_ev_car_record("MH15CD1234",-3,12345,"12345",BatteryType(0))
    except InvalidArgumentException as e:
        print("Invalid argument: ",e)
    except InvalidTypeException as e:
        print("Invalid Type: ",e)

    # Try to add normal one
    add_new_ev_car_record("MH11CD5634",4,1235,"12345",BatteryType(0))
    add_new_ev_car_record("MH19CD5634",4,123567,"12345",BatteryType(0))

    # function to display details--> success
    print("\nDisplaying all car details: ")
    display_details()

    # FUNCTION TO REPLACE BATTERYPACK
    replace_battery_pack("MH11CD5634",BatteryPack("12345",BatteryType(1)))

    # function to display details--> success
    print("\nDisplaying all car details: ")
    display_details()

    # function to get car with max_price
    print("Car with highest price is: ",find_max_battery_capacity())
    
if __name__=="__main__":
    main()