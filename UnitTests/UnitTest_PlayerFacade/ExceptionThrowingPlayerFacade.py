from Common.MovmentCommand import MovementCommand
from Engine.Common.Facade import PlayerEngineFacade
from Engine.Common.Facade.PlayerFacade import PlayerFacade

class ExceptionThrowingPlayerFacade(PlayerFacade):
    def __init__(self,turnsTilException):
        self._TurnsTillException=turnsTilException

    def DoTurn(self, engine: PlayerEngineFacade)->MovementCommand:
        self._TurnsTillException-=1
        if(self._TurnsTillException<0):
            raise Exception('ExceptionThrowingPlayerFacade failed')
        return  MovementCommand.GetEmpty();