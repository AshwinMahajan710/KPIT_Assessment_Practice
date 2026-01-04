from BatteryType import BatteryType
from exceptions import InvalidTypeException, InvalidArgumentException

# class BatteryPack
class BatteryPack:

    # constructor
    def __init__(self, serial_no: str, battery_pack_type: BatteryType):

        # Validation for batteryType
        if not isinstance(battery_pack_type, BatteryType):
            InvalidTypeException(f"Expected type \"BatteryType\", got {type(battery_pack_type)}")
        
        # validtion of serial_no values
        if len(serial_no) == 0:
            InvalidArgumentException(f"Id can never be null")

        # Assign attributes
        self.battery_pack_serial_number: str = serial_no # which is a non-zero length string
        self.battery_pack_type: BatteryType = battery_pack_type # which is either LI_ION or NI_CAD
    
    # Printing the details
    def __repr__(self):
        return f"{self.__dict__}"