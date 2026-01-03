from enum import Enum, auto

class EngineType(Enum):
    PETROL = auto()
    DIESEL = auto()
    HYBRID = auto()

class Status(Enum):
    SOLD = auto()
    Available = auto()
    MAINTAINACE = auto()