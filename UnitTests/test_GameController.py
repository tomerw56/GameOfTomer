from unittest import TestCase
from Engine.Controllers.GameController import GameController
from unittest import TestCase
from Common.Point import Point
from UnitTests.UnitTest_PlayerFacade.NoMovePlayerFacade import NoMovePlayerFacade
from UnitTests.UnitTest_PlayerFacade.EvadingPlayerFacade import EvadingPlayerFacade
from UnitTests.UnitTest_PlayerFacade.ExceptionThrowingPlayerFacade import ExceptionThrowingPlayerFacade
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider
import os.path
from Engine.Common.Facade.Enums import WinnigPlayer
from Engine.Common.Facade.Enums import WinnigReason
from Engine.Common.Facade.PlayerEngineFacade import PlayrerEngineFacade
from Engine.Common.Facade.VictoryAnalysis import VictoryAnalysis
from Engine.Common.PlayerState import PlayerState
from Map.MapHolder import MapHolder
from time import sleep

class test_GameController(TestCase):
    def setUp(self):
        self._RealPath = os.path.join(os.path.dirname(__file__), '../Maps/ChallangeMap.csv')
        self._MovingPath = os.path.join(os.path.dirname(__file__), '../Maps/SimpleMovingMap.csv')
        self._ConfigProvider = UnitTestDummyConfigProvider()
        self._ConfigProvider.addValue('Game.Config', 'MapFileName',self._RealPath)
        self._ConfigProvider.addValue('Game.MovementDefinations', 'maximumAllowedPath', '3')
        self._ConfigProvider.addValue('RestPoint.Config', 'RestPointTimeToProfit', '3')
        self._ConfigProvider.addValue('RestPoint.Config', 'RestPointTimeToRegenerate', '5')
        self._ConfigProvider.addValue('Game.Config','TotalPlayTime', '20')
        self._ConfigProvider.addValue('Player1.Config','StartPositionX','9')
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionY', '9')
        self._ConfigProvider.addValue('Player2.Config', 'StartPositionX', '0')
        self._ConfigProvider.addValue('Player2.Config', 'StartPositionY', '0')
        self._ConfigProvider.addValue('Threat.Config', 'ThreatTimeOut', '3')
        self._ConfigProvider.addValue('Threat.Config', 'ThreatAltDiff', '1')
        self._ConfigProvider.addValue('Recording', 'record', 'True')
        self._ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')

    def test_GameController_Load(self):
        sleep(2)  # Time in seconds.
        playerfacade1=NoMovePlayerFacade()
        playerfacade2=NoMovePlayerFacade()
        gamecontroller = GameController(self._ConfigProvider,playerfacade1,playerfacade2)
        self.assertTrue(gamecontroller.valid, "OK")

    def test_GameController_SimpleRun_NoWinner(self):
        sleep(2)  # Time in seconds.
        playerfacade1=NoMovePlayerFacade()
        playerfacade2=NoMovePlayerFacade()
        gamecontroller = GameController(self._ConfigProvider,playerfacade1,playerfacade2)
        gamecontroller.Run()
        self.assertTrue(gamecontroller.VictoryReason.winningireason==WinnigReason.GAME_TIME_OUT, "OK")
        self.assertTrue(gamecontroller.VictoryReason.winner==WinnigPlayer.NO_WINNER, "OK")

    def test_GameController_SimpleRun_Destruction(self):
        sleep(2)  # Time in seconds.
        playerfacade1 = NoMovePlayerFacade()
        playerfacade2 = NoMovePlayerFacade()
        # SetPlayer 1 To threatposition
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionX', '2')
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionY', '2')
        gamecontroller = GameController(self._ConfigProvider, playerfacade1, playerfacade2)
        gamecontroller.Run()
        self.assertTrue(gamecontroller.VictoryReason.winningireason == WinnigReason.DESTRUCTION, "OK")
        self.assertTrue(gamecontroller.VictoryReason.winner == WinnigPlayer.PLAYER_1, "OK")

    def test_GameController_SimpleRun_Score(self):
        sleep(2)  # Time in seconds.
        playerfacade1 = NoMovePlayerFacade()
        playerfacade2 = NoMovePlayerFacade()
        # SetPlayer 1 To threatposition
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionX', '7')
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionY', '3')
        gamecontroller = GameController(self._ConfigProvider, playerfacade1, playerfacade2)
        gamecontroller.Run()
        self.assertTrue(gamecontroller.VictoryReason.winningireason == WinnigReason.SCORE, "OK")
        self.assertTrue(gamecontroller.VictoryReason.winner == WinnigPlayer.PLAYER_1, "OK")
    def test_GameController_SimpleRun_Score_Chack(self):
        sleep(2)  # Time in seconds.
        playerfacade1 = NoMovePlayerFacade()
        playerfacade2 = NoMovePlayerFacade()
        # SetPlayer 1 To threatposition
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionX', '7')
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionY', '3')
        self._ConfigProvider.addValue('Game.Config', 'TotalPlayTime', '10')
        self._ConfigProvider.addValue('RestPoint.Config', 'RestPointTimeToProfit', '3')
        self._ConfigProvider.addValue('RestPoint.Config', 'RestPointTimeToRegenerate', '5')
        gamecontroller = GameController(self._ConfigProvider, playerfacade1, playerfacade2)
        gamecontroller.Run()
        self.assertTrue(gamecontroller.Player_1_State.score == 3, "OK")


    def test_GameController_Exception(self):
        sleep(2)  # Time in seconds.
        playerfacade1 = NoMovePlayerFacade()
        playerfacade2 = ExceptionThrowingPlayerFacade(4)
        gamecontroller = GameController(self._ConfigProvider, playerfacade1, playerfacade2)
        gamecontroller.Run()
        self.assertTrue(gamecontroller.VictoryReason.winningireason == WinnigReason.PLAYER_2_CRASH, "OK")
        self.assertTrue(gamecontroller.VictoryReason.winner == WinnigPlayer.PLAYER_1, "OK")


    def test_GameController_TestState(self):
        sleep(2)  # Time in seconds.
        playerfacade1 = NoMovePlayerFacade()
        playerfacade2 = NoMovePlayerFacade()
        gamecontroller = GameController(self._ConfigProvider, playerfacade1, playerfacade2)
        gamecontroller.Run()
        gamestate1 = playerfacade1.MyEngine.GetGameState()
        gamestate2=playerfacade2.MyEngine.GetGameState()
        self.assertTrue(playerfacade1.MyEngine.Dimensions.width == 10, "OK")
        self.assertTrue(playerfacade1.MyEngine.Dimensions.height == 10, "OK")
        self.assertTrue(gamestate1.MyPlayer.timeinposition == 20, "OK")
        self.assertTrue(gamestate1.EnemyPlayer.timeinposition == 20, "OK")
        self.assertTrue(gamestate1.playingtime==20, "OK")

        self.assertTrue(gamestate2.MyPlayer.timeinposition == 20, "OK")
        self.assertTrue(gamestate2.EnemyPlayer.timeinposition == 20, "OK")
        self.assertTrue(gamestate2.playingtime == 20, "OK")

    def test_GameController_Threatend(self):
        sleep(2)  # Time in seconds.
        self._ConfigProvider.addValue('Game.Config', 'MapFileName', self._MovingPath)
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionX', '0')
        self._ConfigProvider.addValue('Player1.Config', 'StartPositionY', '0')
        self._ConfigProvider.addValue('Player2.Config', 'StartPositionX', '3')
        self._ConfigProvider.addValue('Player2.Config', 'StartPositionY', '3')
        playerfacade1 = NoMovePlayerFacade()
        playerfacade2 = EvadingPlayerFacade()
        gamecontroller = GameController(self._ConfigProvider, playerfacade1, playerfacade2)
        gamecontroller.Run()

        self.assertTrue(playerfacade2.Evades>0, "OK")

