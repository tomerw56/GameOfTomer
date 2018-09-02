from unittest import TestCase
from Engine.GameDraw.GameDrawing import GameDrawing
from Map.CSVMatrixReader import CSVMatrixReader
from Engine.Common.CompleteGameState import CompleteGameState
from Common.Point import Point
import random
import os

class TestGameDrawing(TestCase):
    def test_DrawNoData(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap/Map.csv')
        csvreader=CSVMatrixReader()
        csvreader.parse(RealPath)
        drawMatch=GameDrawing(csvreader.Matrix)
        self.assertTrue(csvreader.fileLoaded, "error")
    def test_DrawAll_PrePlanned(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap/Map.csv')
        csvreader=CSVMatrixReader()
        csvreader.parse(RealPath)

        game1=CompleteGameState(100, []);
        game1.player_1_State.position=Point(0,0)
        game1.player_2_State.position = Point(9, 9)

        game2 = CompleteGameState(100, []);
        game2.player_1_State.position = Point(1, 1)
        game2.player_2_State.position = Point(2, 4)

        game3 = CompleteGameState(100, []);
        game3.player_1_State.position = Point(2, 7)
        game3.player_2_State.position = Point(9, 3)
        games=[]
        games.append(game1)
        games.append(game2)
        games.append(game3)
        drawMatch = GameDrawing(csvreader.Matrix,games)
        self.assertTrue(csvreader.fileLoaded, "error")

    def test_DrawAll_FinalState(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap/Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)

        game1 = CompleteGameState(100, []);
        game1.player_1_State.position = Point(0, 0)
        game1.player_2_State.position = Point(9, 9)

        game2 = CompleteGameState(100, []);
        game2.player_1_State.position = Point(1, 1)
        game2.player_2_State.position = Point(2, 4)

        game3 = CompleteGameState(100, []);
        game3.player_1_State.position = Point(2, 7)
        game3.player_2_State.position = Point(9, 3)
        game3.player_1_State.score=10
        game3.player_2_State.score = 20
        games = []
        games.append(game1)
        games.append(game2)
        games.append(game3)
        drawMatch = GameDrawing(csvreader.Matrix, games)
        self.assertTrue(csvreader.fileLoaded, "error")

    def test_DrawAll_FinalState_Destruction(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap/Map.csv')
        csvreader = CSVMatrixReader()
        csvreader.parse(RealPath)

        game1 = CompleteGameState(100, []);
        game1.player_1_State.position = Point(0, 0)
        game1.player_2_State.position = Point(9, 9)

        game2 = CompleteGameState(100, []);
        game2.player_1_State.position = Point(1, 1)
        game2.player_2_State.position = Point(2, 4)

        game3 = CompleteGameState(100, []);
        game3.player_1_State.position = Point(2, 7)
        game3.player_2_State.position = Point(9, 3)
        game3.player_1_State.score = 10
        game3.player_2_State.score = 20
        game3.player_2_State.destroyed=True
        games = []
        games.append(game1)
        games.append(game2)
        games.append(game3)
        drawMatch = GameDrawing(csvreader.Matrix, games)
        self.assertTrue(csvreader.fileLoaded, "error")

    def test_DrawRandomData(self):
        RealPath = os.path.join(os.path.dirname(__file__), '../Maps/TestMap/Map.csv')
        csvreader=CSVMatrixReader()
        csvreader.parse(RealPath)
        games = []
        for idx in range (100):
            game=CompleteGameState(100, []);
            self._RandomizeGame(game)
            game.playingtime=idx
            games.append(game)

        drawMatch = GameDrawing(csvreader.Matrix,games)
        self.assertTrue(csvreader.fileLoaded, "error")
    def _RandomizeGame(self,gamestate:CompleteGameState):
        gamestate.player_1_State.position=Point(random.randint(0,9),random.randint(0,9))
        gamestate.player_1_State.threatenedTime=random.randint(0,9)
        gamestate.player_1_State.threateningTime=random.randint(0,10)
        gamestate.player_1_State.score=random.randint(1,40)

        gamestate.player_2_State.position = Point(random.randint(0, 9), random.randint(0, 9))
        gamestate.player_2_State.threatenedTime = random.randint(0, 9)
        gamestate.player_2_State.threateningTime = random.randint(0, 10)
        gamestate.player_2_State.score = random.randint(1, 40)

