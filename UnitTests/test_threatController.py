from unittest import TestCase
from Engine.Controllers.ThreatController import ThreatController
from unittest import TestCase
from Common.Point import Point

from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider
import os.path
from Engine.Controllers.ControllersEnums import PlayerThreatState
from Engine.Common.PlayerState import PlayerState
from Map.MapHolder import MapHolder

class test_threatController(TestCase):
    def setUp(self):

        self._ConfigProvider=UnitTestDummyConfigProvider()
        self._RealPath = os.path.join(os.path.dirname(__file__), '../Maps/ChallangeMap/Map.csv')
        self._ConfigProvider.addValue('Game.MovementDefinations','maximumAllowedPath','3')
        self._ConfigProvider.addValue('Threat.Config', 'ThreatTimeOut', '3')
        self._ConfigProvider.addValue('Threat.Config', 'ThreatAltDiff', '1')
        self._ConfigProvider.addValue('Game.Config', 'DrawMapHolderGraph','False')

    def test_ThreatController_Threat(self):
        path = self._RealPath
        p1 = Point(3, 4)
        p2 = Point(6, 5)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        threatController=ThreatController(holder,self._ConfigProvider)
        playerstate1=PlayerState(1)
        playerstate1.position=p1
        playerstate2 = PlayerState(2)
        playerstate2.position = p2
        self.assertTrue(threatController.GetPlayerThreatState(playerstate1,playerstate2)==PlayerThreatState.THREATENED, "OK")

    def test_ThreatController_NotThreat(self):
        path = self._RealPath
        p1 = Point(6, 4)
        p2 = Point(6, 6)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        threatController=ThreatController(holder,self._ConfigProvider)
        playerstate1=PlayerState(1)
        playerstate1.position=p1
        playerstate2 = PlayerState(2)
        playerstate2.position = p2
        self.assertTrue(threatController.GetPlayerThreatState(playerstate1,playerstate2)==PlayerThreatState.NOT_THREATENED, "OK")

    def test_ThreatController_Destroryed(self):
        path = self._RealPath
        p1 = Point(3, 4)
        p2 = Point(6, 5)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        threatController = ThreatController(holder, self._ConfigProvider)
        playerstate1 = PlayerState(1)
        playerstate1.position = p1
        playerstate1.threateningTime=5
        playerstate2 = PlayerState(2)
        playerstate2.position = p2
        playerstate2.threatenedTime=5
        self.assertTrue(
            threatController.GetPlayerThreatState(playerstate1, playerstate2) == PlayerThreatState.DESTROYED, "OK")