from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
from Common.Dimensions import Dimensions
from Engine.Common.Facade.PlayerStateFacade import PlayerStatFacade
from Engine.Common.Facade.GameStateFacade import GameStateFacade
class EngineFacade:

    def __init__(self,id,configprovider:ConfigProvider,dimensions:Dimensions,map):
        self._ConfigProvider=configprovider
        self._ID=id
        self._Dimensions = dimensions
        self._Map=map

    def MoveTo(self,position:Point)->bool:
        pass

    def MayMove(self,position:Point)->bool:
        pass

    def IsLos(self,position:Point)->bool:
        pass

    def IsLosToEnemy(self,position:Point)->bool:
        pass

    def Finish(self):
        pass

    def GetEnemyState(self)->GameStateFacade:
        pass

    def GetMyState(self)->GameStateFacade:
        pass

    def GetGameState(self)->PlayerStatFacade:
        pass

    @property
    def ID(self):
        return self._ID

    @property
    def Dimensions(self):
        return self._Dimensions

    @property
    def map(self):
        return self._Map