from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point

from Engine.Controllers.ControllersEnums import PlayerNoMovmentState
from typing import List
class NoMovementController:
    def __init__(self,configprovider:ConfigProvider):
        self._ConfigProvider=configprovider;
        self._PointDecTime = int(self._ConfigProvider.getValue("NoMovement.Config", "PointDecTime"))


    def IStaticForTooLong(self,position: Point, nomovetime)->PlayerNoMovmentState:

        if self._IsTimeOutForDec(nomovetime):
            return PlayerNoMovmentState.STATIC_TIMEOUT
        else:
            return PlayerNoMovmentState.OK




    def _IsTimeOutForDec(self,nomovetime)->bool:
        return nomovetime>self._PointDecTime;

