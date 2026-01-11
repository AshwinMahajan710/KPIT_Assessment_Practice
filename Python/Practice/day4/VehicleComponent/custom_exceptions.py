
# custom exception for engine overheating
class EngineOverheatException(Exception):
    def __init__(self, message= "Engine cannot exceed temperature of 150c"):
        super().__init__(message)

# custom exception for handling brake failure issues
class BrakeFailureException(Exception):
    def __init__(self, message="Brake values are not as per instructed"):
        super().__init__(message)
