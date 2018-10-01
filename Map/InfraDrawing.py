from enum import Enum

class DisplayModeEnum(Enum):
    Controlling = 1
    Controlled = 2
    Acceable=3

import numpy as np
import matplotlib.pyplot
import typing
from Common.Point import  Point
from matplotlib.widgets import Button,RadioButtons
from Map.MapHolder import MapHolder

class InfraDrawing():
    def __init__(self, mapholder:MapHolder):

        self._mapholder=mapholder
        self._DrawInitialState()



    def _DrawInitialState(self):
        import numpy as np
        fig, ax = matplotlib.pyplot.subplots()
        matplotlib.pyplot.subplots_adjust(bottom=0.3)
        self._ax=ax
        ax.axis('tight')
        ax.axis('off')
        newmap= self._mapholder.map
        self._the_table = ax.table(cellText=np.asarray(newmap),
                             loc='center')


        class Index(object):
            def __init__(self,plttable, counterlabel, mapholder):
                self._XCounter = 0
                self._YCounter = 0
                self._CounterLabel=counterlabel
                self._mapHolder = mapholder
                self._the_table = plttable
                self._Controlling_Color = "red"
                self._Controlled_Color = "green"
                self._InRange_Color = "orange"
                self._Point_Color = "blue"
                self._map= self._mapHolder.map
                width, height =  self._mapHolder.map.shape
                self._width=width
                self._height=height
                self._DisplayModes = {}
                self._DisplayModes['controlling'] = DisplayModeEnum.Controlling
                self._DisplayModes['controlled'] = DisplayModeEnum.Controlled
                self._DisplayModes['acceable'] = DisplayModeEnum.Acceable
                self._CurrentDisplayMode = DisplayModeEnum.Controlling
                self._DrawData()




            def nextX(self, event):
                if self._XCounter == self._width-1:
                    return
                self._XCounter += 1
                self._DrawData()

            def prevX(self, event):
                if self._XCounter == 0:
                    return
                self._XCounter -= 1
                self._DrawData()


            def nextY(self, event):
                if self._YCounter == self._height-1:
                    return
                self._YCounter += 1
                self._DrawData()

            def prevY(self, event):
                if self._YCounter == 0:
                    return
                self._YCounter -= 1
                self._DrawData()
            def SetDisplayMode(self,displaymode):
                self._CurrentDisplayMode=self._DisplayModes[displaymode.lower()]
                self._DrawData()

            def _ClearCellForColor(self,x,y):
                self._the_table._cells[
                    (x, y)].set_facecolor('w')
            def _setColor(self,x,y,color):
                self._the_table._cells[
                    (y, x)].set_facecolor(color)
            def _ClearOldColoring(self):
                for outeridx in range(self._width):
                    for inneridx in range(self._height):
                        self._ClearCellForColor(outeridx,inneridx)

            def _DrawData(self):
                self._ClearOldColoring()
                self._CounterLabel.set_text("x:{0} y:{1}".format(self._XCounter,self._YCounter))
                self._setColor(self._XCounter,self._YCounter, self._Point_Color)
                if self._CurrentDisplayMode==DisplayModeEnum.Controlling:
                    cotrolledpoints = self._mapHolder.pointscontrol
                    controllingpoints=cotrolledpoints[self._XCounter][self._YCounter].controllingpoints
                    for controllingpoint in controllingpoints:
                        self._setColor(controllingpoint.x,controllingpoint.y,self._Controlling_Color)
                if self._CurrentDisplayMode == DisplayModeEnum.Controlled:
                    cotrolledpoints = self._mapHolder.pointscontrol
                    controlledpoints = cotrolledpoints[self._XCounter][self._YCounter].controlledpoints
                    for controlledpoint in controlledpoints:
                        self._setColor(controlledpoint.x, controlledpoint.y, self._Controlled_Color)
                if self._CurrentDisplayMode == DisplayModeEnum.Acceable:
                    for x in range(self._width):
                        for y in range(self._height):
                            currentpoint=Point(self._XCounter, self._YCounter)
                            examinedpoint=Point(x, y)
                            if currentpoint!=examinedpoint and self._mapHolder.mayMove(currentpoint, examinedpoint):
                                self._setColor(x,y, self._InRange_Color)

                matplotlib.pyplot.draw()

        axprev_X = matplotlib.pyplot.axes([0.6, 0.3, 0.15, 0.075])
        axnext_X = matplotlib.pyplot.axes([0.81, 0.3, 0.15, 0.075])

        axprev_Y = matplotlib.pyplot.axes([0.6, 0.15, 0.15, 0.075])
        axnext_Y = matplotlib.pyplot.axes([0.81, 0.15, 0.15, 0.075])
        bnext_X = Button(axnext_X, 'Next X')
        bprev_X = Button(axprev_X, 'Previous X')

        bnext_Y = Button(axnext_Y, 'Next Y')
        bprev_Y = Button(axprev_Y, 'Previous Y')

        self._CounterLabel = ax.text(0.9, -0.1, '', verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
                                 color='black', fontsize=15)
        callback = Index(self._the_table,self._CounterLabel,self._mapholder)
        bnext_X.on_clicked(callback.nextX)
        bprev_X.on_clicked(callback.prevX)

        bnext_Y.on_clicked(callback.nextY)
        bprev_Y.on_clicked(callback.prevY)

        radioAxes = matplotlib.pyplot.axes([0.3, 0.3, 0.2, 0.1])
        optionsradio = RadioButtons(radioAxes, ('Controlling', 'Controlled', 'Acceable'))
        optionsradio.on_clicked(callback.SetDisplayMode)

        matplotlib.pyplot.show()



