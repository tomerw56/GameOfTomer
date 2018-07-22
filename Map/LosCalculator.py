import networkx as nx
import numpy as np
from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
from Common.BoundingBoxSourceTarget import BoundingBoxSourceTarget
from Common.Constant import Constants
from Common.Point import Point


class LosCalculator:
    def __init__(self, configProvider):
        self._Consts = Constants()
        self._ConfigProvider = configProvider

    def IsLos(self, pFrom: Point, pTo: Point, map: np.matrix):
        try:
            originalalt = map[pFrom.y, pFrom.x]
            width, height = map.shape
            boundingBox = BoundingBoxSourceTarget(map, pFrom, pTo, 200)
            if boundingBox.valid == False:
                print('invalid Bounding Box ')
                return False
            t = np.arange(0, 1.01,0.01)
            vec = np.zeros((len(t),2))
            vec[0, 0] = pFrom.x
            vec[0, 1] = pFrom.y
            vec[100, 0] = pTo.x
            vec[100, 1] = pTo.y
            for ii in range(1, len(t) - 1):
                if pFrom.x==pTo.x:
                    vec[ii, 0]=pFrom.x
                else:
                    vec[ii, 0] =  (pFrom.x * (1 - t[ii]) + pTo.x * (t[ii])) - boundingBox.topleftX
                if pFrom.y == pTo.y:
                    vec[ii, 1] = pFrom.y
                else:
                    vec[ii, 1] = (pFrom.y * (1 - t[ii]) + pTo.y * (t[ii])) - boundingBox.topleftY
            fixedindexes = np.zeros((len(t),2))
            for kk in range(0, len(vec)):
                fixedindexes[kk,0] =round(vec[kk, 0])
                fixedindexes[kk,1] =round(vec[kk, 1])
            for kk in range(0, len(vec)):
                alt = map.item(int(fixedindexes[kk, 1]), int(fixedindexes[kk,0]))
                if alt > originalalt:
                    print('alt diff too high')
                    return False

            return True;

        except nx.exception.NetworkXError:
            return False
        except nx.exception.NetworkXError:
            return False
