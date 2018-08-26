from Common.Point import Point
from typing import List
class PointsControl(object):
    def __init__(self,location:Point):
        self._Location=location
        self._ControlledPoints=[]
        self._ControllingPoints = []

    @property
    def location(self):
        return self._Location

    @property
    def controlledpoints(self):
        return self._ControlledPoints
    @property
    def controllingpoints(self):
        return self._ControllingPoints
