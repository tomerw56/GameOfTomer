
from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.Facade.GameStateFacade import GameStateFacade
from typing import  List
class GameState(GameStateFacade):
    def __init__(self,myPlayerState:PlayerState,enemyPlayerState:PlayerState,totalPlayingTime:int):
        GameStateFacade.__init__(self,myPlayerState,enemyPlayerState,totalPlayingTime)
    @GameStateFacade.playingtime.setter
    def playingtime(self, value):
        self._PlayingTime = value

