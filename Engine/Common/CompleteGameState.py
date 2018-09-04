from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.GameState import GameState
from Engine.Common.Facade.GameStateFacade import GameStateFacade
from Engine.Common.Facade.VictoryAnalysis import VictoryAnalysis
from typing import List


class CompleteGameState():
    def __init__(self, totalPlayingTime: int):
        self._Player1 = PlayerState(1)
        self._Player2 = PlayerState(2)
        self._VictoryAnalysis=VictoryAnalysis();
        self._PlayingTime = 0
        self._TotalPlayingTime = totalPlayingTime

        self._Player_1_GameState = GameState(self._Player1, self._Player2, totalPlayingTime);
        self._Player_2_GameState = GameState(self._Player2, self._Player1, totalPlayingTime);


    @property
    def player_2_GameState(self):
        return self._Player_2_GameState

    @property
    def player_1_GameState(self):
        return self._Player_1_GameState

    @property
    def player_2_State(self):
        return self._Player2

    @property
    def player_1_State(self):
        return self._Player1

    @property
    def playingtime(self):
        return self._PlayingTime

    @playingtime.setter
    def playingtime(self, value):
        self._PlayingTime = value
        self._Player_1_GameState.playingtime=value
        self._Player_2_GameState.playingtime = value

    @property
    def totalplayingtime(self):
        return self._TotalPlayingTime

    @property
    def victory(self):
        return self._VictoryAnalysis



    def __str__(self):
        return 'Player1={0} Player2= {1} PlayingTime={2} TotalPlayingTime={3} '.format(self._Player1,
                                                                                       self._Player2,
                                                                                       self._PlayingTime,
                                                                                       self._TotalPlayingTime)
