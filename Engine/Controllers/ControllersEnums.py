from enum import Enum

class PlayerThreatState(Enum):
    NOT_THREATENED = 1
    THREATENED = 2
    DESTROYED=3

class PlayerNoMovmentState(Enum):
    OK = 1
    STATIC_TIMEOUT = 2
