import numpy as np

from Common.Dimensions import Dimensions
from Common.Point import Point
from Common.Constant import Constants
import networkx as nx
import os
import io
import jsonpickle
import matplotlib.pyplot as plt
from Common.PathResult import PathResult
from Map.CSVMatrixReader import CSVMatrixReader
from Map.MovementCalculator import MovementCalculator
from Map.LosCalculator import LosCalculator
from Common.PointsControl import PointsControl
from networkx.readwrite import json_graph
import sys
import json

class MapHolder:
    def __init__(self,configProvider):
        self._GraphLoaded = False
        self._Consts=Constants()
        self._ConfigProvider=configProvider
        self._MovementCalculator=MovementCalculator(configProvider)
        self._Csvreader=CSVMatrixReader()
        self._LosCalculator = LosCalculator()
        self._GraphLoaded=False
        self._DrawGraphs=bool(self._ConfigProvider.getValue('Game.Config', 'DrawMapHolderGraph').lower() in ("true"))


    def loadMap(self,mapname):
        self._Csvreader.parse(mapname)
        if  self._Csvreader.fileLoaded:
            self._GraphLoaded =self._LoadData(mapname)
        self._Mapname = mapname
        return  self._Csvreader.fileLoaded and  self._GraphLoaded

    def _LoadData(self,mapname):
        try:
            self._PointsControl= {}
            controllingPointsfile=os.path.join(os.path.dirname(mapname), self._Consts.ControllingPointsFileName)
            print("Attempting to load {} form controllingpoints".format(controllingPointsfile))
            with io.open(controllingPointsfile, 'r') as f:
                controllingpoints_frozenstate = f.read()
                tempDict = jsonpickle.decode(controllingpoints_frozenstate)
                dim=self.getMapDim()
                for RowIndex in range(0, dim.width):
                    self._PointsControl[RowIndex] = {}
                    for ColIndex in range(0, dim.height):
                         self._PointsControl[RowIndex][ColIndex]=tempDict['{}'.format(RowIndex)]['{}'.format(ColIndex)]
            movementgraphname = os.path.join(os.path.dirname(mapname), self._Consts.MovementGraphFileName)
            print("Attempting to load {} form movementgraphname".format(movementgraphname))
            with io.open(movementgraphname, 'r') as f:
                movementgraph_frozenstate = f.read()
                dumps=jsonpickle.decode(movementgraph_frozenstate)
                self._Graph = json_graph.node_link_graph(dumps)

            safepointsfilename = os.path.join(os.path.dirname(mapname), self._Consts.SafePointsFileName)
            print("Attempting to load {} form safepointsfilename".format(safepointsfilename))
            self._SafePoints = []
            with io.open(safepointsfilename, 'r') as f:
                safepoints_frozenstate = f.read()
                self._SafePoints = jsonpickle.decode(safepoints_frozenstate)
            return True
        except:
            print(sys.exc_info())
            return False
    def drawGraph(self):
        if self._GraphLoaded:
            graph_pos = nx.shell_layout(self._Graph)
            nx.draw_networkx_nodes(self._Graph, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
            nx.draw_networkx_edges(self._Graph, graph_pos)
            labels = {}
            for Idx in range(0,len(self._Graph.nodes().keys())):
                labels[Idx] = "({0}-{1})".format(self._Graph.nodes[Idx]["X"], self._Graph.nodes[Idx]["Y"])
            nx.draw_networkx_labels(self._Graph, graph_pos,labels=labels, font_size=12, font_family='sans-serif')
            plt.show()

    def getMapDim(self):
        dim=Dimensions(0,0)
        if  self._Csvreader.fileLoaded:
            dim.width,dim.height=self._Csvreader.Matrix.shape
        return dim

    def mayMove(self,pFrom:Point,pTo:Point):
        if not self._Csvreader.fileLoaded:
            return False
        if not self._GraphLoaded:
            return False
        dim=self.getMapDim()
        if dim.IsPointInDim(pFrom)==False:
            return False
        if dim.IsPointInDim(pTo)==False:
            return False
        NodeFrom = Point.ToGridNodeFromPoint(pFrom, dim.height)
        NodeTo = Point.ToGridNodeFromPoint(pTo, dim.height)

        return self._MovementCalculator.mayMove(NodeFrom,NodeTo,self._Graph)
    def isLOS(self,pFrom:Point,pTo:Point):
        if not self._Csvreader.fileLoaded:
            return False
        if not self._GraphLoaded:
            return False
        dim=self.getMapDim()
        if dim.IsPointInDim(pFrom)==False:
            return False
        if dim.IsPointInDim(pTo)==False:
            return False
        return self._LosCalculator.IsLos(pFrom,pTo,self._Csvreader.Matrix)

    def getPath(self,pFrom:Point,pTo:Point):
        if not self._Csvreader.fileLoaded:
            return PathResult([],False)
        if not self._GraphLoaded:
            return  PathResult([],False)
        dim=self.getMapDim()
        if dim.IsPointInDim(pFrom)==False:
            return  PathResult([],False)
        if dim.IsPointInDim(pTo)==False:
            return  PathResult([],False)
        if(pFrom==pTo):
            return PathResult(pTo,True)
        NodeFrom = Point.ToGridNodeFromPoint(pFrom, dim.height)
        NodeTo = Point.ToGridNodeFromPoint(pTo, dim.height)
        path=self._MovementCalculator.getPath(NodeFrom,NodeTo,self._Graph)
        if self._DrawGraphs and path.valid:
            # we set connectivity
            drawingGraph=nx.Graph()
            for idx in range(len(path.nodelist)):

                drawingGraph.add_node(idx)
                drawingGraph.nodes[idx]["X"] = path.points[idx].x
                drawingGraph.nodes[idx]["Y"] = path.points[idx].y
                drawingGraph.nodes[idx]["RealID"] = path.nodelist[idx]

            for idx in range(len(path.nodelist)):
                for inneridx in range(len(path.nodelist)):
                    if(idx!=inneridx and self._Graph.has_edge(path.nodelist[idx],path.nodelist[inneridx])):
                        drawingGraph.add_edge(idx,inneridx, weight=self._Consts.ConnectedGraphVertexWeight)

            graph_pos = nx.shell_layout(drawingGraph)
            nx.draw_networkx_nodes(drawingGraph, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
            nx.draw_networkx_edges(drawingGraph, graph_pos)
            labels = {}
            for Idx in range(0, len(drawingGraph.nodes().keys())):
                labels[Idx] = "({0}-{1})".format(drawingGraph.nodes[Idx]["X"],drawingGraph.nodes[Idx]["Y"])
            nx.draw_networkx_labels(drawingGraph, graph_pos, labels=labels, font_size=12, font_family='sans-serif')
            plt.show()
        return path

    def getAlt(self,location:Point):
        dim = self.getMapDim()
        if dim.IsPointInDim(location) == False:
            return self._Consts.InValidAlt
        nodeloc = Point.ToGridNodeFromPoint(location, dim.height)
        return self._Csvreader.Matrix.item(nodeloc)

    def isCloseToSafty(self, location: Point):
        for safty in self._SafePoints:
            pathresult=self.getPath(location,safty)
            if pathresult.valid and pathresult.length<=self._Consts.saftypointCloseRange:
                return True
        return False

    def isSafePoint(self, location: Point):
        for safty in self._SafePoints:
            if safty==location:
                return True
        return False
    @property
    def mapLoaded(self):
        return  self._Csvreader.fileLoaded
    @property
    def graphLoaded(self):
        return self._GraphLoaded
    @property
    def map(self):
        return self._Csvreader.Matrix
    @property
    def pointscontrol(self):
        return self._PointsControl
    @property
    def saftypoints(self):
        return  self._SafePoints





