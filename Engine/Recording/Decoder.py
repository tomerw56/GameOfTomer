from Utils.ConfigProvider import ConfigProvider
from Engine.Common.CompleteGameState import CompleteGameState
from Engine.Common.GameMetaData import GameMetaData
import os
from os import listdir
from os.path import isfile, join
import datetime
import jsonpickle
import io
import re
from Common.Constant import Constants
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set


class Decoder:
    def __init__(self,path):
        self._Constants=Constants()
        self._Path=path
        self._Valid=False
        self._Initialize()

    def _Initialize(self):
        self._Valid=os.path.exists(self._Path)
        print('Decoder Validity is {0}'.format(self._Valid))


    def _IsMetaDataFile(self,filename):
        return (re.match(filename,self._Constants.RecordGameMetaDataFileName))

    def DecodeAllStates(self)->List[CompleteGameState]:
        gamestates=[];
        if not self._Valid:
            return gamestates;
        onlyfiles = [f for f in listdir(self._Path) if isfile(join(self._Path, f))]
        for i in range(0,len(onlyfiles)):
            if self._IsMetaDataFile(onlyfiles[i]):
                continue
            with io.open(os.path.join(self._Path,onlyfiles[i]), 'r') as f:
                frozenstate=f.read()
                gamestate = jsonpickle.decode(frozenstate)
                gamestates.append(gamestate)
        return gamestates

    def DecodeMetaData(self)->GameMetaData:
        if not self._Valid:
            return None;
        onlyfiles = [f for f in listdir(self._Path) if isfile(join(self._Path, f))]
        for i in range(0,len(onlyfiles)):
            if not self._IsMetaDataFile(onlyfiles[i]):
                continue
            with io.open(os.path.join(self._Path,onlyfiles[i]), 'r') as f:
                frozenstate=f.read()
                metadata = jsonpickle.decode(frozenstate)
                return metadata

    def DecodeStep(self,step)->CompleteGameState:
        gamestate=None
        if not self._Valid:
            return gamestate;
        filedir = os.path.join(self._Path, "Step_{0}.json".format(step))
        if not os.path.exists(filedir):
            print('file {0} not found'.format(filedir))
            return gamestate;


        with io.open(filedir, 'r') as f:
            frozenstate=f.read()
            gamestate = jsonpickle.decode(frozenstate)
            return gamestate
    @property
    def valid(self):
        return self._Valid