import os.path
import numpy as np
import pickle

from networkx import nodes

from Common.Dimensions import Dimensions
from Common.Point import Point
from Common.Constant import Constants
import networkx as nx
import matplotlib.pyplot as plt
from Common.PathResult import PathResult
from Map.CSVMatrixReader import CSVMatrixReader
from Map.MovementCalculator import MovementCalculator
from Map.LosCalculator import LosCalculator


class MapHolder:
    def __init__(self,configProvider):
        self._GraphLoaded = False
        self._Consts=Constants()
        self._Csvreader = CSVMatrixReader()
        self._ConfigProvider=configProvider
        self._MovementCalculator=MovementCalculator(configProvider)
        self._LosCalculator = LosCalculator(configProvider)

    def loadMap(self,mapname):
        self._Csvreader.parse(mapname)
        if  self._Csvreader.fileLoaded:
            self.buildGraph()
        else:
            self._Map=np.asmatrix(np.ones((10,10)))
        self._Mapname = mapname

        return  self._Csvreader.fileLoaded
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
    def saveGraph(self,mapname):
        pass
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

    def getPath(self,pFrom:Point,pTo:Point,draw=False):
        if not self._Csvreader.fileLoaded:
            return PathResult([],False)
        if not self._GraphLoaded:
            return  PathResult([],False)
        dim=self.getMapDim()
        if dim.IsPointInDim(pFrom)==False:
            return  PathResult([],False)
        if dim.IsPointInDim(pTo)==False:
            return  PathResult([],False)
        NodeFrom = Point.ToGridNodeFromPoint(pFrom, dim.height)
        NodeTo = Point.ToGridNodeFromPoint(pTo, dim.height)
        path=self._MovementCalculator.getPath(NodeFrom,NodeTo,self._Graph)
        if draw and path.valid:
            graph_pos = nx.shell_layout(self._Graph)

            nx.draw_networkx_nodes(self._Graph, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
            nx.draw_networkx_edges(self._Graph, graph_pos)
            labels = {}
            for Idx in range(0, len(self._Graph.nodes().keys())):
                labels[Idx] = "({0}-{1})".format(self._Graph.nodes[Idx]["X"], self._Graph.nodes[Idx]["Y"])
            nx.draw_networkx_labels(self._Graph, graph_pos, labels=labels, font_size=12, font_family='sans-serif')

            path_edges = [(path.nodelist[n], path.nodelist[n + 1]) for n in range(len(path.nodelist) - 1)]

            nx.draw_networkx_edges(self._Graph, graph_pos, edgelist=path_edges, edge_color='r', width=10)
            plt.show()
        return path

    def buildGraph(self):
        dim=self.getMapDim()

        labels={}
        self._Graph = nx.Graph()
        for colIndex in range(0, dim.width):
            for rowIndex in range(0, dim.height):
                cord = Point.ToGridNode(colIndex, rowIndex, dim.height)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,0)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,1)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,-1)

                self.UpdateWeight(cord,colIndex,rowIndex,dim,-1,0)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,-1,1)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, -1,-1)

                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1,0)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1, -1)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1, 1)
                self._Graph.nodes[cord]["X"]=colIndex
                self._Graph.nodes[cord]["Y"] = rowIndex
                labels[cord]="({0}-{1})".format(rowIndex,colIndex)
        nx.relabel_nodes(self._Graph,labels)
        self._GraphLoaded=True
    def UpdateWeight(self,cord,colIndex,rowIndex,dim,xFactor,yFactor):
        newColIndex=colIndex+xFactor
        newRowIndex=rowIndex+yFactor

        if (newColIndex)>=dim.width:
            return
        if (newColIndex)<0:
            return
        if (newRowIndex)>=dim.height:
            return
        if (newRowIndex)<0:
            return
        #we try to go to Cover -not connected
        NextCord=Point.ToGridNode(newColIndex,newRowIndex,dim.height)
        if self._Csvreader.Matrix.item((colIndex, rowIndex)) == self._Consts.CoverNumber:
            return
        # we try to go from Cover -not connected

        if self._Csvreader.Matrix.item((newColIndex, newRowIndex)) == self._Consts.CoverNumber:
            return

        # Alt Diff Issue
        AltDiff=abs(self._Csvreader.Matrix.item((colIndex, rowIndex))-self._Csvreader.Matrix.item((newColIndex, newRowIndex)))
        if AltDiff >= self._Consts.MaximumAltDif:
            return

        #we set connectivity
        self._Graph.add_edge(NextCord, cord, weight=self._Consts.ConnectedGraphVertexWeight)


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
    def restPointsLocations(self):
        return self._Csvreader.restpoints()



