from unittest import TestCase
from Common.Point import Point
from Common.PathResult import PathResult
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider
import os.path
import sys
from Map.MapHolder import MapHolder
from Common.Constant import Constants
from Common.PointsControl import PointsControl

class TestMapHolder(TestCase):
    def setUp(self):
        self._RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap/Map.csv')
        self._SimpleRealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestSimpleMap/Map.csv')
        self._NotRealPath = os.path.join(os.path.dirname(__file__), '../Maps/NoMap/Map.csv')
        self._NoControllingPointsMap = os.path.join(os.path.dirname(__file__), '../Maps/NoControllingPointsMap/Map.csv')

        self._ConfigProvider=UnitTestDummyConfigProvider()
        self._ConfigProvider.addValue('Game.MovementDefinations','maximumAllowedPath','3')
        self._Consts=Constants()
    #region Loading
    def test_mapLoaded__FullPath_True(self):
        path = self._RealPath
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.mapLoaded, "error")
        self.assertTrue(holder.graphLoaded, "error")

    def test_mapLoaded_GetDim_Loaded(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        dim=holder.getMapDim()
        self.assertTrue(dim.width==10, "error")
        self.assertTrue(dim.height == 10, "error")

    def test_mapLoaded_False(self):
        path = self._NotRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertFalse(holder.mapLoaded, "error")

    def test_mapLoaded_GetDim_Not_Loaded(self):
        path = self._NotRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.getMapDim().width == 0, "error")
        self.assertTrue(holder.getMapDim().height == 0, "error")

    def test_mapLoaded_GraphLoaded_Not_Loaded(self):
        path = self._NotRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertFalse(holder.graphLoaded, "error")
    #endregion

    #region Graph Creation
    def test_mapLoaded_GraphLoaded_WithDraw(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        holder.drawGraph()
        self.assertTrue(holder.graphLoaded, "error")

    def test_mapLoaded_GraphLoaded_Loaded(self):
        path = self._RealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.graphLoaded, "error")
    #endregion

    #region MayMove

    def test_mapLoaded_MayMove_Success(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom=Point(0,0)
        PointTo = Point(1, 1)
        may=holder.mayMove(PointFrom,PointTo)

        self.assertTrue(may, "error")

    def test_mapLoaded_MayMove_Success_LongPath(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom=Point(0,0)
        PointTo = Point(1, 2)
        may=holder.mayMove(PointFrom,PointTo)

        self.assertTrue(may, "error")

    def test_mapLoaded_MayMove_Failure_OutOfBounds_X(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(-1, 0)
        PointTo = Point(1, 1)
        may = holder.mayMove(PointFrom, PointTo)
        self.assertFalse(may, "error")

    def test_mapLoaded_MayMove_Failure_OutOfBounds_Y(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 900)
        PointTo = Point(1, 1)
        may = holder.mayMove(PointFrom, PointTo)
        self.assertFalse(may, "error")

    def test_mapLoaded_MayMove_Fail_Too_LongDistance(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 0)
        PointTo = Point(2, 2)
        self._ConfigProvider.addValue('Game.MovementDefinations', 'maximumAllowedPath', '1')
        may = holder.mayMove(PointFrom, PointTo)

        self.assertFalse(may, "error")

    def test_mapLoaded_MayMove_Fail_UnReachable(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 0)
        PointTo = Point(3, 3)
        self._ConfigProvider.addValue('Game.MovementDefinations', 'maximumAllowedPath', '1')
        may = holder.mayMove(PointFrom, PointTo)

        self.assertFalse(may, "error")

    #endregion

    #region GetPath
    def test_mapLoaded_GetPath_Success(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 0)
        PointTo = Point(1, 1)
        path = holder.getPath(PointFrom, PointTo)

        self.assertTrue(path.valid, "error")

    def test_mapLoaded_GetPath_Success_LongPath(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 0)
        PointTo = Point(1, 2)
        path = holder.getPath(PointFrom, PointTo)

        self.assertTrue(path.valid, "error")

    def test_mapLoaded_GetPath_Success_LongPath_Draw(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 0)
        PointTo = Point(1, 2)
        path = holder.getPath(PointFrom, PointTo,draw=True)

        self.assertTrue(path.valid, "error")

    def test_mapLoaded_GetPath_Failure_OutOfBounds_X(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(-1, 0)
        PointTo = Point(1, 1)
        path = holder.getPath(PointFrom, PointTo)

        self.assertFalse(path.valid, "error")

    def test_mapLoaded_GetPath_Failure_OutOfBounds_Y(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 900)
        PointTo = Point(1, 1)
        path = holder.getPath(PointFrom, PointTo)

        self.assertFalse(path.valid, "error")

    def test_mapLoaded_GetPath_Fail_Too_LongDistance(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 0)
        PointTo = Point(2, 2)
        self._ConfigProvider.addValue('Game.MovementDefinations', 'maximumAllowedPath', '1')
        path = holder.getPath(PointFrom, PointTo)

        self.assertFalse(path.valid, "error")

    def test_mapLoaded_MayMove_Fail_UnReachable(self):
        path = self._SimpleRealPath
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        PointFrom = Point(0, 0)
        PointTo = Point(3, 3)
        self._ConfigProvider.addValue('Game.MovementDefinations', 'maximumAllowedPath', '1')
        path = holder.getPath(PointFrom, PointTo)

        self.assertFalse(path.valid, "error")
    #endregion

    # region Get Alt
    def test_GetAlt_Failed_1(self):
        path = self._RealPath
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.getAlt(Point(15,15))==self._Consts.InValidAlt, "error")
    def test_GetAlt_Failed_2(self):
        path = self._RealPath
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.getAlt(Point(-1,-1))==self._Consts.InValidAlt, "error")

    def test_GetAlt_Success_1(self):
        path = self._RealPath
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.getAlt(Point(0, 0)) ==1, "error")
    def test_GetAlt_Success_3(self):
        path = self._RealPath
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.getAlt(Point(4, 3)) == 3, "error")

    def test_GetAlt_Success_2(self):
        path = self._RealPath
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        self.assertTrue(holder.getAlt(Point(1, 2)) == 2, "error")

    # endregion

    # region Get Controlling_Points
    def test_Get_ControllingPoints_1(self):
        path = self._NoControllingPointsMap
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        cotrolledpoints=holder.pointscontrol
        controllingpointsLen=len(cotrolledpoints[1][1].controllingpoints)
        controlledpointsLen = len(cotrolledpoints[1][1].controlledpoints)

        self.assertTrue(controllingpointsLen == 0, "error")
        self.assertTrue(controlledpointsLen==8, "error")

    def test_Get_ControllingPoints_2(self):
        path = self._NoControllingPointsMap
        print(path)
        holder = MapHolder(self._ConfigProvider)
        holder.loadMap(path)
        cotrolledpoints=holder.pointscontrol;
        controllingpointsLen=len(cotrolledpoints[2][2].controllingpoints)
        controlledpointsLen = len(cotrolledpoints[2][2].controlledpoints)

        self.assertTrue(controllingpointsLen== 5, "error")
        self.assertTrue(controlledpointsLen==6, "error")
    #endregion

