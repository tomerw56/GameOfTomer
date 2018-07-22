from Utils.ConfigProvider import ConfigProvider
from Engine.Common.GameState import GameState
import os
import datetime
import jsonpickle
import io


class Recorder:
    def __init__(self,configProvider:ConfigProvider):
        self._Configuration=configProvider
        self._Record=bool(self._Configuration.getValue('Recording','record').lower() in ("true"))
        if self._Record:
            self._Initialize()
    def _Initialize(self):
        directory=self._Configuration.getValue('Recording','folder')
        if not os.path.exists(directory):
            os.makedirs(directory)
        self._NewFullDir=os.path.join(directory,datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
        os.makedirs(self._NewFullDir)

    def Record(self,gamestate:GameState):
        if not self._Record:
            return "";
        frozen = jsonpickle.encode(gamestate)
        filedir = os.path.join(self._NewFullDir,"Step_{0}.json".format(gamestate.playingtime))
        with io.open(filedir, 'w') as f:
            f.write(frozen)
        return filedir