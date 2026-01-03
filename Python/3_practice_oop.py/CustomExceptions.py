# custom class for handling invalid datatype passed exception
class InvalidDataTypeException(Exception):
    def __init__(self, message="Invalid data type passed. Please check inputs"):
        super().__init__(message)
