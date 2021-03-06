from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
from Common.Dimensions import Dimensions
import numpy as np
from Common.PathResult import  PathResult
from Engine.Common.Facade.PlayerStateFacade import PlayerStatFacade
from Engine.Common.Facade.GameStateFacade import GameStateFacade
class PlayrerEngineFacade:

    def __init__(self,id,map:np.matrix,dimensions:Dimensions):
        self._ID=int(id)
        self._Dimensions=dimensions
        self._Map=map


    def MayIMove(self, position: Point) -> bool:
        pass

    def MayMoveBetweenPoints(self, pFrom: Point, pTo: Point) -> bool:
        pass

    def GetPathForMe(self,position:Point)->PathResult:
        pass
    def GetPathForBetweenPoints(self, pFrom: Point, pTo: Point)->PathResult:
        pass

    def IsLosToEnemy(self,position:Point)->bool:
        pass

    def IsLosBetweenPoints(self, pFrom: Point, pTo: Point) -> bool:
       pass

    def IsLosFromMeToPoint(self, position: Point) -> bool:
        pass

    def IsControllingEnemy(self)->bool:
        pass

    def IsBeingControlledByEnemy(self)->bool:
        pass

    def GetGameState(self)->GameStateFacade:
        pass

    @property
    def ID(self):
        return self._ID

    @property
    def Dimensions(self):
        return self._Dimensions

    @property
    def map(self)->np.matrix:
        return self._Map