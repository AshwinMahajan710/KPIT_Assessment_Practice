# Represents individual battery cells with 5 attributes (including Enums)
from enums import BatteryStatus, BatteryType
from CustomExceptions import InvalidDataTypeException

class Battery:
    def __init__(self, battery_id: int, battery_type: BatteryType, status: BatteryStatus, voltage: float, temperature: float):
        if not isinstance(battery_id, int):
            raise InvalidDataTypeException("battery_id must be int")

        if not isinstance(battery_type, BatteryType):
            raise InvalidDataTypeException("battery_type must be BatteryType")

        if not isinstance(status, BatteryStatus):
            raise InvalidDataTypeException("status must be BatteryStatus")

        if not isinstance(voltage, (int, float)):
            raise InvalidDataTypeException("voltage must be numeric")

        if not isinstance(temperature, (int, float)):
            raise InvalidDataTypeException("temperature must be numeric")

        self.battery_id = battery_id
        self.battery_type = battery_type
        self.status = status
        self.voltage = float(voltage)
        self.temperature = float(temperature)
        
    def __repr__(self):
        return f"Object Info: {self.__dict__}"