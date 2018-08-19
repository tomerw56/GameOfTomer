from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
from Engine.Common.RestPointState import RestPointState
from Engine.Controllers.ControllersEnums import PlayerThreatState
from Engine.Common.PlayerState import PlayerState
from Map.MapHolder import MapHolder
from Common.Constant import Constants
class ThreatController:
    def __init__(self,mapholder:MapHolder,configprovider:ConfigProvider):
        self._mapHolder=mapholder
        self._Consts=Constants()
        self._ConfigProvider=configprovider
        self._ThreatTimeOut= int(self._ConfigProvider.getValue("Threat.Config", "ThreatTimeOut"))
        self._ThreatAltDiff = int(self._ConfigProvider.getValue("Threat.Config", "ThreatAltDiff"))
    def GetPlayerThreatState(self,threateningPlayer:PlayerState,threatenedPlayer:PlayerState)->PlayerThreatState:
        if self._mapHolder.isLOS(threateningPlayer.position,threatenedPlayer.position) and self._IsControllingAlt(threateningPlayer.position,threatenedPlayer.position):
            if threatenedPlayer.threatenedTime>self._ThreatTimeOut:
                return PlayerThreatState.DESTROYED
            else:
                return PlayerThreatState.THREATENED
        else:
            return PlayerThreatState.NOT_THREATENED
    def _IsControllingAlt(self,threateningPlayer_position,threatenedPlayer_position):
        threateningPlayerAlt=self._mapHolder.getAlt(threateningPlayer_position)
        if threateningPlayerAlt==self._Consts.InValidAlt:
            return False
        threatenedPlayerAlt = self._mapHolder.getAlt(threatenedPlayer_position)
        if threatenedPlayerAlt == self._Consts.InValidAlt:
            return False
        return (threateningPlayerAlt-threatenedPlayerAlt)>=self._ThreatAltDiff