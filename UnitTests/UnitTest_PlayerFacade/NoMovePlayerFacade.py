from Common.MovmentCommand import MovementCommand
from Engine.Common.Facade import PlayerEngineFacade
from Engine.Common.Facade.PlayerFacade import PlayerFacade

class NoMovePlayerFacade(PlayerFacade):
    def DoTurn(self, engine: PlayerEngineFacade)->MovementCommand:
        if not hasattr(self,"_Engine"):
            self._Engine=engine;
        return  MovementCommand.GetEmpty();

    def GetDescription(self) -> str:
        return "NoMovePlayerFacade"

    @property
    def MyEngine(self)->PlayerEngineFacade:
        return self._Engine