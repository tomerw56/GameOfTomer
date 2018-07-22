from Utils.ConfigProvider import ConfigProvider
from Engine.Common.GameState import GameState
import os
from os import listdir
from os.path import isfile, join
import datetime
import jsonpickle
import io
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set


class Decoder:
    def __init__(self,configProvider:ConfigProvider,path):
        self._Configuration=configProvider
        self._Path=path
        self._Valid=False
        self._Initialize()

    def _Initialize(self):
        self._Valid=os.path.exists(self._Path)
        print('Decoder Validity is {0}'.format(self._Valid))


    def DecodeAllStates(self)->List[GameState]:
        gamestates=[];
        if not self._Valid:
            return gamestates;

        onlyfiles = [f for f in listdir(self._Path) if isfile(join(self._Path, f))]
        for i in range(0,len(onlyfiles)):
            with io.open(os.path.join(self._Path,onlyfiles[i]), 'r') as f:
                frozenstate=f.read()
                gamestate = jsonpickle.decode(frozenstate)
                gamestates.append(gamestate)
        return gamestates

    def DecodeStep(self,step)->GameState:
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