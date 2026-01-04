
#  custom exception for Invalid Type
class InvalidTypeException(Exception):
    def __init__(self, message = "Invalid type passed... please pass appropriate type "):
        super().__init__(message)

#  custom exception for Invalid Type
class InvalidArgumentException(Exception):
    def __init__(self, message = "Invalid Attributes passed... please pass appropriate attributes "):
        super().__init__(message)

# custom exception if not found something
class NotFoundException (Exception):
    def __init__(self, message = "Given object not found "):
        super().__init__(message)
