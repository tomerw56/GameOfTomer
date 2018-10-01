import networkx as nx
import numpy as np
from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point

from Common.Constant import Constants
from Common.Point import Point


class LosCalculator:
    def __init__(self):
        self._Consts = Constants()

    def IsLos(self, pFrom: Point, pTo: Point, map: np.matrix)->bool:
        if self.IsSafePoint(pTo,map):
            return False
        alt=map[pFrom.y,pFrom.x]
        if pFrom==pTo:
            return True
        lospoints=self._bres(pFrom,pTo)
        for point in lospoints:
            currntalt=map[point.y, point.x]
            if currntalt!=self._Consts.SafePointValue:
                if currntalt>alt:
                    return False
        return True

    def IsSafePoint(self,point,map:np.matrix):
        alt = map[point.y, point.x]
        return alt==self._Consts.SafePointValue
    def getLosList(self,pFrom:Point,pTo:Point):
        lospoints=[]
        lospoints = self._bres(pFrom, pTo)
        return lospoints

    def _bres(self,pFrom:Point,pTo:Point):
        end = False
        x0 = pFrom.x
        y0 = pFrom.y
        x1 = pTo.x
        y1  = pTo.y
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        if x0 < x1:
            sx = 1
        else:
            sx = -1

        if y0 < y1:
            sy = 1
        else:
            sy = -1
        err = dx - dy
        LOSpoints=[]
        while not end:
            if x0 == x1 and y0 == y1:
                end = True
                LOSpoints.append(Point(x1, y1))
                return LOSpoints
            e2 = 2 * err
            if e2 > -dy:
                err = err - dy
                x0 = x0 + sx
            if e2 < dx:
                err = err + dx
                y0 = y0 + sy
            LOSpoints.append(Point(x0, y0))
        return LOSpoints




