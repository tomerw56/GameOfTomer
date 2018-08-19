from enum import Enum
class PlayerRestPointState(Enum):
    NOT_IN_RESTPOINT = 1
    IN_REST_POINT_NO_REWARD = 2
    IN_REST_POINT_WITH_REWARD = 3

class PlayerThreatState(Enum):
    NOT_THREATENED = 1
    THREATENED = 2
    DESTROYED=3