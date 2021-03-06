from Utils.ConfigProvider import ConfigProvider
from Common.Point import Point
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
        isLOS=False
        control = self._mapHolder.pointscontrol
        if self._IsSafetyPoint(threatenedPlayer.position):
            print ('Attacked player in safepoint')
            return PlayerThreatState.SAFEPOINT
        isLOS=self._isLos(threateningPlayer.position,threatenedPlayer.position)

        if isLOS:
            if self._IsControllingAlt(threateningPlayer.position, threatenedPlayer.position):
                if self._mapHolder.isCloseToSafty(threateningPlayer.position):
                    if threatenedPlayer.threatenedTime>self._ThreatTimeOut:
                        print('Attacked player was in threat state for too long and now destroyed!!!')
                        return PlayerThreatState.DESTROYED
                    else:
                        print('Attacked player is in threat state')
                        return PlayerThreatState.THREATENED
                else:
                    print('Attacking player not close to safty point')
                    return PlayerThreatState.NOT_THREATENED
            else:
                print ('Attacking player is not in threat alt')
                return PlayerThreatState.NOT_THREATENED
        else:
            print('Attacking Player has no LOS')
            return PlayerThreatState.NOT_THREATENED
        return PlayerThreatState.NOT_THREATENED
    def isThreatnedForTooLong(self,threatenedtime):
        return threatenedtime>self._Consts.ThreatTimeTillPunishment
    def _isLos(self,threateningPlayer_position, threatenedPlayer_position):
        control = self._mapHolder.pointscontrol
        controlledpoints = control[threateningPlayer_position.x][threateningPlayer_position.y].controlledpoints
        for point in controlledpoints:
            if point == threatenedPlayer_position:
               return True
        return False
    def _IsSafetyPoint(self,threatenedPlayer_position):
        saftypoints = self._mapHolder.saftypoints
        for point in saftypoints:
            if point == threatenedPlayer_position:
                return  True
        return False
    def _IsControllingAlt(self,threateningPlayer_position,threatenedPlayer_position):
        threateningPlayerAlt=self._mapHolder.getAlt(threateningPlayer_position)
        if threateningPlayerAlt==self._Consts.InValidAlt:
            return False
        threatenedPlayerAlt = self._mapHolder.getAlt(threatenedPlayer_position)
        if threatenedPlayerAlt == self._Consts.InValidAlt:
            return False
        return (threateningPlayerAlt-threatenedPlayerAlt)>=self._ThreatAltDiff