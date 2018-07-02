from unittest import TestCase
from Common.Dimensions import Dimensions

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

    def test_ToString(self):
        p = Dimensions(2, 1)
        print(p.getString())
        self.assertTrue(("Width=2 Height= 1"== p.getString()), "error")
