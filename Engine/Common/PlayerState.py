
from Utils.ConfigProvider import ConfigProvider
from Engine.Common.Facade.PlayerStateFacade import PlayerStatFacade
from Common.Point import Point
class PlayerState(PlayerStatFacade):
    def __init__(self,id:int):
        PlayerStatFacade.__init__(self,id)
    @PlayerStatFacade.threatenedTime.setter
    def threatenedTime(self, value):
        self._ThreatenedTime = value

    @PlayerStatFacade.threateningTime.setter
    def threateningTime(self, value):
        self._ThreateningTime = value

    @PlayerStatFacade.restPointTime.setter
    def restPointTime(self, value):
        self._RestPointTime = value

    @PlayerStatFacade.timeinposition.setter
    def timeinposition(self, value):
        self._TimeInPosition = value

    @PlayerStatFacade.destroyed.setter
    def destroyed(self, value):
        self._IsDestoryed = value

    @PlayerStatFacade.score.setter
    def score(self, value):
        self._Score = value

    @PlayerStatFacade.position.setter
    def position(self, value):
        self._Position = value
