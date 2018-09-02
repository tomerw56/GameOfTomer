from Map.CSVMatrixReader import CSVMatrixReader
from Map.LosCalculator import LosCalculator
import shutil
import os
from pathlib import Path
from Common.Point import  Point
from Common.Constant import Constants
from Common.Dimensions import Dimensions
import networkx as nx
from Common.PointsControl import PointsControl
from networkx.readwrite import json_graph
import json
import sys
import  io
import jsonpickle

class InfraPrepMode(object):
    def __init__(self,filename):
        self._filename=filename
        self._Csvreader = CSVMatrixReader()
        self._Valid=self._Csvreader.parse(filename)
        self._Consts=Constants()
        self._LosCalculator = LosCalculator()

    def Prep(self,destfolder)->bool:
        if(self._Valid):
            filename=Path(self._filename).name
            try:
                #copy CSV
                destfilename=os.path.join(destfolder, filename)
                if(destfilename !=self._filename ):
                    shutil.copy2(self._filename,destfilename )
                #build Graph
                self._buildGraph()
                self._SaveGraph(destfolder)
                # build Controllpoints
                self._LoadControlledPoints()
                self._SaveControllingPoints(destfolder)


            except:
                print(sys.exc_info())
                return False

        return False

    def _LoadControlledPoints(self):
        self._PointsControl={}
        dim=self._getMapDim()
        for RowIndex in range(0, dim.width):
            self._PointsControl[RowIndex] = {}
            for ColIndex in range(0, dim.height):
                self._GetControllingPointsForPoint(RowIndex,ColIndex)
    def _GetControllingPointsForPoint(self,x,y):
        dim = self._getMapDim()
        point=Point(x,y)

        pointcontrol=PointsControl(point)
        for ColIndex in range(0, dim.height):
            for RowIndex in range(0, dim.width):
                targetpoint=Point(RowIndex,ColIndex)
                if(targetpoint!=point):
                    if(self._LosCalculator.IsLos(point,targetpoint,self._Csvreader.Matrix)):
                        pointcontrol.controlledpoints.append(targetpoint)
                    if (self._LosCalculator.IsLos(targetpoint, point, self._Csvreader.Matrix)):
                        pointcontrol.controllingpoints.append(targetpoint)

        self._PointsControl[x][y]=pointcontrol

    def _SaveControllingPoints(self,destfolder):
        controllingpoints = jsonpickle.encode(self._PointsControl)

        filedir = os.path.join(destfolder, self._Consts.ControllingPointsFileName)
        with io.open(filedir, 'w') as f:
            f.write(controllingpoints)
    def _SaveGraph(self,destfolder,):
        data = json_graph.node_link_data(self._Graph)
        graph = json.dumps(data)
        filedir = os.path.join(destfolder, self._Consts.MovementGraphFileName)
        with io.open(filedir, 'w') as f:
            f.write(graph)

    def _getMapDim(self):
        dim = Dimensions(0, 0)
        if self._Csvreader.fileLoaded:
            dim.width, dim.height = self._Csvreader.Matrix.shape
        return dim

    def _buildGraph(self):
        dim = self._getMapDim()
        labels = {}
        self._Graph = nx.Graph()
        for colIndex in range(0, dim.width):
            for rowIndex in range(0, dim.height):
                cord = Point.ToGridNode(colIndex, rowIndex, dim.height)
                self._UpdateWeight(cord, colIndex, rowIndex, dim, 0, 0)
                self._UpdateWeight(cord, colIndex, rowIndex, dim, 0, 1)
                self._UpdateWeight(cord, colIndex, rowIndex, dim, 0, -1)

                self._UpdateWeight(cord, colIndex, rowIndex, dim, -1, 0)
                self._UpdateWeight(cord, colIndex, rowIndex, dim, -1, 1)
                self._UpdateWeight(cord, colIndex, rowIndex, dim, -1, -1)

                self._UpdateWeight(cord, colIndex, rowIndex, dim, 1, 0)
                self._UpdateWeight(cord, colIndex, rowIndex, dim, 1, -1)
                self._UpdateWeight(cord, colIndex, rowIndex, dim, 1, 1)
                self._Graph.nodes[cord]["X"] = colIndex
                self._Graph.nodes[cord]["Y"] = rowIndex
                labels[cord] = "({0}-{1})".format(rowIndex, colIndex)
        nx.relabel_nodes(self._Graph, labels)

    def _UpdateWeight(self, cord, colIndex, rowIndex, dim, xFactor, yFactor):
        newColIndex = colIndex + xFactor
        newRowIndex = rowIndex + yFactor

        if (newColIndex) >= dim.width:
            return
        if (newColIndex) < 0:
            return
        if (newRowIndex) >= dim.height:
            return
        if (newRowIndex) < 0:
            return
        # we try to go to Cover -not connected
        NextCord = Point.ToGridNode(newColIndex, newRowIndex, dim.height)
        if self._Csvreader.Matrix.item((colIndex, rowIndex)) == self._Consts.CoverNumber:
            return
        # we try to go from Cover -not connected

        if self._Csvreader.Matrix.item((newColIndex, newRowIndex)) == self._Consts.CoverNumber:
            return

        # Alt Diff Issue
        AltDiff = abs(
            self._Csvreader.Matrix.item((colIndex, rowIndex)) - self._Csvreader.Matrix.item((newColIndex, newRowIndex)))
        if AltDiff >= self._Consts.MaximumAltDif:
            return

        # we set connectivity
        self._Graph.add_edge(NextCord, cord, weight=self._Consts.ConnectedGraphVertexWeight)


    @property
    def valid(self) -> bool:
        return self._Valid

