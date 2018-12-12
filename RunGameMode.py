
import glob
from os import path
import os
import sys
import importlib
import itertools
import xml.etree.ElementTree as ET
from itertools import combinations,repeat
from Utils.IniConfigProvider import IniConfigProvider
import os.path
import time
from Engine.Controllers.GameController import GameController
from time import sleep

class RunGameMode(object):
    def __init__(self,botfile,inifile,gamespercouple,threads):
        self._ConfigProvider=IniConfigProvider(inifile)
        self._GamesPerCouple=gamespercouple
        botsdataparsed=self._parseBots(botfile)
        gameSchedualeBuilt=self._BuildGameScheduale(gamespercouple)
        self._Threads = threads
        self._Valid=botsdataparsed  and self._ConfigProvider.ConfigValid

    @property
    def valid(self) -> bool:
        return self._Valid
    def _BuildGameScheduale(self,gamespercouple):
        pairs=list(itertools.combinations(self._BotsData.keys(),2))
        self._TestsKeys=[]
        for i in range(0,gamespercouple):
            self._TestsKeys+=pairs
        return True
    def Run(self):

        for gamepair in  self._TestsKeys:
            try:
                sleep(2)
                firstPlayer = self._InstanceCreator(gamepair[0], self._BotsData[gamepair[0]])
                secondPlayer = self._InstanceCreator(gamepair[1], self._BotsData[gamepair[1]])
                gamecontroller = GameController(self._ConfigProvider, firstPlayer, secondPlayer)
                if not gamecontroller.valid:
                    print ("Invalid game controller")
                else:
                    print(f"Game between {gamepair[0]} and gamepair{gamepair[1]}")
                    starttime = time.time()
                    gamecontroller.Run()
                    endtime=time.time()
                    print(f"Game took {endtime-starttime} seconds Winner={gamecontroller.VictoryReason.winner} WinnignReason={gamecontroller.VictoryReason.winningireason}")
            except:
                print(sys.exc_info())

    def _parseBots(self, botfile):
        self._BotsData={};
        if path.isfile(botfile):
            try:
                tree = ET.parse(botfile)
                root = tree.getroot()
                for child in root:
                    if 'args' in child.attrib:
                        self._BotsData[child.attrib['file']]=(child.attrib['module'],child.attrib['classname'],child.attrib['args'])
                    else:
                        self._BotsData[child.attrib['file']] = (child.attrib['module'], child.attrib['classname'])
                return True
            except:
                return False
        else:
            return False
    def _InstanceCreator(self,filename,data):
        result=None
        sys.path.append(os.path.dirname(filename))
        try:
            module = importlib.import_module(data[0])
            class_=getattr(module,data[1])
            if (len(data)>2):
                result=class_(data[2])
            else:
                result = class_()
        except ImportError:
            print ("unable to load module:" + filename)
            return (None)
        return result

