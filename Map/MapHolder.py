import os.path
import numpy as np
import pickle
from Common.Dimensions import Dimensions
from Common.Point import Point
from Common.Constant import Constants
import networkx as nx
import matplotlib.pyplot as plt

from Map.CSVMatrixReader import CSVMatrixReader
from Map.MovementCalculator import MovementCalculator


class MapHolder:
    def __init__(self,configProvider):
        self._GraphLoaded = False
        self._Consts=Constants()
        self._Csvreader = CSVMatrixReader()
        self._ConfigProvider=configProvider
        self._MovementCalculator=MovementCalculator(configProvider)

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
            plt.subplot(121)
            nx.draw(self._Graph, with_labels=True, font_weight='bold')
            plt.subplot(122)
            dim=self.getMapDim();
            numberOfNodes=(dim.height)*(dim.width)
            nx.draw_shell(self._Graph, nlist=[range(0,numberOfNodes)], with_labels=True, font_weight='bold')
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
        NodeFrom = self.getConnectivtyNodeIndexFromPoint(pFrom, dim.height)
        NodeTo = self.getConnectivtyNodeIndexFromPoint(pTo, dim.height)

        return self._MovementCalculator.mayMove(NodeFrom,NodeTo,self._Graph)



    def buildGraph(self):
        dim=self.getMapDim()


        self._Graph = nx.Graph()
        for colIndex in range(0, dim.width):
            for rowIndex in range(0, dim.height):
                cord = self.getConnectivtyNodeIndex(colIndex, rowIndex, dim.height)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,0)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,1)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,0,-1)

                self.UpdateWeight(cord,colIndex,rowIndex,dim,-1,0)
                self.UpdateWeight(cord,colIndex,rowIndex,dim,-1,1)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, -1,-1)

                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1,0)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1, -1)
                self.UpdateWeight(cord,colIndex, rowIndex, dim, 1, 1)
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
        NextCord=self.getConnectivtyNodeIndex(newColIndex,newRowIndex,dim.height)
        if self._Csvreader.Matrix.item((colIndex, rowIndex)) == self._Consts.CoverNumber:
            return
        # we try to go from Cover -not connected

        if self._Csvreader.Matrix.item((newColIndex, newRowIndex)) == self._Consts.CoverNumber:
            return

        # Alt Diff Issue
        AltDiff=abs(self._Csvreader.Matrix.item((colIndex, rowIndex))-self._Csvreader.Matrix.item((newColIndex, newRowIndex)))
        if AltDiff >= self._Consts.MaximumAltDif:
            return

        print("NextCord={0} cord={1} ConnectedGraphVertexWeight={2}".format(NextCord,cord,self._Consts.ConnectedGraphVertexWeight))
        #we set connectivity
        self._Graph.add_weighted_edges_from([(NextCord, cord, self._Consts.ConnectedGraphVertexWeight)])
    def getConnectivtyNodeIndex(self,x,y,rownumber):
        return x+(y*rownumber)
    def getConnectivtyNodeIndexFromPoint(self,point:Point,rownumber):
        return point.x+(point.y*rownumber)
    @property
    def mapLoaded(self):
        return  self._Csvreader.fileLoaded
    @property
    def graphLoaded(self):
        return self._GraphLoaded




