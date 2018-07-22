
from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.RestPointState import RestPointState
from typing import  List
class GameStateFacade():
    def __init__(self,totalPlayingTime:int,restPointStates:List[RestPointState]=[]):
        self._Player1=PlayerState(1)
        self._Player2 = PlayerState(2)
        self._PlayingTime=0
        self._TotalPlayingTime = totalPlayingTime
        self._RestingPoints=restPointStates

    @property
    def RestingPoints(self):
        return self._RestingPoints
    @property
    def player1(self):
        return self._Player1

    @property
    def player2(self):
        return self._Player2
    @property
    def playingtime(self):
        return self._PlayingTime

    @property
    def totalplayingtime(self):
        return self._TotalPlayingTime

    def __str__(self):
        return 'Player1={0} Player2= {1} PlayingTime={2} TotalPlayingTime={3} '.format(self._Player1, self._Player2,self._PlayingTime,self._TotalPlayingTime)