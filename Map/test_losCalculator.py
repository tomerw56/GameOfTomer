from unittest import TestCase
from Map.LosCalculator import LosCalculator
from Map.CSVMatrixReader import CSVMatrixReader
from Common.Point import Point
import os.path
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider

class TestLosCalculator(TestCase):
    def setUp(self):
          self._ConfigProvider = UnitTestDummyConfigProvider()

    def test_IsLos_Success_Short(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(1, 1);
        p2 = Point(8, 1);
        calc=LosCalculator(  self._ConfigProvider)
        isLos=calc.IsLos(p1,p2,csvreader.Matrix)
        self.assertTrue(isLos)
    def test_IsLos_Fail_Short(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(1, 1);
        p2 = Point(1, 3);
        calc=LosCalculator(  self._ConfigProvider)
        isLos=calc.IsLos(p1,p2,csvreader.Matrix)
        self.assertFalse(isLos)
    def test_IsLos_Success_Diagonal(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(3, 4);
        p2 = Point(6, 5);
        calc=LosCalculator(  self._ConfigProvider)
        isLos=calc.IsLos(p1,p2,csvreader.Matrix)
        self.assertTrue(isLos)

    def test_IsLos_Fail_Diagonal(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(2, 1);
        p2 = Point(6, 5);
        calc = LosCalculator(self._ConfigProvider)
        isLos = calc.IsLos(p1, p2, csvreader.Matrix)
        self.assertFalse(isLos)
