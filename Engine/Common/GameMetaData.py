from Utils.ConfigProvider import ConfigProvider
from Engine.Common.PlayerState import PlayerState
from Engine.Common.GameState import GameState
from Engine.Common.Facade.GameStateFacade import GameStateFacade
from Engine.Common.RestPointState import RestPointState
from Engine.Common.Facade.VictoryAnalysis import VictoryAnalysis
from typing import List
from time import time
import datetime


class GameMetaData():
    def __init__(self, infrapath):
        self._infrapath = infrapath
        self._PlayTime=datetime.datetime.now()
    @property
    def infrapath(self):
        return self._infrapath

    @property
    def playtime(self):
        return self._PlayTime

