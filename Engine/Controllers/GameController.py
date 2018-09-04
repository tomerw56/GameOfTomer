from Utils.ConfigProvider import ConfigProvider
from Engine.Recording.Recorder import Recorder
from Engine.Common.Facade.PlayerFacade import PlayerFacade
from Engine.GameEngine.PlayerEngine import PlayerEngine
from Engine.Common.CompleteGameState import CompleteGameState
from Common.MovmentCommand import MovementCommand
from Engine.Common.GameState import GameState
from Common.Point import Point
import sys
from Engine.Common.PlayerState import PlayerState
from Engine.Common.Facade.Enums import WinnigPlayer
from Engine.Common.Facade.Enums import WinnigReason
from Engine.Controllers.ThreatController import ThreatController
from Engine.Controllers.NoMovementController import NoMovementController
from Engine.Controllers.ControllersEnums import PlayerThreatState
from Engine.Controllers.ControllersEnums import PlayerNoMovmentState
from Engine.Common.Facade.VictoryAnalysis import VictoryAnalysis
from Map.MapHolder import MapHolder
from Engine.Common.GameMetaData import GameMetaData
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
        self._TotalPlayTime =int(self._ConfigProvider.getValue("Game.Config","TotalPlayTime"))
        self._CurrentPlayTime=0
        self._ThreatController=ThreatController(self._MapHolder,self._ConfigProvider)
        self._NoMovementController=NoMovementController(self._ConfigProvider)

    def _InitMapHolder(self):
        self._MapHolder=MapHolder(self._ConfigProvider)
        self._MapHolder.loadMap(self._ConfigProvider.getValue("Game.Config","MapFileName"))
        return self._MapHolder.graphLoaded  & self._MapHolder.graphLoaded

    def _InitGameState(self):
        self._CompleteGameState=CompleteGameState(self._ConfigProvider.getValue("Game.Config","TotalPlayTime"));
        self._GameMetaData=GameMetaData(self._ConfigProvider.getValue("Game.Config","MapFileName"))

    def _InitPlayers(self):
        self._CompleteGameState.player_1_State.position=Point(int(self._ConfigProvider.getValue("Player1.Config","StartPositionX")),
                                          int(self._ConfigProvider.getValue("Player1.Config","StartPositionY")))

        self._CompleteGameState.player_2_State.position = Point(int(self._ConfigProvider.getValue("Player2.Config", "StartPositionX")),
                                            int(self._ConfigProvider.getValue("Player2.Config", "StartPositionY")))

        self._Player_1_Engine=PlayerEngine(self._CompleteGameState.player_1_GameState,self._ConfigProvider,self._MapHolder)
        self._Player_2_Engine = PlayerEngine(self._CompleteGameState.player_2_GameState, self._ConfigProvider, self._MapHolder)
    def Run(self):
        while self._CurrentPlayTime < self._TotalPlayTime:
            self._Recorder.Record(self._CompleteGameState)
            if self._WasPlayerDestroyedInPreviousRound():
                return
            try:
                Player_1_MovementCommand =self._Player1.DoTurn(self._Player_1_Engine)
            except:
                print(sys.exc_info())
                self._CompleteGameState.victory.winner=WinnigPlayer.PLAYER_2
                self._CompleteGameState.victory.winningireason = WinnigReason.PLAYER_1_CRASH
                self._Recorder.Record(self._CompleteGameState)
                return
            try:
                Player_2_MovementCommand = self._Player2.DoTurn(self._Player_2_Engine)
            except:
                print(sys.exc_info())
                self._CompleteGameState.victory.winner = WinnigPlayer.PLAYER_1
                self._CompleteGameState.victory.winningireason = WinnigReason.PLAYER_2_CRASH
                self._Recorder.Record(self._CompleteGameState)
                return
            self._UpdatePlayersThreatState()
            self._UpdateBoradAccordingToMovments(Player_1_MovementCommand,Player_2_MovementCommand)
            self._CurrentPlayTime += 1
            self._CompleteGameState.playingtime=self._CurrentPlayTime;


        self._FillTimeOutVictory()


    def _WasPlayerDestroyedInPreviousRound(self)->bool:
        if self._CompleteGameState.player_1_State.destroyed and self._CompleteGameState.player_2_State.destroyed:
            self._CompleteGameState.victory.winner = WinnigPlayer.BOTH_DESTROYED
            self._CompleteGameState.victory.winningireason = WinnigReason.DESTRUCTION
            return True
        if self._CompleteGameState.player_1_State.destroyed:
            self._CompleteGameState.victory.winner = WinnigPlayer.PLAYER_2
            self._CompleteGameState.victory.winningireason = WinnigReason.DESTRUCTION
            return True
        if self._CompleteGameState.player_2_State.destroyed:
            self._CompleteGameState.victory.winner = WinnigPlayer.PLAYER_1
            self._CompleteGameState.victory.winningireason = WinnigReason.DESTRUCTION
            return True
        return False
    def _FillTimeOutVictory(self):

        if self._CompleteGameState.player_1_State.score < 0 and self._CompleteGameState.player_2_State.score < 0:
            self._CompleteGameState.victory.winner = WinnigPlayer.NO_WINNER
            self._CompleteGameState.victory.winningireason = WinnigReason.NO_WIN
            return

        if self._CompleteGameState.player_1_State.score > self._CompleteGameState.player_2_State.score:
            self._CompleteGameState.victory.winner = WinnigPlayer.PLAYER_1
            self._CompleteGameState.victory.winningireason = WinnigReason.SCORE
            return
        if self._CompleteGameState.player_1_State.score < self._CompleteGameState.player_2_State.score:
            self._CompleteGameState.victory.winner = WinnigPlayer.PLAYER_2
            self._CompleteGameState.victory.winningireason = WinnigReason.SCORE
            return
        self._CompleteGameState.victory.winningireason = WinnigReason.GAME_TIME_OUT
        self._CompleteGameState.victory.winner = WinnigPlayer.NO_WINNER

    def _UpdateBoradAccordingToMovments(self,Player_1_MovementCommand:MovementCommand,Player_2_MovementCommand:MovementCommand):
        if (Player_1_MovementCommand.pointTo == Player_2_MovementCommand.pointTo) and  (not Player_1_MovementCommand.IsEmpty) and  (not Player_2_MovementCommand.IsEmpty):
            return

        self._PerfomMovment(self._CompleteGameState.player_1_State,Player_1_MovementCommand)
        self._PerfomMovment(self._CompleteGameState.player_2_State, Player_2_MovementCommand)


        self._UpdatePlayerNoMovementPanelty(self._CompleteGameState.player_1_State)
        self._UpdatePlayerNoMovementPanelty(self._CompleteGameState.player_2_State)

    def _PerfomMovment(self,playerstate:PlayerState,movement:MovementCommand):
        if movement.IsEmpty:
            playerstate.UpdateStatesDueToNoMovement()
        else:
            if self._MapHolder.mayMove( playerstate.position,movement.pointTo):
                playerstate.UpdateStatesDueToMovement(movement.pointTo)
            else:
                playerstate.UpdateStatesDueToNoMovement()
    def _UpdatePlayerNoMovementPanelty(self,playerstate:PlayerState):
        result=self._NoMovementController.IStaticForTooLong(playerstate.position,playerstate.timeinposition)
        if result!=PlayerNoMovmentState.OK:
            playerstate.score-=1

    def _UpdatePlayersThreatState(self):
        player2ThreatState = self._ThreatController.GetPlayerThreatState(self._CompleteGameState.player_1_State,
                                                        self._CompleteGameState.player_2_State)

        self._UpdateThreatStateAccordingToThreat(self._CompleteGameState.player_1_State,
                                                    self._CompleteGameState.player_2_State,player2ThreatState)
        player1ThreatState = self._ThreatController.GetPlayerThreatState(self._CompleteGameState.player_2_State,
                                                        self._CompleteGameState.player_1_State)

        self._UpdateThreatStateAccordingToThreat(self._CompleteGameState.player_2_State,
                                             self._CompleteGameState.player_1_State, player1ThreatState)
    def _UpdateThreatStateAccordingToThreat(self,threateningPlayer:PlayerState,threatenedPlayer:PlayerState,threatstate:PlayerThreatState):
        if(threatstate==PlayerThreatState.THREATENED):
            threateningPlayer.threateningTime+=1
            threatenedPlayer.threatenedTime+=1
            threatenedPlayer.threatened=True
        if(threatstate==PlayerThreatState.DESTROYED):
            threatenedPlayer.destroyed=True
            threateningPlayer.score+=10
    @property
    def valid(self):
        return self._Valid

    @property
    def Player_1_State(self)->PlayerState:
        return self._CompleteGameState.player_1_State

    @property
    def Player_2_State(self) -> PlayerState:
        return self._CompleteGameState.player_2_State

    @property
    def VictoryReason(self)->VictoryAnalysis:
        return self._CompleteGameState.victory









