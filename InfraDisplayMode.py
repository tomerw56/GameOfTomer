from Map.MapHolder import MapHolder
from Map.InfraDrawing import InfraDrawing
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider
from Map.LosCalculator import LosCalculator
import numpy as np
import shutil
import os
from pathlib import Path
from Common.Point import  Point
from Common.Constant import Constants
from Common.Dimensions import Dimensions
import networkx as nx
from Common.PointsControl import PointsControl
from networkx.readwrite import json_graph
import json
import sys
import  io

class InfraDisplayMode(object):
    def __init__(self,mapname,maximumAllowedPath):
        ConfigProvider=UnitTestDummyConfigProvider()
        ConfigProvider.addValue('Game.Config', 'DrawMapHolderGraph', 'False')
        ConfigProvider.addValue('Game.MovementDefinations','maximumAllowedPath',str(maximumAllowedPath))

        self._MapHolder = MapHolder(ConfigProvider)

        self._Valid = self._MapHolder.loadMap(mapname)

    def Draw(self):
        if (self._Valid):
            drawinfra = InfraDrawing(self._MapHolder)

    @property
    def valid(self) -> bool:
        return self._Valid