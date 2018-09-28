from unittest import TestCase
from Map.LosCalculator import LosCalculator
from Map.CSVMatrixReader import CSVMatrixReader
from Common.Point import Point
import os.path
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider

class TestLosCalculator(TestCase):
    def setUp(self):
          self._ConfigProvider = UnitTestDummyConfigProvider()

    def test_IsLos_Success_SameRow_RightMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(1, 1);
        p2 = Point(8, 1);
        calc=LosCalculator()
        isLos=calc.IsLos(p1,p2,csvreader.Matrix)
        self.assertTrue(isLos)

    def test_IsLos_Success_SameRow_LeftMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(8, 1);
        p2 = Point(1, 1);
        calc = LosCalculator()
        isLos = calc.IsLos(p1, p2, csvreader.Matrix)
        self.assertTrue(isLos)
    def test_IsLos_Fail_SameRow_LeftMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(0, 2);
        p2 = Point(3, 2);
        calc=LosCalculator()
        isLos=calc.IsLos(p1,p2,csvreader.Matrix)
        self.assertFalse(isLos)


    def test_IsLos_Fail_SameRow_RightMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(4, 7);
        p2 = Point(1, 7);
        calc = LosCalculator()
        isLos = calc.IsLos(p1, p2, csvreader.Matrix)
        self.assertFalse(isLos)

    def test_IsLos_Success_SameCol_UpMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(8, 8);
        p2 = Point(8, 6);
        calc = LosCalculator()
        isLos = calc.IsLos(p1, p2, csvreader.Matrix)
        self.assertTrue(isLos)

    def test_IsLos_Success_SameCol_DownMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(8, 1);
        p2 = Point(1, 1);
        calc = LosCalculator()
        isLos = calc.IsLos(p1, p2, csvreader.Matrix)
        self.assertTrue(isLos)

    def test_IsLos_Fail_SameCol_DownMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(1, 3);
        p2 = Point(1, 8);
        calc = LosCalculator()
        isLos = calc.IsLos(p1, p2, csvreader.Matrix)
        self.assertFalse(isLos)

    def test_IsLos_Fail_SameCol_UpMovment(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\ChallangeMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(7, 4);
        p2 = Point(7, 2);
        calc = LosCalculator()
        isLos = calc.IsLos(p1, p2, csvreader.Matrix)
        self.assertFalse(isLos)