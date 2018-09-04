import os.path
import sys
from Common.Point import Point as pt
from unittest import TestCase

from Common import Point
from Map.CSVMatrixReader import CSVMatrixReader

class TestCSVMatrixReader(TestCase):
    def test_Parse_OK(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap/Map.csv')
        csvreader=CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertTrue(csvreader.fileLoaded, "error")


    def test_Parse_Fail_FileName(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..Maps/NoMap/Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertFalse(csvreader.fileLoaded, "error")

    def test_Parse_Fail_TooShort(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..Maps/TooShortTestMap/Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertFalse(csvreader.fileLoaded, "error")

    def test_Parse_Fail_TooManyItems(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..Maps/TooManyCollsTestMap/Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertFalse(csvreader.fileLoaded, "error")


