from unittest import TestCase
import os.path

from Common.Point import Point
from Engine.Common.GameState import GameState
from Engine.Common.PlayerState import PlayerState
from Engine.GameEngine import PlayerEngine
from Map.MapHolder import MapHolder
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider


class TestPlayerEngine(TestCase):
    def setUp(self):
        self._RealPath = os.path.join(os.path.dirname(__file__), '..\\..\\Maps\\TestMap.csv')
        self._ConfigProvider = UnitTestDummyConfigProvider()
        self._ConfigProvider.addValue('Game.MovementDefinations', 'maximumAllowedPath', '3')

    def test_Creation(self):
        path = self._RealPath
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)

        gamestate=GameState(10,1,2)
        engine=PlayerEngine.PlayerEngine(gamestate,self._ConfigProvider,holder)
        self.assertTrue(engine.GetGameState().MyPlayer.id==1)
        self.assertTrue(engine.GetGameState().EnemyPlayer.id == 2)

    def test_Update_GameState(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)

        gamestate = GameState(10, 1, 2)
        engine = PlayerEngine.PlayerEngine( gamestate, self._ConfigProvider, holder)
        self.assertTrue(engine.GetGameState().MyPlayer.position.x == 0)
        self.assertTrue(engine.GetGameState().EnemyPlayer.position.x==0)
        self.assertTrue(engine.GetGameState().playingtime==0)
        gamestate.playingtime=100
        gamestate.MyPlayer.position=Point(10,10)
        gamestate.EnemyPlayer.position = Point(20, 20)
        self.assertTrue(engine.GetGameState().MyPlayer.position.x == 10)
        self.assertTrue(engine.GetGameState().EnemyPlayer.position.x == 20)
        self.assertTrue(engine.GetGameState().playingtime == 100)


    def test_Movement_Success(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)

        gamestate = GameState(10, 1, 2)
        engine = PlayerEngine.PlayerEngine( gamestate, self._ConfigProvider, holder)
        PointFrom = Point(0, 0)
        PointTo = Point(1, 2)
        self.assertTrue(engine.MayIMove(PointTo))
        self.assertTrue(engine.MayMoveBetweenPoints(PointFrom,PointTo))

    def test_Movement_Fail(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)

        gamestate = GameState(10, 1, 2)

        self._ConfigProvider.addValue('Game.MovementDefinations', 'maximumAllowedPath', '1')
        engine = PlayerEngine.PlayerEngine( gamestate, self._ConfigProvider, holder)
        PointFrom = Point(0, 0)
        PointTo = Point(3,3)
        self.assertFalse(engine.MayIMove(PointTo))
        self.assertFalse(engine.MayMoveBetweenPoints(PointFrom, PointTo))

    def test_Los_Success(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        gamestate = GameState(10, 1, 2)

        gamestate.MyPlayer.position = Point(1, 1);

        gamestate.EnemyPlayer.position=Point(8,1)

        engine = PlayerEngine.PlayerEngine(gamestate, self._ConfigProvider, holder)
        self.assertTrue(engine.IsLosToEnemy())
        self.assertTrue(engine.IsLosFromMeToPoint(Point(6,1)))
        p1 = Point(3, 4);
        p2 = Point(6, 5);
        self.assertTrue(engine.IsLosBetweenPoints(p1,p2))

    def test_Los_Fail(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        gamestate = GameState(10, 1, 2)

        gamestate.MyPlayer.position = Point(1, 1);
        gamestate.EnemyPlayer.position = Point(1, 3)

        engine = PlayerEngine.PlayerEngine(gamestate, self._ConfigProvider, holder)
        self.assertFalse(engine.IsLosToEnemy())
        self.assertFalse(engine.IsLosFromMeToPoint(Point(1, 4)))
        p1 = Point(2, 1);
        p2 = Point(6, 5);
        self.assertFalse(engine.IsLosBetweenPoints(p1, p2))



