import numpy as np
from Engine.Common.CompleteGameState import CompleteGameState
import matplotlib.pyplot
import typing
from Common.Point import  Point
from matplotlib.widgets import Button
from Map.LosCalculator import LosCalculator

class GameDrawing():
    def __init__(self, map:np.matrix, gamestates:typing.List[CompleteGameState]=[]):
        self._map=map
        self._GameStates=gamestates

        self._DrawInitialState()


    def _DrawInitialState(self):
        import numpy as np
        fig, ax = matplotlib.pyplot.subplots()
        matplotlib.pyplot.subplots_adjust(bottom=0.2)
        self._ax=ax
        ax.axis('tight')
        ax.axis('off')
        self._the_table = ax.table(cellText=np.asarray(self._map),
                             loc='center')


        self._Counter = ax.text(0.95, 0.01, '',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=15)

        class Index(object):
            def __init__(self, plttable, counter, map, gamestates: typing.List[CompleteGameState] = []):
                self._GameStates = gamestates
                self._LosCalculator = LosCalculator()

                self._CurrentIndex = 0
                self._the_table=plttable
                self._Counter=counter
                self._Player_1_Color = "red"
                self._Player_2_Color = "green"
                self._ThreatColor = "orange"
                self._map=map
                width, height = map.shape
                self._width=width
                self._height=height
                self._PreviousPlayer_1_Location=None
                self._PreviousPlayer_2_Location = None

                self._Player1StatDrawn=False
                self._Player2StatDrawn = False
                self._Player_1_threatenedTime=None
                self._Player_1_threateningTime = None

                self._Player_1_timeinposition = None
                self._Player_1_threatened = None
                self._Player_1_destroyed = None
                self._Player_1_score = None

                self._Player_2_threatenedTime = None
                self._Player_2_threateningTime = None

                self._Player_2_timeinposition = None
                self._Player_2_threatened = None
                self._Player_2_destroyed = None
                self._Player_2_score = None
                self._FinalScore=None
                self._Destruction=None




                if(len(gamestates)!=0):
                    self._DrawState(self._GameStates[0])
                    self._PreviousPlayer_1_Location = self._GameStates[0].player_1_State.position
                    self._PreviousPlayer_2_Location = self._GameStates[0].player_2_State.position

            def next(self, event):
                if len(self._GameStates) == 0:
                    return
                self._CurrentIndex += 1
                if (self._CurrentIndex > len(self._GameStates) - 1):
                    self._CurrentIndex = len(self._GameStates) - 1
                self._DrawState(self._GameStates[self._CurrentIndex])
                self._PreviousPlayer_1_Location = self._GameStates[self._CurrentIndex].player_1_State.position
                self._PreviousPlayer_2_Location = self._GameStates[self._CurrentIndex].player_2_State.position

            def prev(self, event):
                if len(self._GameStates) == 0:
                    return
                self._CurrentIndex -= 1
                if (self._CurrentIndex < 0):
                    self._CurrentIndex = 0
                self._DrawState(self._GameStates[self._CurrentIndex])
                self._PreviousPlayer_1_Location = self._GameStates[self._CurrentIndex].player_1_State.position
                self._PreviousPlayer_2_Location = self._GameStates[self._CurrentIndex].player_2_State.position

            def _ClearCellForColor(self,x,y):
                self._the_table._cells[
                    (x, y)].set_facecolor('w')
            def _ClearOldColoring(self):
                for outeridx in range(self._width):
                    for inneridx in range(self._height):
                        self._ClearCellForColor(outeridx,inneridx)

            def _DrawState(self, gamestate: CompleteGameState):
                self._ClearOldColoring()

                self._Counter.set_text("Step: {0}".format(self._CurrentIndex))
                self._the_table._cells[
                    (gamestate.player_1_State.position.x, gamestate.player_1_State.position.y)].set_facecolor(self._Player_1_Color)
                self._the_table._cells[
                    (gamestate.player_2_State.position.x, gamestate.player_2_State.position.y)].set_facecolor(self._Player_2_Color)


                if(gamestate.player_2_State.threatened or gamestate.player_1_State.threatened):
                    pointlist=self._LosCalculator.getLosList(gamestate.player_1_State.position,gamestate.player_2_State.position)
                    if(len(pointlist)>2):
                        lastindex=len(pointlist)-2
                        for idx in range(0,lastindex):
                            self._the_table._cells[pointlist[idx].x,pointlist[idx].y].set_facecolor(self._ThreatColor)



                if(self._FinalScore == None):
                    self._FinalScore=ax.text(0.1, 0.95, '',
                                                            verticalalignment='bottom', horizontalalignment='left',
                                                            transform=ax.transAxes,
                                                            color='Black', fontsize=15)
                    self._FinalScore.visible=False
                self._FinalScore.set_text("Player 1 [{0}] Player 2 [{1}]".format(gamestate.player_1_State.score,
                                                                                 gamestate.player_2_State.score))
                self._FinalScore.set_visible(self._CurrentIndex == len(self._GameStates) - 1)

                if (self._Destruction == None):
                    self._Destruction = ax.text(0.1, 0.80, '',
                                               verticalalignment='bottom', horizontalalignment='left',
                                               transform=ax.transAxes,
                                               color='Black', fontsize=20)
                    self._Destruction.visible = False

                self._Destruction.set_visible(False)
                if gamestate.player_1_State.destroyed:
                    self._Destruction.set_text("Player 1 Destroyed")
                    self._Destruction.set_color(self._Player_1_Color)
                    self._Destruction.set_visible(True)
                if gamestate.player_2_State.destroyed:
                    self._Destruction.set_text("Player 2 Destroyed")
                    self._Destruction.set_color(self._Player_2_Color)
                    self._Destruction.set_visible(True)


                if(not self._Player1StatDrawn):
                    self._Player1StatDrawn = True
                    ax.text(0.1, 0.2, 'Player 1',
                            verticalalignment='bottom', horizontalalignment='left',
                            transform=ax.transAxes,
                            color=self._Player_1_Color, fontsize=6)
                    self._Player_1_threatenedTime =  ax.text(0.1, 0.17, '',
                                        verticalalignment='bottom', horizontalalignment='left',
                                        transform=ax.transAxes,
                                        color=self._Player_1_Color, fontsize=6)

                    self._Player_1_threateningTime = ax.text(0.1, 0.14, '',
                                                            verticalalignment='bottom', horizontalalignment='left',
                                                            transform=ax.transAxes,
                                                            color=self._Player_1_Color, fontsize=6)
                    self._Player_1_timeinposition = ax.text(0.1, 0.11, '',
                                                            verticalalignment='bottom', horizontalalignment='left',
                                                            transform=ax.transAxes,
                                                            color=self._Player_1_Color, fontsize=6)
                    self._Player_1_threatened = ax.text(0.1, 0.08 ,'',
                                                            verticalalignment='bottom', horizontalalignment='left',
                                                            transform=ax.transAxes,
                                                            color=self._Player_1_Color, fontsize=6)
                    self._Player_1_destroyed = ax.text(0.1, 0.05, '',
                                                            verticalalignment='bottom', horizontalalignment='left',
                                                            transform=ax.transAxes,
                                                            color=self._Player_1_Color, fontsize=6)
                    self._Player_1_score = ax.text(0.1, 0.02, '',
                                                       verticalalignment='bottom', horizontalalignment='left',
                                                       transform=ax.transAxes,
                                                       color=self._Player_1_Color, fontsize=6)

                if (not self._Player2StatDrawn):
                    self._Player2StatDrawn = True
                    ax.text(0.4, 0.2, 'Player 2',
                            verticalalignment='bottom', horizontalalignment='left',
                            transform=ax.transAxes,
                            color=self._Player_2_Color, fontsize=6)
                    self._Player_2_threatenedTime = ax.text(0.4, 0.17, '',
                                                            verticalalignment='bottom', horizontalalignment='left',
                                                            transform=ax.transAxes,
                                                            color=self._Player_2_Color, fontsize=6)

                    self._Player_2_threateningTime = ax.text(0.4, 0.14, '',
                                                             verticalalignment='bottom', horizontalalignment='left',
                                                             transform=ax.transAxes,
                                                             color=self._Player_2_Color, fontsize=6)

                    self._Player_2_timeinposition = ax.text(0.4, 0.11, '',
                                                            verticalalignment='bottom', horizontalalignment='left',
                                                            transform=ax.transAxes,
                                                            color=self._Player_2_Color, fontsize=6)
                    self._Player_2_threatened = ax.text(0.4, 0.08, '',
                                                        verticalalignment='bottom', horizontalalignment='left',
                                                        transform=ax.transAxes,
                                                        color=self._Player_2_Color, fontsize=6)
                    self._Player_2_destroyed = ax.text(0.4, 0.05, '',
                                                       verticalalignment='bottom', horizontalalignment='left',
                                                       transform=ax.transAxes,
                                                       color=self._Player_2_Color, fontsize=6)
                    self._Player_2_score = ax.text(0.4, 0.02, '',
                                                   verticalalignment='bottom', horizontalalignment='left',
                                                   transform=ax.transAxes,
                                                   color=self._Player_2_Color, fontsize=6)
                self._Player_1_threatenedTime.set_text("threatenedTime: {0}".format(gamestate.player_1_State.threatenedTime))
                self._Player_1_threateningTime.set_text("threateningTime: {0}".format(gamestate.player_1_State.threateningTime))
                self._Player_1_timeinposition.set_text("timeinposition: {0}".format(gamestate.player_1_State.timeinposition))
                self._Player_1_threatened.set_text("threatened: {0}".format(gamestate.player_1_State.threatened))
                self._Player_1_destroyed.set_text("destroyed: {0}".format(gamestate.player_1_State.destroyed))
                self._Player_1_score.set_text("score: {0}".format(gamestate.player_1_State.score))
                self._Player_2_threatenedTime.set_text(
                    "threatenedTime: {0}".format(gamestate.player_2_State.threatenedTime))
                self._Player_2_threateningTime.set_text(
                    "threateningTime: {0}".format(gamestate.player_2_State.threateningTime))
                self._Player_2_timeinposition.set_text(
                    "timeinposition: {0}".format(gamestate.player_2_State.timeinposition))
                self._Player_2_threatened.set_text("threatened: {0}".format(gamestate.player_2_State.threatened))
                self._Player_2_destroyed.set_text("destroyed: {0}".format(gamestate.player_2_State.destroyed))
                self._Player_2_score.set_text("score: {0}".format(gamestate.player_2_State.score))
                matplotlib.pyplot.draw()
        axprev = matplotlib.pyplot.axes([0.7, 0.05, 0.1, 0.075])
        axnext = matplotlib.pyplot.axes([0.81, 0.05, 0.1, 0.075])

        callback = Index(self._the_table,self._Counter,self._map,self._GameStates)
        bnext = Button(axnext, 'Next')
        bnext.on_clicked(callback.next)
        bprev = Button(axprev, 'Previous')
        bprev.on_clicked(callback.prev)

        matplotlib.pyplot.show()






