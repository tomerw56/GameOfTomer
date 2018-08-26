from Common.MovmentCommand import MovementCommand
from Engine.Common.Facade import PlayerEngineFacade
from Engine.Common.Facade.PlayerFacade import PlayerFacade
import random

class EvadingPlayerFacade(PlayerFacade):
    def DoTurn(self, engine: PlayerEngineFacade)->MovementCommand:
        self._Evades=0
        if not hasattr(self,"_Engine"):
            self._Engine=engine;
        if not engine.GetGameState().MyPlayer.Threatened:
            return  MovementCommand.GetEmpty();
        return self.CalcMovment(engine)


    def CalcMovment(self,engine:PlayerEngineFacade)->MovementCommand:
        X=random.randint(1, 4)
        Y=random.randint(2, 3)
        self._Evades+=1
        return MovementCommand(X,Y)

    @property
    def Evades(self) -> int:
        return self._Evades

    @property
    def MyEngine(self)->PlayerEngineFacade:
        return self._Engine