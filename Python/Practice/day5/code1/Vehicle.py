from Exceptions import InvalidArgumentException, InvalidDatatypeException
from Vehicle_Types import VehicleType

# class vehicle --> which contains details of vehicle
class Vehicle():

    # constructor
    def __init__(self, vehicle_id: int, make: str, model: str, price: float, vehicle_type: VehicleType, fuel_type: str, transmission_type: str, mileage: int | float):

        # Handling exceptions
        if not isinstance(vehicle_id, int):
            raise InvalidDatatypeException(f"For vehicle Id: Expected int, got {type(vehicle_id)}")
        if not isinstance(make, str):
            raise InvalidDatatypeException(f"For make: Expected string, got {type(make)}")
        if not isinstance(model, str):
            raise InvalidDatatypeException(f"For model: Expected string, got {type(model)}")
        if not isinstance(price, (int,float)):
            raise InvalidDatatypeException(f"For Price: Expected int or float, got {type(price)}")
        if not isinstance(vehicle_type, VehicleType):
            raise InvalidDatatypeException(f"For Vehicle_type: Expected 'VehicleType', got {type(vehicle_type)}")
                
        # Handling invalid arguments for price and vehicle_id
        if(vehicle_id<0):
            vehicle_id = 0
            raise InvalidArgumentException(f"Vehicle Id can never be -ve:")
        if(price<0):
            price = 0
            raise InvalidArgumentException(f"Price can never be -ve")
        if (mileage<0):
            mileage = 0
            raise InvalidArgumentException(f"mileage can never be -ve")
        
        # After validation assign values
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.price = price
        self.vehicle_type = vehicle_type
        self.fuel_type = fuel_type 
        self.transmission_type = transmission_type
        self.mileage = mileage

    # To print information of obj
    def __repr__(self):
        return f"Vehicle({self.__dict__})"        