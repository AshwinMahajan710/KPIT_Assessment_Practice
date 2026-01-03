# custom exception to handle invalid data types
class InvalidDatatypeException(Exception):
    def __init__(self, message: str = "Invalid data type provide.. please try again"):
        super.__init__(message)

# custom exception to handle invalid arguments
class InvalidArgumentException(Exception):
    def __init__(self, message: str = "Invalid argument provide.. please try again"):
        super.__init__(message)


