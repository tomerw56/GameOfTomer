

from Common.MovmentCommand import MovementCommand
from Engine.Common.Facade import PlayerEngineFacade
from Engine.Common.Facade.PlayerFacade import PlayerFacade

class ExceptionThrowingPlayerFacade(PlayerFacade):
    def __init__(self,*args):
        if len(args)==1:
            turnsTilException = int(args[0])
        else:
            turnsTilException=5
        self._TurnsTillException=turnsTilException
    def GetDescription(self) -> str:
        return "EvadingPlayerFacade"
    def DoTurn(self, engine: PlayerEngineFacade)->MovementCommand:
        self._TurnsTillException-=1
        if(self._TurnsTillException<0):
            raise Exception('ExceptionThrowingPlayerFacade failed')
        return  MovementCommand.GetEmpty();