from enum import Enum
class WinnigReason(Enum):
    NO_WIN = 1
    GAME_TIME_OUT = 2
    DESTRUCTION = 3
    PLAYER_1_CRASH = 4
    PLAYER_2_CRASH = 5,
    SCORE=6
class WinnigPlayer(Enum):
    NO_WINNER = 1
    PLAYER_1 = 2
    PLAYER_2 = 3
    BOTH_DESTROYED = 4

