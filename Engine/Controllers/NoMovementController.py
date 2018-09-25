from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point

from Engine.Controllers.ControllersEnums import PlayerNoMovmentState
from typing import List
class NoMovementController:
    def __init__(self,configprovider:ConfigProvider):
        self._ConfigProvider=configprovider;
        self._PointDecTime = int(self._ConfigProvider.getValue("NoMovement.Config", "PointDecTime"))
        self._SafePointDecTime = int(self._ConfigProvider.getValue("NoMovement.Config", "SafePointDecTime"))



    def IStaticForTooLong(self,position: Point, nomovetime,isSafePoint)->PlayerNoMovmentState:


        if self._IsTimeOutForDec(nomovetime,isSafePoint):
            return PlayerNoMovmentState.STATIC_TIMEOUT
        else:
            return PlayerNoMovmentState.OK




    def _IsTimeOutForDec(self,nomovetime,isSafePoint)->bool:
        if isSafePoint:
            return nomovetime > self._SafePointDecTime;
        return nomovetime>self._PointDecTime;

