from unittest import TestCase
import os.path
import sys
from Map.MapHolder import MapHolder


class TestMapHolder(TestCase):
    def setUp(self):
        self._RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap.csv')
        self._NotRealPath = os.path.join(os.path.dirname(__file__), '../Maps/NoMap.csv')
    def test_mapLoaded_True(self):
        path= self._RealPath
        print(path)
        holder =MapHolder()
        holder.loadMap(path)
        self.assertTrue(holder.mapLoaded, "error")

    def test_mapLoaded_GetDim_Loaded(self):
        path = self._RealPath

        holder = MapHolder()
        holder.loadMap(path)
        dim=holder.getMapDim()
        print (dim.getString())
        self.assertTrue(dim.width==10, "error")
        self.assertTrue(dim.height == 10, "error")

    def test_mapLoaded_GraphLoaded_Loaded(self):
        path = self._RealPath
        holder = MapHolder()
        holder.loadMap(path)
        self.assertTrue(holder.graphLoaded, "error")

    def test_mapLoaded_False(self):
        path= self._NotRealPath
        holder =MapHolder()
        holder.loadMap(path)
        self.assertFalse(holder.mapLoaded, "error")

    def test_mapLoaded_GetDim_Not_Loaded(self):
        path = self._NotRealPath
        holder = MapHolder()
        holder.loadMap(path)
        self.assertTrue(holder.getMapDim().width == 0, "error")
        self.assertTrue(holder.getMapDim().height == 0, "error")

    def test_mapLoaded_GraphLoaded_Not_Loaded(self):
        path = self._NotRealPath
        holder = MapHolder()
        holder.loadMap(path)
        self.assertFalse(holder.graphLoaded, "error")


