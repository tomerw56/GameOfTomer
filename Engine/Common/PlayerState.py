
from Utils.ConfigProvider import ConfigProvider
from Engine.Common.Facade.PlayerStateFacade import PlayerStatFacade
from Common.MovmentCommand import MovementCommand
from Common.Point import Point
class PlayerState(PlayerStatFacade):
    def __init__(self,id:int):
        PlayerStatFacade.__init__(self,id)

    def UpdateStatesDueToNoMovement(self):
        self._TimeInPosition  +=1

    def UpdateStatesDueToMovement(self,pTo:Point):
        self._ThreatenedTime = 0
        self._ThreateningTime = 0
        self._TimeInPosition = 0
        self._IsThretened = False
        self._Position=pTo

    @PlayerStatFacade.threatenedTime.setter
    def threatenedTime(self, value):
        self._ThreatenedTime = value

    @PlayerStatFacade.threateningTime.setter
    def threateningTime(self, value):
        self._ThreateningTime = value


    @PlayerStatFacade.timeinposition.setter
    def timeinposition(self, value):
        self._TimeInPosition = value

    @PlayerStatFacade.Threatened.setter
    def threatened(self, value):
        self._IsThretened = value

    @PlayerStatFacade.destroyed.setter
    def destroyed(self, value):
        self._IsDestoryed = value

    @PlayerStatFacade.score.setter
    def score(self, value):
        self._Score = value

    @PlayerStatFacade.position.setter
    def position(self, value):
        self._Position = value
