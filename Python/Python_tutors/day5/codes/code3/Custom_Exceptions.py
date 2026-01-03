# custom exception for battery object

class InvalidBatteryObjectException(Exception):
    def __init__(self, given_type):
        super().__init__(f"Provided Type '{type(given_type)}', but should be of type 'Battery'")
