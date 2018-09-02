from unittest import TestCase
import os.path
from Map.CSVMatrixReader import CSVMatrixReader
from Common.BoundingBoxSourceTarget import BoundingBoxSourceTarget
from Common.Point import Point
import numpy as np;

class TestBoundingBoxSourceTarget(TestCase):
    def test_BB_Valid(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1=Point(1,1);
        p2 = Point(3, 4);
        BB=BoundingBoxSourceTarget(csvreader.Matrix,p1,p2,20);

        self.assertTrue(BB.valid)

    def test_BB_Valid_Y_OutOfBoundries(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(1, 1);
        p2 = Point(3, 3000);
        BB = BoundingBoxSourceTarget(csvreader.Matrix, p1, p2, 20);
        self.assertTrue(BB.valid)

    def test_BB_Valid_X_OutOfBoundries(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(1, 1);
        p2 = Point(300, 4);
        BB = BoundingBoxSourceTarget(csvreader.Matrix, p1, p2, 20);
        self.assertTrue(BB.valid)

    def test_BB_Dimensions(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1=Point(1,1);
        p2 = Point(3, 4);
        BB=BoundingBoxSourceTarget(csvreader.Matrix,p1,p2,20);


        self.assertTrue(BB.bb[0]==1)
        self.assertTrue(BB.bb[1] == 1)
        self.assertTrue(BB.bb[2] ==10)
        self.assertTrue(BB.bb[3] == 10)

    def test_BB_Dimensions_ZeroMargin(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1 = Point(1, 1);
        p2 = Point(3, 4);
        BB = BoundingBoxSourceTarget(csvreader.Matrix, p1, p2, 0);

        self.assertTrue(BB.bb[0] == 1)
        self.assertTrue(BB.bb[1] == 1)
        self.assertTrue(BB.bb[2] == 3)
        self.assertTrue(BB.bb[3] == 4)

    def test_BB_Dimensions_Values_1(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1=Point(1,1);
        p2 = Point(3, 4);
        BB=BoundingBoxSourceTarget(csvreader.Matrix,p1,p2);
        self.assertTrue(BB.dsmSubset[0, 0] == 2)
        self.assertTrue(BB.dsmSubset[1, 1] == 3)
        self.assertTrue(BB.dsmSubset[2, 2] == 2)

    def test_BB_Dimensions_Values_2(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..\Maps\TestMap\Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        p1=Point(1,1);
        p2 = Point(5,5);
        BB=BoundingBoxSourceTarget(csvreader.Matrix,p1,p2);
        self.assertTrue(BB.dsmSubset[0, 0] == 2)
        self.assertTrue(BB.dsmSubset[1, 1] == 3)
        self.assertTrue(BB.dsmSubset[2, 2] == 2)
        self.assertTrue(BB.dsmSubset[3, 3] == 3)
        self.assertTrue(BB.dsmSubset[4, 4] == 1)
