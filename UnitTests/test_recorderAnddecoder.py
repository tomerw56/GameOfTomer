from unittest import TestCase
from Utils.UnitTestDummyConfigProvider import UnitTestDummyConfigProvider
from Engine.Recording.Recorder import Recorder
from Engine.Recording.Decoder import Decoder
from Engine.Common.CompleteGameState import CompleteGameState
from Engine.Common.GameMetaData import GameMetaData
from Engine.Common.RestPointState import RestPointState
from time import sleep
from Common.Point import Point
import os
import json
from Engine.GameDraw.GameDrawing import GameDrawing
from Map.CSVMatrixReader import CSVMatrixReader
import random

class TestRecordering(TestCase):
    def test_Record_Write(self):
        ConfigProvider = UnitTestDummyConfigProvider()

        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')
        gamestate=CompleteGameState(100)
        gamestate.playingtime=1
        gamestate.player_1_GameState.position=Point(1,1)
        gamestate.player_1_GameState.score=10
        gamestate.player_2_GameState.position = Point(2, 2)
        gamestate.player_2_GameState.score=20
        gamestate.player_1_GameState.timeinposition=4
        gamestate.player_2_GameState.timeinposition=5
        gamemetadata=GameMetaData("MyPath");
        recorder=Recorder(ConfigProvider)

        sleep(2)  # Time in seconds.
        filedir=recorder.Record(gamestate)
        # Read JSON file
        with open(filedir) as data_file:
            data_loaded = json.load(data_file)
        self.assertTrue(data_loaded!="")

    def test_Record_WriteMetadata(self):
        ConfigProvider = UnitTestDummyConfigProvider()

        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')

        gamemetadata = GameMetaData("MyPath");
        recorder = Recorder(ConfigProvider)

        sleep(2)  # Time in seconds.
        filedir = recorder.WriteMetadata(gamemetadata)
        # Read JSON file
        with open(filedir) as data_file:
            data_loaded = json.load(data_file)
        self.assertTrue(data_loaded != "")

    def test_Record_N0_Write(self):
        ConfigProvider = UnitTestDummyConfigProvider()

        ConfigProvider.addValue('Recording', 'record', 'False')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')
        gamestate=CompleteGameState(100)
        gamestate.playingtime=1
        gamestate.player_1_GameState.position=Point(1,1)
        gamestate.player_1_GameState.score=10
        gamestate.player_2_GameState.position = Point(2, 2)
        gamestate.player_2_GameState.score=20
        gamestate.player_1_GameState.timeinposition=4
        gamestate.player_2_GameState.timeinposition=5

        sleep(2)  # Time in seconds.
        recorder=Recorder(ConfigProvider)
        filedir=recorder.Record(gamestate)

        # Read JSON filE
        self.assertTrue(filedir=="")

    def test_Decoder_InvalidPath(self):
        ConfigProvider = UnitTestDummyConfigProvider()
        decoder = Decoder('c:\\NoFolder')
        self.assertFalse(decoder.valid)

    def test_Decoder_InvalidPath_DcodeAll(self):
        ConfigProvider = UnitTestDummyConfigProvider()
        decoder = Decoder( 'c:\\NoFolder')
        self.assertTrue(len(decoder.DecodeAllStates())==0)

    def test_Decoder_InvalidPath_Dcode(self):
        ConfigProvider = UnitTestDummyConfigProvider()
        decoder = Decoder( 'c:\\NoFolder')
        self.assertTrue(decoder.DecodeStep(100)  is None)

    def test_Decoder_ValidPath_DcodeMetaData(self):
        metadatapath="SomePath"
        ConfigProvider = UnitTestDummyConfigProvider()
        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')
        metadata=GameMetaData(metadatapath)
        recorder = Recorder(ConfigProvider)
        filedir =recorder.WriteMetadata(metadata)
        sleep(2)  # Time in seconds.
        folder = os.path.dirname(filedir)
        decoder = Decoder(folder)

        decodedmetadata=decoder.DecodeMetaData()

        self.assertTrue(decodedmetadata.infrapath ==metadatapath)

    def test_Decoder_ValidPath_DcodeMetaDataAndStates(self):
        metadatapath="SomePath"
        ConfigProvider = UnitTestDummyConfigProvider()
        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')

        restpoints = []
        restpoints.append(RestPointState(Point(1, 2)))
        restpoints.append(RestPointState(Point(2, 7)))
        gamestate = CompleteGameState(100, restpoints)
        gamestate.playingtime = 1
        gamestate.player_1_GameState.position = Point(1, 1)
        gamestate.player_1_GameState.score = 10
        gamestate.player_2_GameState.position = Point(2, 2)
        gamestate.player_2_GameState.score = 20
        gamestate.player_1_GameState.timeinposition = 4
        gamestate.player_2_GameState.timeinposition = 5

        recorder = Recorder(ConfigProvider)
        filedir = recorder.Record(gamestate)
        gamestate.playingtime = 2
        filedir = recorder.Record(gamestate)
        gamestate.playingtime = 3
        filedir = recorder.Record(gamestate)
        folder = os.path.dirname(filedir)

        metadata=GameMetaData(metadatapath)
        recorder.WriteMetadata(metadata)
        sleep(2)  # Time in seconds.
        folder = os.path.dirname(filedir)
        decoder = Decoder(folder)
        gamestates = decoder.DecodeAllStates()

        decodedmetadata=decoder.DecodeMetaData()

        self.assertTrue(len(gamestates) == 3)
        self.assertTrue(gamestates[0].playingtime == 1)
        self.assertTrue(gamestates[1].playingtime == 2)
        self.assertTrue(gamestates[2].playingtime == 3)
        self.assertTrue(len(gamestates[0].RestingPoints) == 2)
        self.assertTrue(gamestates[0].RestingPoints[0].position.x == 1)
        self.assertTrue(gamestates[0].RestingPoints[1].position.x == 2)

        self.assertTrue(decodedmetadata.infrapath ==metadatapath)



    def test_Decoder_ValidPath_DcodeAll(self):

        ConfigProvider = UnitTestDummyConfigProvider()
        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')
        restpoints=[]
        restpoints.append(RestPointState(Point(1,2)))
        restpoints.append(RestPointState(Point(2, 7)))
        gamestate = CompleteGameState(100,restpoints)
        gamestate.playingtime = 1
        gamestate.player_1_GameState.position = Point(1, 1)
        gamestate.player_1_GameState.score = 10
        gamestate.player_2_GameState.position = Point(2, 2)
        gamestate.player_2_GameState.score = 20
        gamestate.player_1_GameState.timeinposition = 4
        gamestate.player_2_GameState.timeinposition = 5



        sleep(2)  # Time in seconds.
        recorder = Recorder(ConfigProvider)
        filedir = recorder.Record(gamestate)
        gamestate.playingtime = 2
        filedir = recorder.Record(gamestate)
        gamestate.playingtime = 3
        filedir = recorder.Record(gamestate)
        folder=os.path.dirname(filedir)

        decoder = Decoder(folder)
        gamestates=decoder.DecodeAllStates()

        self.assertTrue(len(gamestates)==3)
        self.assertTrue(gamestates[0].playingtime == 1)
        self.assertTrue(gamestates[1].playingtime == 2)
        self.assertTrue(gamestates[2].playingtime == 3)
        self.assertTrue(len(gamestates[0].RestingPoints) == 2)
        self.assertTrue(gamestates[0].RestingPoints[0].position.x == 1)
        self.assertTrue(gamestates[0].RestingPoints[1].position.x == 2)

    def test_Decoder_Dcode_And_Draw(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap.csv')

        ConfigProvider = UnitTestDummyConfigProvider()
        ConfigProvider.addValue('Recording', 'record', 'True')
        ConfigProvider.addValue('Recording', 'folder', 'c:\TestJson')

        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)
        restpoints = []
        restpoints.append(RestPointState(Point(1, 2)))
        restpoints.append(RestPointState(Point(2, 7)))
        recorder = Recorder(ConfigProvider)
        metadata = GameMetaData(RealPath)
        recorder.WriteMetadata(metadata)

        for idx in range(100):
            game = CompleteGameState(100, restpoints);
            self._RandomizeGame(game)
            game.playingtime = idx
            filedir=recorder.Record(game)

        sleep(1)  # Time in seconds.

        folder = os.path.dirname(filedir)
        decoder = Decoder(folder)
        gamestates = decoder.DecodeAllStates()
        drawMatch = GameDrawing(csvreader.Matrix, gamestates)



    def _RandomizeGame(self, gamestate: CompleteGameState):
        gamestate.player_1_State.position = Point(random.randint(0, 9), random.randint(0, 9))
        gamestate.player_1_State.threatenedTime = random.randint(0, 9)
        gamestate.player_1_State.threateningTime = random.randint(0, 10)
        gamestate.player_1_State.score = random.randint(1, 40)

        gamestate.player_2_State.position = Point(random.randint(0, 9), random.randint(0, 9))
        gamestate.player_2_State.threatenedTime = random.randint(0, 9)
        gamestate.player_2_State.threateningTime = random.randint(0, 10)
        gamestate.player_2_State.score = random.randint(1, 40)