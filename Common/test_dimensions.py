from unittest import TestCase
from Common.Dimensions import Dimensions
from Common.Point import Point

class TestDimensions(TestCase):
    def test_Width_True(self):
        p=Dimensions(1,2)
        self.assertTrue((1 == p.width), "error")

    def test_Width_False(self):
        p = Dimensions(1, 2)
        self.assertFalse((2 == p.width), "error")

    def test_Height_True(self):
        p = Dimensions(2, 1)
        self.assertTrue((1 == p.height), "error")

    def test_Height_False(self):
        p = Dimensions(2, 1)
        self.assertFalse((2 == p.height), "error")

    def test_PointIn_True(self):
        p = Dimensions(6, 6)
        point=Point(3,3)
        self.assertTrue(p.IsPointInDim(point), "error")
    def test_PointIn_False_X_Large(self):
        p = Dimensions(6, 6)
        point=Point(7,3)
        self.assertFalse(p.IsPointInDim(point), "error")

    def test_PointIn_False_X_Small(self):
        p = Dimensions(6, 6)
        point = Point(-1, 3)
        self.assertFalse(p.IsPointInDim(point), "error")

    def test_PointIn_False_Y_Large(self):
        p = Dimensions(6, 6)
        point = Point(7, 3)
        self.assertFalse(p.IsPointInDim(point), "error")

    def test_PointIn_False_Y_Small(self):
        p = Dimensions(6, 6)
        point = Point(3, -1)
        self.assertFalse(p.IsPointInDim(point), "error")


