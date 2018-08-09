import os.path
import sys
from unittest import TestCase
from Map.CSVMatrixReader import CSVMatrixReader

class TestCSVMatrixReader(TestCase):
    def test_Parse_OK(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap.csv')
        csvreader=CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertTrue(csvreader.fileLoaded, "error")


    def test_Parse_Fail_FileName(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..Maps/NoMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertFalse(csvreader.fileLoaded, "error")

    def test_Parse_Fail_TooShort(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..Maps/TooShortTestMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertFalse(csvreader.fileLoaded, "error")

    def test_Parse_Fail_TooManyItems(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..Maps/TooManyCollsTestMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertFalse(csvreader.fileLoaded, "error")

    def test_No_RestPoints(self):
        RealPath = os.path.join(os.path.dirname(__file__), '..Maps/TestMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertFalse(len(csvreader.restpoints)>0, "error")

    def test_4_RestPoints(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/ChallangeMap.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        self.assertTrue(len(csvreader.restpoints) == 4, "OK")

