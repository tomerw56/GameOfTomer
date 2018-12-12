from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.GameState import GameState
from Engine.Common.Facade.GameStateFacade import GameStateFacade

from Engine.Common.Facade.VictoryAnalysis import VictoryAnalysis
from typing import List
from time import time
import datetime


class GameMetaData():
    def __init__(self, infrapath):
        self._infrapath = infrapath
        self._Player_1_Description=""
        self._Player_2_Description = ""
        self._PlayTime=datetime.datetime.now()
    @property
    def infrapath(self):
        return self._infrapath

    @property
    def playtime(self):
        return self._PlayTime

    @property
    def player_1_description(self):
        return self._Player_2_Description


    @property
    def player_2_description(self):
        return self._Player_2_Description

    @player_1_description.setter
    def player_1_description(self, value):
        self._Player_1_Description = value

    @player_2_description.setter
    def player_2_description(self, value):
        self._Player_2_Description = value
