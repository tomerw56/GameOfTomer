from unittest import TestCase
from Engine.Common.Facade.Enums import WinnigReason
from Engine.Common.Facade.Enums import WinnigPlayer

class TestEnums(TestCase):
    def test_WinningReason(self):
        for name, attr in WinnigReason.__members__.items():
            print(attr.value)

        reason=WinnigReason.GAME_TIME_OUT
        self.assertTrue(reason==WinnigReason.GAME_TIME_OUT)
    def test_WinningPlayer(self):
        for name, attr in WinnigPlayer.__members__.items():
            print(attr.value)

        player=WinnigPlayer.PLAYER_1
        self.assertTrue(player==WinnigPlayer.PLAYER_1)
