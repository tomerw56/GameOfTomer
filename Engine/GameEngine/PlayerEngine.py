from Engine.Common.Facade.PlayerEngineFacade import PlayrerEngineFacade
from Engine.Common.PlayerState import PlayerState
from Engine.Common.GameState import GameState
from Utils.ConfigProvider import ConfigProvider
from Map.MapHolder import MapHolder
from Common.Point import Point

class PlayerEngine(PlayrerEngineFacade):
    def __init__(self,gamestate:GameState,configprovider:ConfigProvider,mapholder:MapHolder):
        self._GameState=gamestate
        PlayrerEngineFacade.__init__(self,gamestate.MyPlayer.id,mapholder.map,mapholder.getMapDim())
        self._ConfigProvider=configprovider
        self._mapholder=mapholder

        self._GameState = gamestate

    def Update(self,gamestate:GameState):

        self._GameState = gamestate

    def MayIMove(self, position: Point) -> bool:
        return  self._mapholder.mayMove(self._GameState.MyPlayer.position,position)

    def MayMoveBetweenPoints(self, pFrom: Point,pTo:Point) -> bool:
        return  self._mapholder.mayMove(pFrom,pTo)

    def IsLosBetweenPoints(self, pFrom: Point,pTo:Point) -> bool:
        return self._mapholder.isLOS(pFrom,pTo)

    def IsLosFromMeToPoint(self, position: Point) -> bool:
        return self._mapholder.isLOS(self._GameState.MyPlayer.position,position)

    def IsLosToEnemy(self) -> bool:
        return self._mapholder.isLOS(self._GameState.MyPlayer.position, self._GameState.EnemyPlayer.position)

    def IsControllingEnemy(self) -> bool:
        control=self._mapholder.pointscontrol
        controlledpoints=control[(self._GameState.MyPlayer.position.x,self._GameState.MyPlayer.position.y)].controlledpoints
        for point in controlledpoints:
            if point==self._GameState.EnemyPlayer.position:
                return True
        return False

    def IsBeingControlledByEnemy(self) -> bool:
        control = self._mapholder.pointscontrol
        controllingpoints = control[
            (self._GameState.MyPlayer.position.x, self._GameState.MyPlayer.position.y)].controllingpoints
        for point in controllingpoints:
            if point == self._GameState.EnemyPlayer.position:
                return True
        return False

    def GetGameState(self) -> GameState:
        return self._GameState
