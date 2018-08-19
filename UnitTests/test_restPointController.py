from unittest import TestCase
from Common.Point import Point
from Engine.Controllers.RestPointController import RestPointController
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider
import os.path
from Engine.Controllers.ControllersEnums import PlayerRestPointState
from Map.MapHolder import MapHolder

class TestRestPointController(TestCase):
    def setUp(self):

        self._ConfigProvider=UnitTestDummyConfigProvider()
        self._RealPath = os.path.join(os.path.dirname(__file__), '../Maps/ChallangeMap.csv')
        self._ConfigProvider.addValue('Game.MovementDefinations','maximumAllowedPath','3')
        self._ConfigProvider.addValue('RestPoint.Config', 'RestPointTimeToProfit', '3')
        self._ConfigProvider.addValue('RestPoint.Config', 'RestPointTimeToRegenerate', '5')

    def test_RestPointController_Load_End2End(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        restPointController=RestPointController(holder.restPointsLocations,self._ConfigProvider)
        self.assertTrue(len(restPointController.restpoints) == 4, "OK")

    def test_RestPointController_Load(self):
        restpointslocations=[]
        restpointslocations.append(Point(1,1))
        restpointslocations.append(Point(2, 2))
        restpointslocations.append(Point(3, 3))
        restpointslocations.append(Point(4, 4))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(len(restPointController.restpoints) == 4, "OK")

    def test_RestPointController_Empty(self):
        restpointslocations = []

        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(len(restPointController.restpoints) == 0, "OK")

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_NotOnPoint(self):
        restpointslocations=[]
        restpointslocations.append(Point(1,1))
        restpointslocations.append(Point(2, 2))
        restpointslocations.append(Point(3, 3))
        restpointslocations.append(Point(4, 4))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(5,5),10) == PlayerRestPointState.NOT_IN_RESTPOINT, "OK")

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_NotOnPoint_Empty(self):
        restpointslocations = []
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(5, 5),10) == PlayerRestPointState.NOT_IN_RESTPOINT,
                        "OK")

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_InPoint_NoReward(self):
        restpointslocations = []
        restpointslocations.append(Point(1,1))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       1) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_InPoint_NoReward_PointStateUpdated(self):
        restpointslocations = []
        restpointslocations.append(Point(1, 1))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       1) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")
        self.assertTrue(restPointController.restpoints[0].timetoregenerate==0)

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_InPoint_WithReward(self):
        restpointslocations = []
        restpointslocations.append(Point(1,1))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       5) == PlayerRestPointState.IN_REST_POINT_WITH_REWARD,
                        "OK")

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_InPoint_WithReward_PointStateUpdated(self):
        restpointslocations = []
        restpointslocations.append(Point(1, 1))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       5) == PlayerRestPointState.IN_REST_POINT_WITH_REWARD,
                        "OK")
        self.assertTrue(restPointController.restpoints[0].timetoregenerate==5)

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_InPoint_WithReward_PointStateUpdated_3Times(
            self):
        restpointslocations = []
        restpointslocations.append(Point(1, 1))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       5) == PlayerRestPointState.IN_REST_POINT_WITH_REWARD,
                        "OK")
        self.assertTrue(restPointController.restpoints[0].timetoregenerate == 5)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       6) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       7) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")
        self.assertTrue(restPointController.restpoints[0].timetoregenerate == 3)

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_InPoint_WithReward_2_Times(
            self):
        restpointslocations = []
        restpointslocations.append(Point(1, 1))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       5) == PlayerRestPointState.IN_REST_POINT_WITH_REWARD,
                        "OK")
        self.assertTrue(restPointController.restpoints[0].timetoregenerate == 5)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       6) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       7) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       8) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       9) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                       10) == PlayerRestPointState.IN_REST_POINT_WITH_REWARD,
                        "OK")

    def test_RestPointController_UpdateRestingPointStateAccordingToPosition_Movement(
            self):
        restpointslocations = []
        restpointslocations.append(Point(1, 1))
        restpointslocations.append(Point(2, 2))
        restPointController = RestPointController(restpointslocations, self._ConfigProvider)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(1, 1),
                                                                                      5) == PlayerRestPointState.IN_REST_POINT_WITH_REWARD,
                        "OK")
        self.assertTrue(restPointController.restpoints[0].timetoregenerate == 5)
        self.assertTrue(restPointController.UpdateRestingPointStateAccordingToPosition(Point(2, 2),
                                                                                       1) == PlayerRestPointState.IN_REST_POINT_NO_REWARD,
                        "OK")

        self.assertTrue(restPointController.restpoints[0].timetoregenerate == 4)
        self.assertTrue(restPointController.restpoints[1].timetoregenerate == 0)



