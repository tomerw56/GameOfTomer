from Common.MovmentCommand import MovementCommand
from Engine.Common.Facade import PlayerEngineFacade
from Common.Point import Point
from Engine.Common.Facade.PlayerFacade import PlayerFacade
import random

class EvadingPlayerFacade(PlayerFacade):
    def __init__(self):
        self._Evades = 0
    def DoTurn(self, engine: PlayerEngineFacade)->MovementCommand:

        if not hasattr(self,"_Engine"):
            self._Engine=engine;
        if not engine.GetGameState().MyPlayer.Threatened:
            return  MovementCommand.GetEmpty();
        return self.CalcMovment(engine)


    def CalcMovment(self,engine:PlayerEngineFacade)->MovementCommand:


        X=engine.GetGameState().MyPlayer.position.x
        Y=engine.GetGameState().MyPlayer.position.y-1

        if engine.MayIMove(Point(X,Y)):
            self._Evades+=1
            return MovementCommand(Point(X,Y))
        return MovementCommand.GetEmpty()

    @property
    def Evades(self) -> int:
        return self._Evades

    @property
    def MyEngine(self)->PlayerEngineFacade:
        return self._Engine