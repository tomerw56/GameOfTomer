from Common.MovmentCommand import MovementCommand
from Engine.Common.Facade import PlayerEngineFacade


class PlayerFacade:
    def DoTurn(self, engine: PlayerEngineFacade)->MovementCommand:
        pass;
    def GetDescription(self)->str:
        return ""
