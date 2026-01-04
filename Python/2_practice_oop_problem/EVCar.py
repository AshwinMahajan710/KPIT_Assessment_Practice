from BatteryPack import BatteryPack
from exceptions import InvalidTypeException, InvalidArgumentException

# class EVCar
class EVCar:

    # constructor
    def __init__(self, car_seat_count: int, car_price: int|float, car_battery_pack: BatteryPack):
        
        # Type validation
        if not isinstance(car_seat_count, int):
            raise InvalidTypeException(f"Expected int, Got {type(car_seat_count)}")
        if not isinstance(car_price, (int,float)):
            raise InvalidTypeException(f"Expected int or float, Got {type(car_price)}")
        if not isinstance(car_battery_pack, BatteryPack):
            raise InvalidTypeException(f"Expected \"BatteryType\", Got {type(car_battery_pack)}")

        # Values Validation
        if(car_seat_count <= 0):
            raise InvalidArgumentException("Car seat count can never be less than on equal to 0")
        if(car_price <= 0):
            raise InvalidArgumentException("Car price can never be less than on equal to 0")
        if(car_battery_pack is None):
            raise InvalidArgumentException("Battery pack can never be null")

        # After validation assign values
        self.car_seat_count: int = car_seat_count # which is an integer (must be positive non-zero value)
        self.car_price: int| float = car_price  # which is a non-zero, positive integer
        self.car_battery_pack: BatteryPack  = car_battery_pack # which is an instance of type BatteryPack (must NOT BE NULL)
    
    # To print details 
    def __repr__(self):
        return f"EVCar( {self.__dict__} )"

    