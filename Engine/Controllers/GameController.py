from Utils.ConfigProvider import ConfigProvider
from Engine.Recording.Recorder import Recorder
from Engine.Common.Facade.PlayerFacade import PlayerFacade
from Engine.GameEngine import PlayerEngine
from Engine.Common.CompleteGameState import CompleteGameState
from Common.MovmentCommand import MovementCommand
from Engine.Common.GameState import GameState
from Common.Point import Point
from Engine.Common.RestPointState import RestPointState
from Map.MapHolder import MapHolder
class GameController:
    def __init__(self,configProvider:ConfigProvider,player1:PlayerFacade,player2:PlayerFacade):
        self._Player1=player1
        self._Player2=player2
        self._ConfigProvider=configProvider
        self._Recorder=Recorder(self._ConfigProvider)

        if not self._InitMapHolder():
            self._Valid=False
            return
        self._InitController();
        self._InitGameState()
        self._InitPlayers()

        self._Valid=True

    def _InitController(self):
        self._TotalPlayTime =self._ConfigProvider.getValue("Game.Config","MapFileName")
        self._CurrentPlayTime=0
        self._RestPoints=[]
        for restpointlocation in self._MapHolder.restPointsLocations:
            self._RestPoints.append(RestPointState(restpointlocation))
    def _InitMapHolder(self):
        self._MapHolder=MapHolder(self._ConfigProvider)
        self._MapHolder.loadMap(self._ConfigProvider.getValue("Game.Config","MapFileName"))
        return self._MapHolder.graphLoaded  & self._MapHolder.graphLoaded

    def _InitGameState(self):
        self._CompleteGameState=CompleteGameState(self._ConfigProvider.getValue("Game.Config","TotalPlayTime"), self._RestPoints);

    def _InitPlayers(self):
        self._CompleteGameState.player_1_State.position=Point(self._ConfigProvider.getValue("Player1.Config","StartPositionX"),
                                          self._ConfigProvider.getValue("Player1.Config","StartPositionY"))

        self._CompleteGameState.player_2_State.position = Point(self._ConfigProvider.getValue("Player2.Config", "StartPositionX"),
                                            self._ConfigProvider.getValue("Player2.Config", "StartPositionY"))

        self._Player_1_Engine=PlayerEngine(self._CompleteGameState.player_1_GameState,self._ConfigProvider,self._MapHolder)
        self._Player_2_Engine = PlayerEngine(self._CompleteGameState.player_2_GameState, self._ConfigProvider, self._MapHolder)
    def Run(self):
        while self._CurrentPlayTime < self._TotalPlayTime:
            self._Recorder.Record(self._CompleteGameState)
            Player_1_MovementCommand =self._Player1.DoTurn(self._Player_1_Engine)
            Player_2_MovementCommand = self._Player2.DoTurn(self._Player_2_Engine)
            self._UpdateBoradAccordingToMovments(Player_1_MovementCommand,Player_2_MovementCommand)
            self.self._CompleteGameState.playingtime=self._CurrentPlayTime;
            self._CurrentPlayTime += 1
    def _UpdateBoradAccordingToMovments(self,Player_1_MovementCommand:MovementCommand,Player_2_MovementCommand:MovementCommand):
        pass
    @property
    def valid(self):
        return self._Valid









