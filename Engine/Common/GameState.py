
from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.Facade.GameStateFacade import GameStateFacade
from Engine.Common.RestPointState import RestPointState
from typing import  List
class GameState(GameStateFacade):
    def __init__(self,totalPlayingTime:int,myPlayerState,enemyPlayerState,restPointStates:List[RestPointState]=[]):
        GameStateFacade.__init__(self,myPlayerState,enemyPlayerState,totalPlayingTime,restPointStates)
    @GameStateFacade.playingtime.setter
    def playingtime(self, value):
        self._PlayingTime = value

