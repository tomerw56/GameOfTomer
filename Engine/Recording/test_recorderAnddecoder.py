from unittest import TestCase
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider
from Engine.Recording.Recorder import Recorder
from Engine.Recording.Decoder import Decoder
from Engine.Common.GameState import GameState
from Engine.Common.RestPointState import RestPointState
from time import sleep
from Common.Point import Point
import os
import json

class TestRecordering(TestCase):
    def test_Record_Write(self):
        ConfigProvider = UnitTestDummyConfigProvider()

        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')
        gamestate=GameState(100)
        gamestate.playingtime=1
        gamestate.player1.position=Point(1,1)
        gamestate.player1.score=10
        gamestate.player2.position = Point(2, 2)
        gamestate.player2.score=20
        gamestate.player1.timeinposition=4
        gamestate.player2.timeinposition=5

        recorder=Recorder(ConfigProvider)

        sleep(2)  # Time in seconds.
        filedir=recorder.Record(gamestate)
        # Read JSON file
        with open(filedir) as data_file:
            data_loaded = json.load(data_file)
        self.assertTrue(data_loaded!="")

    def test_Record_N0_Write(self):
        ConfigProvider = UnitTestDummyConfigProvider()

        ConfigProvider.addValue('Recording', 'record', 'False')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')
        gamestate=GameState(100)
        gamestate.playingtime=1
        gamestate.player1.position=Point(1,1)
        gamestate.player1.score=10
        gamestate.player2.position = Point(2, 2)
        gamestate.player2.score=20
        gamestate.player1.timeinposition=4
        gamestate.player2.timeinposition=5

        sleep(2)  # Time in seconds.
        recorder=Recorder(ConfigProvider)
        filedir=recorder.Record(gamestate)

        # Read JSON filE
        self.assertTrue(filedir=="")

    def test_Decoder_InvalidPath(self):
        ConfigProvider = UnitTestDummyConfigProvider()
        decoder = Decoder(ConfigProvider,'c:\\NoFolder')
        self.assertFalse(decoder.valid)

    def test_Decoder_InvalidPath_DcodeAll(self):
        ConfigProvider = UnitTestDummyConfigProvider()
        decoder = Decoder(ConfigProvider, 'c:\\NoFolder')
        self.assertTrue(len(decoder.DecodeAllStates())==0)

    def test_Decoder_InvalidPath_Dcode(self):
        ConfigProvider = UnitTestDummyConfigProvider()
        decoder = Decoder(ConfigProvider, 'c:\\NoFolder')
        self.assertTrue(decoder.DecodeStep(100)  is None)

    def test_Decoder_ValidPath_DcodeAll(self):
        ConfigProvider = UnitTestDummyConfigProvider()
        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')
        restpoints=[]
        restpoints.append(RestPointState(Point(1,2)))
        restpoints.append(RestPointState(Point(2, 7)))
        gamestate = GameState(100,restpoints)
        gamestate.playingtime = 1
        gamestate.player1.position = Point(1, 1)
        gamestate.player1.score = 10
        gamestate.player2.position = Point(2, 2)
        gamestate.player2.score = 20
        gamestate.player1.timeinposition = 4
        gamestate.player2.timeinposition = 5

        sleep(2)  # Time in seconds.
        recorder = Recorder(ConfigProvider)
        filedir = recorder.Record(gamestate)
        gamestate.playingtime = 2
        filedir = recorder.Record(gamestate)
        gamestate.playingtime = 3
        filedir = recorder.Record(gamestate)
        folder=os.path.dirname(filedir)
        decoder = Decoder(ConfigProvider,folder)
        gamestates=decoder.DecodeAllStates()

        self.assertTrue(len(gamestates)==3)
        self.assertTrue(gamestates[0].playingtime == 1)
        self.assertTrue(gamestates[1].playingtime == 2)
        self.assertTrue(gamestates[2].playingtime == 3)
        self.assertTrue(len(gamestates[0].RestingPoints) == 2)
        self.assertTrue(gamestates[0].RestingPoints[0].position.x == 1)
        self.assertTrue(gamestates[0].RestingPoints[1].position.x == 2)