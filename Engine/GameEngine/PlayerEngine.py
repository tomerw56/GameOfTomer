from Engine.Common.Facade.PlayerEngineFacade import PlayrerEngineFacade
from Engine.Common.PlayerState import PlayerState
from Engine.Common.GameState import GameState
from Utils.ConfigProvider import ConfigProvider
from Map.MapHolder import MapHolder
from Common.Point import Point

class PlayerEngine(PlayrerEngineFacade):
    def __init__(self,myState:PlayerState,enemyState:PlayerState,gamestate:GameState,configprovider:ConfigProvider,mapholder:MapHolder):
        PlayrerEngineFacade.__init__(self,myState.id,mapholder.map,mapholder.getMapDim())
        self._ConfigProvider=configprovider
        self._mapholder=mapholder
        self._MyState=myState
        self._EnemyState = enemyState
        self._GameState = gamestate

    def Update(self,myState:PlayerState,enemyState:PlayerState,gamestate:GameState):
        self._MyState = myState
        self._EnemyState = enemyState
        self._GameState = gamestate

    def MayIMove(self, position: Point) -> bool:
        return  self._mapholder.mayMove(self._MyState.position,position)

    def MayMoveBetweenPoints(self, pFrom: Point,pTo:Point) -> bool:
        return  self._mapholder.mayMove(pFrom,pTo)

    def IsLosBetweenPoints(self, pFrom: Point,pTo:Point) -> bool:
        return self._mapholder.isLOS(pFrom,pTo)

    def IsLosFromMeToPoint(self, position: Point) -> bool:
        return self._mapholder.isLOS(self._MyState.position,position)

    def IsLosToEnemy(self) -> bool:
        return self._mapholder.isLOS(self._MyState.position, self._EnemyState.position)

    def GetEnemyState(self) -> PlayerState:
        return self._EnemyState

    def GetMyState(self) -> PlayerState:
        return self._MyState

    def GetGameState(self) -> GameState:
        return self._GameState

