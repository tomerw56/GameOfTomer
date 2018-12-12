from Common.MovmentCommand import MovementCommand
from Common.Point import Point
from Engine.Common.Facade import PlayerEngineFacade
from Engine.Common.Facade.PlayerFacade import PlayerFacade

class SamePointMovingPlayerFacade(PlayerFacade):
    def __init__(self):
        self._DestPoint=Point(1,2)
    def DoTurn(self, engine: PlayerEngineFacade)->MovementCommand:
        if not hasattr(self,"_Engine"):
            self._Engine=engine;
        return  MovementCommand(self._DestPoint)

    def GetDescription(self)-> str:
        return "SamePointMovingPlayerFacade"

    @property
    def MyEngine(self)->PlayerEngineFacade:
        return self._Engine