
from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.Facade.PlayerStateFacade import PlayerStatFacade

from typing import  List
class GameStateFacade():
    def __init__(self,myPlayerState:PlayerState,enemyPlayerState:PlayerState,totalPlayingTime:int):
        self._MyPlayer=myPlayerState
        self._EnemyPlayer = enemyPlayerState
        self._PlayingTime=0
        self._TotalPlayingTime = totalPlayingTime


    @property
    def MyPlayer(self)->PlayerStatFacade:
        return self._MyPlayer

    @property
    def EnemyPlayer(self)->PlayerStatFacade:
        return self._EnemyPlayer
    @property
    def playingtime(self):
        return self._PlayingTime

    @property
    def totalplayingtime(self):
        return self._TotalPlayingTime

    def __str__(self):
        return 'MyPlayer={0} EnemyPlayer= {1} PlayingTime={2} TotalPlayingTime={3} '.format(self._MyPlayer, self._EnemyPlayer,self._PlayingTime,self._TotalPlayingTime)