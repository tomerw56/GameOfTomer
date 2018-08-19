from unittest import TestCase
from Common.Point import Point

class TestPoint(TestCase):
    def test_x_True(self):
        p=Point(1,2)
        self.assertTrue((1 == p.x), "error")

    def test_x_False(self):
        p = Point(1, 2)
        self.assertFalse((2 == p.x), "error")

    def test_Y_True(self):
        p = Point(2, 1)
        self.assertTrue((1 == p.y), "error")

    def test_Y_False(self):
        p = Point(2, 1)
        self.assertFalse((2 == p.y), "error")


