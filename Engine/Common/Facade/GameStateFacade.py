
from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.RestPointState import RestPointState
from typing import  List
class GameStateFacade():
    def __init__(self,myPlayerState,enemyPlayerState,totalPlayingTime:int,restPointStates:List[RestPointState]=[]):
        self._MyPlayer=myPlayerState
        self._EnemyPlayer = enemyPlayerState
        self._PlayingTime=0
        self._TotalPlayingTime = totalPlayingTime
        self._RestingPoints=restPointStates

    @property
    def RestingPoints(self):
        return self._RestingPoints
    @property
    def MyPlayer(self):
        return self._MyPlayer

    @property
    def EnemyPlayer(self):
        return self._EnemyPlayer
    @property
    def playingtime(self):
        return self._PlayingTime

    @property
    def totalplayingtime(self):
        return self._TotalPlayingTime

    def __str__(self):
        return 'MyPlayer={0} EnemyPlayer= {1} PlayingTime={2} TotalPlayingTime={3} '.format(self._MyPlayer, self._EnemyPlayer,self._PlayingTime,self._TotalPlayingTime)